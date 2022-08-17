from aiohttp import request
import requests
import pandas as pd

from api_key import API_KEY

class TimeSeries( object ):

    def __init__( self, api_key ):
        self.api_key = api_key 

    def get_data( self, symbol : str, interval : str ):
        request_url = "https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}".format( symbol=symbol, interval=interval, api_key=API_KEY )
        response = requests.get( request_url )

        if ( response.status_code != 200 ):
            raise Exception( "Connectivity error with TwelveData API." )

        data = response.json()

        values = pd.DataFrame.from_dict( data['values'] )
        meta_data = data['meta']

        return meta_data, values

    def get_daily( self, symbol: str ):
        """ Returns pandas DataFrame of daily interval data for a ticker symbol """
        return self.get_data( symbol, "1day" )

    def get_weekly( self, symbol : str ):
        """ Returns pandas DataFrame of weekly interval data for a ticker symbol """
        return self.get_data( symbol, "1week" )





def time_series_data( symbol : str, interval : str ):
    """Requests time series data from the TwelveData API"""

    # Format request URL
    request_url = "https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&apikey={api_key}".format( symbol=symbol, interval=interval, api_key=API_KEY )
    # Retrive data from API endpoint
    data = requests.get( request_url )
    # 
    print ( data.json() )