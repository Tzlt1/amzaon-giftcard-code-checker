import requests
import time

def check_gift_card(session, code):
    url = "https://www.amazon.com/gp/gc/redeem"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    }
    data = {
        "c": code,
    }

    try:
        response = session.post(url, headers=headers, data=data, timeout=10)
        if response.status_code == 200:
            if "Enter the claim code" in response.text:
                print(f"The gift card code {code} is valid and can be redeemed.")
            else:
                print(f"The gift card code {code} is not valid or has already been redeemed.")
        else:
            print(f"Failed to check the validity of the gift card code {code}. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while checking the gift card code {code}: {e}")

def check_gift_cards(codes):
    with requests.Session() as session:
        retries = 3
        for code in codes:
            for attempt in range(retries):
                try:
                    check_gift_card(session, code)
                    break
                except Exception as e:
                    print(f"Attempt {attempt + 1}/{retries} failed for gift card code {code}: {e}")
                    time.sleep(1)  # Wait for 1 second before retrying
            else:
                print(f"Failed to check gift card code {code} after {retries} attempts.")

if __name__ == "__main__":
    num_codes = int(input("Enter the number of Amazon gift card codes to check: "))
    codes = []
    for i in range(num_codes):
        code = input(f"Enter gift card code {i+1}: ")
        codes.append(code)

    check_gift_cards(codes)
