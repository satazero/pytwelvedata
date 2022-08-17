# PyTwelveData

A naive wrapper for TwelveData's financial data API endpoints. 
An API key subscription is required, and can be acquired from [TwelveData's website](https://twelvedata.com/pricing).

Special thanks to Romel Torres [Alpha Vantage API](https://github.com/RomelTorres/alpha_vantage) for giving me a good framework to build off of. 

# Installation

Clone the repository to the local machine:

```
git clone !!REPOSITORY_URL!!
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
API_KEY = "example_api_key_from_twelve_data"
```

Include this package into your Python project:

```
import pytwelvedata
```

# Functionality

Virtually none as of writing this.