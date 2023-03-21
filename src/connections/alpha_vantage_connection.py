import requests


class AlphaVantageConnection:
    
    @staticmethod
    def connect():
        api_url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo"
        response = requests.get(api_url)
        return response.json()
