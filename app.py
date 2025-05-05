from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import google.generativeai as genai
from offers import get_top_offers  # Make sure this module exists and works
import os

app = Flask(__name__)

# Set up Gemini
genai.configure(api_key="AIzaSyBOiwW9uvB3lQ59ejZetel0jEuZlFxVrGE")  # Replace with your actual Gemini API key
model = genai.GenerativeModel("gemini-1.5-pro")


user_sessions = {}

# Gemini prompt template
PROMPT_TEMPLATE = """
You are Smart FLIP Bot — a friendly cashback and finance assistant helping users discover the best offers.

User preferences:
- Categories: {categories}
- City: {city}
- Bank: {bank}

User said: "{user_query}"

Provide a helpful, structured reply with:
- Top 3 cashback offers if asked
- Savings data (mocked)
- Explanation of how FLIP earns
- Friendly tone with emojis and bullets
"""

# Initialize or get existing user session
def get_user_session(phone_number):
    if phone_number not in user_sessions:
        user_sessions[phone_number] = {
            "stage": "onboarding",
            "categories": "",
            "city": "",
            "bank": ""
        }
    return user_sessions[phone_number]

@app.route("/webhook", methods=["POST"])
def whatsapp_webhook():
    incoming_msg = request.values.get("Body", "").strip()
    from_number = request.values.get("From", "")
    resp = MessagingResponse()
    msg = resp.message()

    session = get_user_session(from_number)

    # 🔁 Reset preferences if user sends reset/start
    if incoming_msg.lower() in ["reset", "start", "restart", "start over"]:
        user_sessions[from_number] = {
            "stage": "onboarding",
            "categories": "",
            "city": "",
            "bank": ""
        }
        msg.body("🔄 Preferences reset! Let's start fresh. 👋\nWhat categories are you interested in? (e.g., shopping, food, travel)")
        return str(resp)

    # Onboarding process
    if session["stage"] == "onboarding":
        if session["categories"] == "":
            session["categories"] = incoming_msg
            msg.body("📍 Great! Now, please tell me your city or location.")
            return str(resp)
        elif session["city"] == "":
            session["city"] = incoming_msg
            msg.body("🏦 Awesome! Lastly, which bank/card do you use?")
            return str(resp)
        elif session["bank"] == "":
            session["bank"] = incoming_msg
            session["stage"] = "ready"
            msg.body(
                "✅ You're all set! I’ve saved your preferences.\n\n"
                "Now you can ask me things like:\n"
                "• What are today’s cashback offers?\n"
                "• How much did I save last week?\n"
                "• How does FLIP make money?"
            )
            return str(resp)

    # Direct offer query handling
    if "offer" in incoming_msg.lower() or "cashback" in incoming_msg.lower():
        offers = get_top_offers(session)  # Custom function you provide
        if offers:
            reply = "🔥 *Top Cashback Offers Based on Your Preferences:*\n"
            for idx, offer in enumerate(offers[:3], start=1):
                reply += (
                    f"\n{idx}. 🛍 *{offer['merchant']}* — {offer['value']}\n"
                    f"🔗 {offer['link']}\n"
                    f"⏳ Expiry: {offer['expiry']}\n"
                )
        else:
            reply = "😓 No current offers found for your preferences. Try again later or update your categories."
        msg.body(reply)
        return str(resp)

    # AI response via Gemini
    try:
        prompt = PROMPT_TEMPLATE.format(
            categories=session["categories"],
            city=session["city"],
            bank=session["bank"],
            user_query=incoming_msg
        )
        gemini_response = model.generate_content(prompt)
        reply = gemini_response.text.strip()
    except Exception as e:
        print(f"Gemini error: {e}")
        reply = "⚠️ Oops! I'm having trouble thinking right now. Try again shortly."

    msg.body(reply)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
