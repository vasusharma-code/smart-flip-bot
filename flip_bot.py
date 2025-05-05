# flip_bot.py
from offers import get_top_offers

class FLIPBot:
    def __init__(self):
        self.user_prefs = {
            "categories": "shopping",
            "location": "delhi",
            "bank": "HDFC"
        }

    def chat(self, message):
        msg = message.lower()
        if "how does flip make money" in msg:
            return "💼 FLIP earns through affiliate commissions from partner merchants."
        elif "how much did i save" in msg:
            return "📊 You saved ₹534 last week through FLIP! 🥳 (mocked data)"
        elif "cashback" in msg or "top offers" in msg:
            offers = get_top_offers(self.user_prefs)
            if not offers:
                return "😓 Sorry, no offers available at the moment."
            reply = "🔥 Top Cashback Offers for You:\n"
            for offer in offers:
                reply += f"\n🛒 {offer['merchant']} - {offer['value']}\n🔗 {offer['link']}\n⏳ Expiry: {offer['expiry']}\n"
            return reply
        else:
            return "🤖 I can help with cashback offers, savings tips, and FLIP info. Try asking: 'What are the top cashback offers?'"

