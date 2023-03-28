from repositories.alpha_vantage_repository import AlphaVantageRepository


if __name__ == "__main__":
    print(AlphaVantageRepository.get_intraday_time_series("IBM", "5min"))
