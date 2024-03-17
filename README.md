# BinanceTradingBot

## Binance Historical Data Fetcher

### Overview
This script fetches historical trading data from the Binance cryptocurrency exchange for the BTCUSDT trading pair and saves it to a CSV file. It utilizes the Binance API to retrieve daily kline (candlestick) data from a specified start date to the current date. The data includes open, high, low, close, and volume information, which is crucial for financial analysis and trading strategy development.

### Requirements
- Python 3.x
- pandas
- python-binance

### Installation
Before running the script, ensure you have Python installed on your system. You can then install the required Python packages using pip:

`pip install pandas python-binance`

### Setup

1. Obtain your Binance API Key and Secret:

- Log in to your Binance account and navigate to the API Management page.
- Create a new API key. Ensure you keep the Secret Key safe and do not share it with others.

2. Open the script and enter your Binance API Key and Secret in the following section:

```bash
api_key = 'enter your binance API_Key'
api_secret = 'enter your binance API_Secret'
```

### Usage
To run the script and fetch historical data, simply execute the following command in your terminal:
```bash
python binance_data_fetcher.py
```
The script will fetch the historical data and save it to BTCUSDT_Historical_data.csv in the same directory as the script.


### Security Note
`Important`: Never commit your API keys or secrets to version control systems like Git. It's recommended to use environment variables or configuration files that are not tracked in your version control system to manage sensitive information.

### Contributing
Contributions are welcome! If you have suggestions for improvements or bug fixes, please feel free to submit a pull request or open an issue.


# BOT.py `in develop... mode...` 
