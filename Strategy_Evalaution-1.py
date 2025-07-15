import pandas as pd
import matplotlib.pyplot as plt

# Load CSV with multi-level headers
df = pd.read_csv(r"C:\Users\L2\Desktop\IP_project\reliance.csv", skiprows=2, header=[0, 1], index_col=0, parse_dates=True)

# Flatten multi-index columns (e.g., ('Close', 'RELIANCE.NS') → 'Close_RELIANCE.NS')
df.columns = [f"{col[0]}_{col[1]}" for col in df.columns]


# Extract the Close price
#df['Close'] = df.filter(like='Close_').iloc[:, 0]
df['Close'] = df['Unnamed: 1_level_0_1290.7442626953125']


# Calculate Moving Averages
df['SMA_5'] = df['Close'].rolling(window=5).mean()
df['SMA_20'] = df['Close'].rolling(window=20).mean()

# Generate Signals
df['Signal'] = 0
#df['Signal'][df['SMA_5'] > df['SMA_20']] = 1
df.loc[df['SMA_5'] > df['SMA_20'], 'Signal'] = 1
df['Position'] = df['Signal'].diff()

# Plotting
plt.figure(figsize=(14, 7))
plt.plot(df['Close'], label='Close Price', alpha=0.6)
plt.plot(df['SMA_5'], label='5-Day SMA', linestyle='--')
plt.plot(df['SMA_20'], label='20-Day SMA', linestyle='--')

# Buy signals
plt.plot(df[df['Position'] == 1].index,
         df['SMA_5'][df['Position'] == 1],
         '^', markersize=12, color='green', label='Buy Signal')

# Sell signals
plt.plot(df[df['Position'] == -1].index,
         df['SMA_5'][df['Position'] == -1],
         'v', markersize=12, color='red', label='Sell Signal')

plt.title("SMA Crossover Strategy on RELIANCE")
plt.xlabel("Date")
plt.ylabel("Price (INR)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


#----Evaluation-----

# Extract signals
signals = df[df['Position'].isin([1, -1])].copy()

# Reset index to make iteration easier
signals = signals.reset_index()

# Initialize trade list
trades = []

# Simulate trades
position_open = False
for i in range(len(signals)):
    signal = signals.loc[i, 'Position']
    date = signals.loc[i, 'index']
    price = signals.loc[i, 'Close']

    if signal == 1 and not position_open:
        # Buy signal
        buy_date = date
        buy_price = price
        position_open = True

    elif signal == -1 and position_open:
        # Sell signal
        sell_date = date
        sell_price = price
        position_open = False
        profit = sell_price - buy_price
        return_pct = (sell_price - buy_price) / buy_price * 100
        trades.append({
            'Buy Date': buy_date,
            'Buy Price': buy_price,
            'Sell Date': sell_date,
            'Sell Price': sell_price,
            'Profit (Rs.)': profit,
            'Return (%)': return_pct
        })

# Convert trades to DataFrame
trades_df = pd.DataFrame(trades)

# Show summary
total_profit = trades_df['Profit (Rs.)'].sum()
avg_return = trades_df['Return (%)'].mean()
total_trades = len(trades_df)

print("Total Trades:", total_trades)
print("Total Profit (Rs.):", round(total_profit, 2))
print("Average Return per Trade (%):", round(avg_return, 2))
print(trades_df)

