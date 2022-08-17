from pytwelvedata import TimeSeries
from api_key import API_KEY
import pandas as pd

ts = TimeSeries( API_KEY )

meta, data = ts.get_daily("MSFT")

print(data)
