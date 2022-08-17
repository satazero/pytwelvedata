from pytwelvedata import TimeSeries

from api_key import API_KEY

def test_get_daily():    
    ts = TimeSeries( API_KEY )

    meta, data = ts.get_daily("MSFT")

    assert meta['symbol'] == "MSFT"
    assert meta['interval'] == "1day"
    assert meta['currency'] == "USD"

def test_get_weekly():
    ts = TimeSeries( API_KEY )

    meta, data = ts.get_weekly("AAPL")

    assert meta['symbol'] == "AAPL"
    assert meta['interval'] == "1week"
    assert meta['currency'] == "USD"



