# Copyright 2026 Saudi Agentic AI Entrepreneurship Academy contributors
# Licensed under the Apache License, Version 2.0
"""The application around the model: validation, tools, limits, approval and escalation.

The model proposes; this code decides. Every limit that matters is enforced here, outside
the model: input formats, ownership of an order, which tools exist, and who approves.
"""
import os

from .model import INTENTS
from .text import mask_phone, western_digits
from .tools import ToolInputError

STATUS_AR = {"processing": "قيد التجهيز", "shipped": "شُحن", "out_for_delivery": "خرج للتوصيل", "delivered": "تم التسليم"}
OUT_OF_SCOPE = {"cancel": "طلب إلغاء", "refund": "طلب استرداد", "address_change": "طلب تغيير عنوان", "complaint": "شكوى"}
STOP_FILE = "STOP"


def stopped():
    """The stop switch: a file named STOP in the working directory, or SAAEA_AGENT_STOP=1."""
    return os.path.exists(STOP_FILE) or os.environ.get("SAAEA_AGENT_STOP") == "1"


class Agent:
    def __init__(self, model, store, ownership_check="app", normalise_digits=False, answer_only_from_policy=False):
        self.model, self.store = model, store
        self.ownership_check = ownership_check            # "app": enforced here. "prompt": only a sentence in the instructions
        self.normalise_digits = normalise_digits
        self.answer_only_from_policy = answer_only_from_policy

    def handle(self, message, account, notes=""):
        """One customer message in, one result out. `notes` is untrusted data and is never read as instructions."""
        result = {"account": mask_phone(account), "intent": "unknown", "action": None, "tool_calls": [],
                  "pending_approval": [], "escalated_to_human": False, "urgent": False, "reply_draft": "", "summary": ""}
        if stopped():
            return self._escalate(result, "stopped", "الوكيل موقوف. كل الرسائل تُحال إلى الموظفة.")
        if self.normalise_digits:
            message = western_digits(message)
        understood = self.model.understand(message)
        intent = understood.get("intent")
        if intent not in INTENTS:                           # never trust the shape of model output
            intent = "unknown"
        result["intent"] = intent
        result["urgent"] = bool(understood.get("urgent"))
        if intent in OUT_OF_SCOPE:
            if intent == "cancel" and understood.get("conditional"):
                result["intent"] = "conditional_cancel"
                return self._escalate(result, "escalate", "طلب إلغاء مشروط%s. لم يُنفَّذ شيء." % ("، عاجل" if result["urgent"] else ""))
            return self._escalate(result, "escalate", "%s. خارج نطاق الوكيل، ولم يُنفَّذ شيء." % OUT_OF_SCOPE[intent])
        if intent == "shipping_question":
            return self._shipping(result, understood.get("city"))
        if intent == "order_status":
            return self._order_status(result, understood.get("order_id"), account)
        return self._escalate(result, "escalate", "رسالة لم تُفهم. تُحال كما هي.")

    def _escalate(self, result, action, summary):
        result.update(action=action, escalated_to_human=True, summary=summary,
                      reply_draft="شكراً لتواصلك. حوّلنا طلبك إلى الموظفة المختصة وستتواصل معك.")
        return result

    def _shipping(self, result, city):
        result["tool_calls"].append({"tool": "get_shipping_policy", "input": city})
        entry = self.store.get_shipping_policy(city) if city else None
        if entry:
            result.update(action="reply_policy", reply_draft="مدة الشحن إلى %s: %s، بحسب سياسة الشحن المعتمدة." % (city, entry["duration"]))
        elif self.answer_only_from_policy:
            return self._escalate(result, "escalate", "سؤال شحن لا جواب له في السياسة المعتمدة.")
        else:                                               # the gap you will find in Module 2.8: an answer with no source
            result.update(action="reply_policy", reply_draft="مدة الشحن عادةً من 3 إلى 5 أيام عمل.")
        return result

    def _order_status(self, result, order_id, account):
        if not order_id:
            result.update(action="ask_order_id", reply_draft="أهلاً بك. فضلاً زوّدنا برقم الطلب المكوّن من خمسة أرقام لنتحقق من حالته.")
            return result
        if self.ownership_check == "app" and self.store.owner_of(order_id) not in (None, account):
            result.update(action="refuse_ownership", reply_draft="عذراً، لا نستطيع مشاركة بيانات طلب مسجّل على حساب آخر. يمكن لصاحب الطلب مراسلتنا من رقمه.")
            return result
        result["tool_calls"].append({"tool": "get_order_status", "input": order_id})
        try:
            status = self.store.get_order_status(order_id)
        except ToolInputError:
            result.update(action="tool_input_error", summary="مدخل غير صالح للأداة: %r" % (order_id,))
            return self._escalate(result, "tool_input_error", result["summary"])
        if status is None:
            result.update(action="reply_not_found", reply_draft="لم نجد طلباً بالرقم %s. فضلاً تأكد من الرقم وأعد إرساله." % order_id)
            return result
        draft = "أهلاً بك. حالة طلبك رقم %s: %s. آخر تحديث قبل %d يوم." % (order_id, STATUS_AR[status["status"]], status["days_since_update"])
        if status["status"] != "delivered" and status["days_since_update"] > self.store.followup_after_days():
            result["pending_approval"].append({"tool": "create_followup_ticket", "order_id": order_id, "level": "B"})
            draft += " نقترح فتح طلب متابعة مع فريق الشحن."
        result.update(action="reply_status", reply_draft=draft)
        return result

    def approve(self, pending, approved_by):
        """A named person approves a level B action. Nothing at level B runs without this call."""
        return self.store.create_followup_ticket(pending["order_id"], approved_by)
