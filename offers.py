# offers.py
import requests
from bs4 import BeautifulSoup

def scrape_grabon_offers():
    url = "https://www.grabon.in/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    offers = []
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        cards = soup.select(".coupon-card")[:5]
        for card in cards:
            merchant = card.select_one(".store")
            value = card.select_one(".c-type")
            link_tag = card.select_one("a")

            offer = {
                "merchant": merchant.text.strip() if merchant else "Unknown Merchant",
                "value": value.text.strip() if value else "Special Offer",
                "link": "https://www.grabon.in" + link_tag['href'] if link_tag and 'href' in link_tag.attrs else url,
                "expiry": "Limited Time"
            }
            offers.append(offer)

        # If scraping fails silently
        if not offers:
            raise Exception("No offer cards found")

        return offers

    except Exception as e:
        print(f"⚠️ Error scraping GrabOn: {e}")
        return fallback_mocked_offers()

def fallback_mocked_offers():
    return [
        {
            "merchant": "Amazon",
            "value": "10% cashback on electronics",
            "link": "https://www.amazon.in",
            "expiry": "May 10, 2025"
        },
        {
            "merchant": "Zomato",
            "value": "Flat ₹100 off on orders above ₹299",
            "link": "https://www.zomato.com",
            "expiry": "May 12, 2025"
        },
        {
            "merchant": "Flipkart",
            "value": "5% cashback with HDFC cards",
            "link": "https://www.flipkart.com",
            "expiry": "May 9, 2025"
        }
    ]

def get_top_offers(session):
    offers = scrape_grabon_offers()
    return offers[:3]

def get_top_offers(session):
    return [
        {
            "merchant": "Amazon",
            "value": "10% Cashback",
            "link": "https://flipbot.com/offer/amazon",
            "expiry": "May 31"
        },
        {
            "merchant": "Swiggy",
            "value": "₹100 off",
            "link": "https://flipbot.com/offer/swiggy",
            "expiry": "May 20"
        },
        {
            "merchant": "Myntra",
            "value": "Flat 15% off",
            "link": "https://flipbot.com/offer/myntra",
            "expiry": "June 5"
        }
    ]

