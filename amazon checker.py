import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com/gp/check-gift-card-balance/"
gift_codes = ["GiftCode1", "GiftCode2", "GiftCode3",...]
valid_gift_codes = []

for gift_code in gift_codes:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    data = {
        "giftCardNumber": gift_code,
        "giftCardPin": ""  # Leave pin blank if not required
    }

    response = requests.post(url, headers=headers, data=data)
    soup = BeautifulSoup(response.content, "html.parser")

    if soup.find("span", {"id": "gc-balance-amount"}) is not None:
        balance = soup.find("span", {"id": "gc-balance-amount"}).text.strip()
        valid_gift_codes.append({"gift_code": gift_code, "balance": balance})

print("Valid Gift Codes:")
for gift_code in valid_gift_codes:
    print(f"Gift Code: {gift_code['gift_code']}, Balance: {gift_code['balance']}")
