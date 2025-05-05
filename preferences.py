

def capture_preferences(session):
    print("\n🛠️ Let's set up your preferences!")

    session['categories'] = input("📂 Preferred categories (travel, food, shopping): ").lower().split(", ")
    session['location'] = input("📍 Your city or location: ").title()
    session['bank'] = input("🏦 Bank or card type (mocked): ").title()

    print("\n✅ Preferences saved! You can now ask me about the best cashback offers.")
