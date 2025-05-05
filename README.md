# FLIP Smart Chatbot MVP

## Overview
FLIP Smart Chatbot is a prototype assistant that helps users discover live cashback and reward offers, answers finance-related FAQs, and adapts to user preferences. The bot is designed for WhatsApp deployment and simulates a real assistant experience.

---

## Features

1. **User Onboarding & Preference Capture**
   - Asks users for preferred categories (e.g., travel, food, shopping), city/location, and bank/card type.
   - Stores preferences in session memory for personalized responses.

2. **Web Scraping for Live Offers**
   - Scrapes sample deal websites (e.g., GrabOn) or uses mocked data to fetch live cashback offers.
   - Returns top 3 offers based on user preferences.
   - Each offer includes merchant name, offer value, link, and expiry.

3. **Conversational Intelligence**
   - Users can ask about best offers, savings (mocked), and how FLIP earns money.
   - Integrates with Google Gemini (Generative AI) for friendly, fallback responses.
   - Handles unclear questions gracefully.

4. **WhatsApp Integration**
   - Deployable via Twilio WhatsApp Sandbox (or similar platforms).
   - Text-based UI with structured formatting (emojis, bullets).

---

## Tech Stack
- **Python** (Flask for web server)
- **Twilio** (WhatsApp API)
- **Google Gemini** (LLM for conversational AI)
- **BeautifulSoup** (Web scraping)
- **Session memory** (in-memory dict for user sessions)

---

## Scraping Logic
- `offers.py` contains scraping logic for deal sites (e.g., GrabOn).
- If scraping fails, returns mocked offers for demo reliability.
- Each offer includes merchant, value, link, and expiry fields.

---

## Flow Design
1. User sends a message on WhatsApp.
2. Bot onboards user by asking for preferences (categories, city, bank).
3. Preferences are stored in a session (per phone number).
4. User can ask for offers, savings, or FLIP info.
5. Bot fetches offers (scraped or mocked) and responds in a friendly, structured format.
6. For general queries, Gemini LLM generates a conversational reply.
7. GEMINI_API_KEY="AIzaSyBOiwW9uvB3lQ59ejZetel0jEuZlFxVrGE"
---

## Preference Handling
- User preferences are stored in a session dictionary keyed by phone number.
- Used to personalize offer recommendations and responses.

---

## WhatsApp Integration Steps
1. **Set up Twilio WhatsApp Sandbox:**
   - Create a Twilio account and enable WhatsApp Sandbox.
   - Configure webhook URL to point to your Flask app's `/webhook` endpoint.
2. **Run the Flask app:**
   - Install dependencies: `pip install flask twilio google-generativeai beautifulsoup4 requests`
   - Start the server: `python app.py`
3. **Test on WhatsApp:**
   - Send messages to your Twilio Sandbox number to interact with the bot.


---

## Demo

https://www.loom.com/share/85bb05d17cc1471f8944da4621336c99?sid=71a875af-bd55-4d53-9fab-e04e858e1d44
---

**Note:** Message delivery and response speed may be slow because the APIs used (Gemini and Twilio) are on free tiers. Gemini replies may also be truncated or not fully shown due to Twilio's free API limitations and Flask response handling.

## License
MIT
