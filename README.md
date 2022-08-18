# PyTwelveData

A naive wrapper for TwelveData's financial data API endpoints. 
An API key subscription is required, and can be acquired from [TwelveData's website](https://twelvedata.com/pricing).

Special thanks to Romel Torres [Alpha Vantage API](https://github.com/RomelTorres/alpha_vantage) for giving me a good framework to build off of. 

# Installation

Clone the repository to the local machine:

```
git clone https://github.com/satazero/pytwelvedata
```

Create a virtual environment

```
python3 -m venv /path/to/virtual/environment
```

Install package dependencies:

```
pip install -r requirements.txt
```

Create a file `api_key.py` in the base directory of this project including your API key.

```
# ./api_key.py

API_KEY = "example_api_key_from_twelve_data"
```

Include this package into your Python project:

```
import pytwelvedata
```

# Functionality

Simplistic access to TwelveData API without having to handcraft requests yourself. Mostly used as a tool in building my personal proof of concept models. 
Written before finding the official TwelveData Python package, but still provides a simplistic interface for accessing similar functionality. Additionally,
its functionality is limited to what it is accessible only with the free/basic subscription plan.

Currently supports the gamut of Time Series data endpoints, as well as the Technical Indicator endpoints.