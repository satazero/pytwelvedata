import requests 
import pandas as pd

class TechnicalIndicators( object ):
    def __init__( self, api_key ):
        self.api_key = api_key 

    def get_indicator( self, symbol, endpoint, interval ):
        request_url = "https://api.twelvedata.com/{endpoint}?symbol={symbol}&interval={interval}&apikey={api_key}".format( endpoint=endpoint, symbol=symbol, interval=interval, api_key=self.api_key )
        response = requests.get( request_url )

        data = response.json()

        meta = data['meta']
        values = pd.DataFrame.from_dict( data['values'] )

        return meta, values

    def get_macd( self, symbol, interval ):
        return self.get_indicator( symbol, "macd", interval )

    def get_rsi( self, symbol, interval ):
        return self.get_indicator( symbol, "rsi", interval )

    def get_percent_b( self, symbol, interval ):
        return self.get_indicator( symbol, "percent_b", interval )

    def get_stoch( self, symbol, interval ):
        return self.get_indicator( symbol, "stoch", interval )

    def get_sma( self, symbol, interval ):
        return self.get_indicator( symbol, "sma", interval )

    def get_ema( self, symbol, interval ):
        return self.get_indicator( symbol, "ema", interval )

    def get_bbands( self, symbol, interval ):
        return self.get_indicator( symbol, "bbands", interval )

    def get_adx( self, symbol, interval ):
        return self.get_indicator( symbol, "adx", interval )