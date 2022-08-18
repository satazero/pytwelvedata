from pytwelvedata import TimeSeries
from pytwelvedata import TechnicalIndicators
from api_key import API_KEY
import pandas as pd

td = TechnicalIndicators( API_KEY )

meta, data = td.get_percent_b( "AAPL", "1min" )

print( data )
