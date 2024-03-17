from binance.client import Client
import pandas as pd
import datetime

# Binance API creadentials
api_key = 'enter your binance API_Key'
api_secret = 'enter your binance API_Secret'

# Initialize the binance client
client = Client(api_key, api_secret)

# define the symbol and the interval
symbol ='BTCUSDT'
interval = Client.KLINE_INTERVAL_1DAY

# Fetch historikal data (the data can customize)
start_str = '1 Jan, 2017'
end_str = datetime.datetime.now().strftime("%d %b, %Y")

#fetch historical klines from binance
klines = client.get_historical_klines(symbol, interval, start_str, end_str)

#Create a DataFrame
columns = ['open_time', 'open', 'high', 'low', 'close', 'volume', 
           'close_time', 'quote_asset_volume', 'number_of_trades', 
           'taker_buy_base_volume', 'taker_buy_quote_volume', 'ignore']
df = pd.DataFrame(klines, columns=columns)

# Conjvert timestamp to readable dates
df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')
df['close_time'] = pd.to_datetime(df['close_time'], unit='ms')

# Optional: select columns to save
df = df[['open_time', 'open', 'high', 'low', 'close', 'volume']]

# save DataFrame to a csv file
csv_file = 'BTCUSDT_Historical_data.csv'
df.to_csv(csv_file, index=False)

print(f"Data saved to {csv_file}")