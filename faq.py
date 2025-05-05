# faq.py

def answer_query(query):
    static_faqs = {
        "how does flip make money?": "💼 FLIP earns through affiliate commissions from partner merchants.",
        "how much did i save last week?": "📊 You saved ₹534 last week through FLIP! 🥳 (mocked data)"
    }
    return static_faqs.get(query.lower(), None)
