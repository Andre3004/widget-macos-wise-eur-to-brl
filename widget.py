import rumps
from main import get_eur_to_brl_rate
import threading

class EuroQuoteWidget(rumps.App):
    def __init__(self):
        super().__init__("EUR → BRL", "€")
        self.update_rate()
        
    def update_rate(self):
        exchange_rate = get_eur_to_brl_rate()
        if exchange_rate:
            self.title = f"€ {exchange_rate.rate:.2f}"
        else:
            self.title = "€ --"
        
        threading.Timer(300, self.update_rate).start()

if __name__ == "__main__":
    EuroQuoteWidget().run() 