import requests
import settings


class AlphaVantageRepository:
    
    @staticmethod
    def get_intraday_time_series(symbol, interval):
        api_url = settings.URL_BASE_ALPHA_VANTAGE + "query?function=TIME_SERIES_INTRADAY&symbol=" + symbol + "&interval=" + interval + "&apikey=" + settings.ALPHA_VANTAGE_API_KEY
        response = requests.get(api_url)
        return response.json()
    
    

