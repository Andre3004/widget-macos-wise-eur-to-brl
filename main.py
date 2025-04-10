import requests
from bs4 import BeautifulSoup
from typing import Optional
from dataclasses import dataclass
from datetime import datetime

@dataclass
class ExchangeRate:
    rate: float
    timestamp: datetime

def get_eur_to_brl_rate() -> Optional[ExchangeRate]:
    url = "https://wise.com/br/currency-converter/eur-to-brl-rate"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        rate_element = soup.select_one("h3:-soup-contains('EUR = ')")
        
        if not rate_element:
            return None
            
        rate_text = rate_element.text.strip()
        rate_value = rate_text.split("=")[1].replace("BRL", "").replace(",", ".").replace("R$", "").strip()
        rate = float(rate_value)
        
        return ExchangeRate(
            rate=rate,
            timestamp=datetime.now()
        )
        
    except Exception as e:
        print(f"Error fetching exchange rate: {e}")
        return None

def main():
    exchange_rate = get_eur_to_brl_rate()
    
    if exchange_rate:
        print(f"Current EUR to BRL exchange rate:")
        print(f"1 EUR = R$ {exchange_rate.rate:.4f}")
        print(f"Last updated: {exchange_rate.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print("Failed to fetch exchange rate")

if __name__ == "__main__":
    main()
