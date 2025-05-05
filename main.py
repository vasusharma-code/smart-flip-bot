# main.py
from offers import get_top_offers
import os

def onboarding():
    print("\n🛠️ Let's set up your preferences!")
    categories = input("📂 Preferred categories (travel, food, shopping): ").strip().lower().split(",")
    city = input("📍 Your city or location: ").strip()
    bank = input("🏦 Bank or card type (mocked): ").strip()

    session = {
        "categories": [c.strip() for c in categories],
        "city": city,
        "bank": bank
    }

    print("\n✅ Preferences saved! You can now ask me about the best cashback offers.\n")
    return session

def answer_query(user_input, session):
    user_input = user_input.lower()

    if "offer" in user_input or "cashback" in user_input:
        offers = get_top_offers(session)
        if offers:
            print("\n🔥 Top Cashback Offers for You:\n")
            for offer in offers:
                print(f"🛒 {offer['merchant']} - {offer['value']}")
                print(f"🔗 {offer['link']}")
                print(f"⏳ Expiry: {offer['expiry']}\n")
        else:
            print("😓 Sorry, no offers available at the moment.")
    elif "save" in user_input and "week" in user_input:
        print("📊 You saved ₹534 last week through FLIP! 🥳 (mocked data)")
    elif "how" in user_input and "flip" in user_input and "money" in user_input:
        print("💼 FLIP earns through affiliate commissions from partner merchants.")
    else:
        print("🤔 Sorry, I didn't understand that. You can ask about cashback offers or savings.")

def chatbot():
    print("🤖 Welcome to FLIP Smart Assistant!")
    session = onboarding()

    while True:
        user_input = input("💬 You: ").strip()
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("👋 Goodbye!")
            break
        answer_query(user_input, session)

if __name__ == "__main__":
    chatbot()
