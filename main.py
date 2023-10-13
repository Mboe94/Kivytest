from kivy.app import App
from kivy.uix.label import Label
from alpha_vantage.timeseries import TimeSeries

class StockPriceApp(App):

    def build(self):
        layout = Label(text=self.get_stock_prices())
        return layout

    def get_stock_prices(self):
        api_key = '0C1MOUCLIDM7MWSP'  # Replace with your Alpha Vantage API key
        symbols = ['TSLA', 'NVDA', 'NVO', 'U']  # Symbols for Tesla, Nvidia, Novo Nordisk, and Unity
        stock_prices = ""
        try:
            ts = TimeSeries(key=api_key, output_format='json')
            for symbol in symbols:
                data, meta_data = ts.get_quote_endpoint(symbol=symbol)
                price = float(data['05. price'])  # Convert price to float
                stock_prices += f"{symbol}: ${price:.2f}\n"
            return stock_prices
        except Exception as e:
            return f"An error occurred: {e}"

if __name__ == '__main__':
    StockPriceApp().run()
