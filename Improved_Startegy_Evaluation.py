import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv(r"C:\Users\L2\Desktop\IP_project\reliance.csv", skiprows=2, header=[0, 1], index_col=0, parse_dates=True)
df.columns = [f"{col[0]}_{col[1]}" for col in df.columns]

# Extract Close price (update this column name if needed)
df['Close'] = df['Unnamed: 1_level_0_1290.7442626953125']

# Calculate Moving Averages
df['SMA_5'] = df['Close'].rolling(window=5).mean()
df['SMA_20'] = df['Close'].rolling(window=20).mean()

# Strategy Logic with Confirmation Filter
df['Signal'] = 0
df.loc[df['SMA_5'] > df['SMA_20'] * 1.002, 'Signal'] = 1  # Buy when 5-SMA is >0.2% above 20-SMA
df.loc[df['SMA_5'] < df['SMA_20'] * 0.998, 'Signal'] = -1  # Sell when 5-SMA is >0.2% below 20-SMA
df['Position'] = df['Signal'].diff()

# Backtest Logic
trades = []
in_position = False
buy_price = 0
buy_date = None

for i in range(1, len(df)):
    if df['Position'].iloc[i] == 1 and not in_position:
        buy_price = df['Close'].iloc[i]
        buy_date = df.index[i]
        in_position = True

    elif df['Position'].iloc[i] == -1 and in_position:
        sell_price = df['Close'].iloc[i]
        sell_date = df.index[i]
        profit = sell_price - buy_price
        return_pct = (profit / buy_price) * 100
        if return_pct > 0.5:  # Only accept trades with >0.5% return
            trades.append({
                'Buy Date': buy_date,
                'Buy Price': round(buy_price, 2),
                'Sell Date': sell_date,
                'Sell Price': round(sell_price, 2),
                'Profit (Rs.)': round(profit, 2),
                'Return (%)': round(return_pct, 2)
            })
        in_position = False

# Create trades DataFrame
trades_df = pd.DataFrame(trades)

# === Evaluation ===
total_trades = len(trades_df)
total_profit = trades_df['Profit (Rs.)'].sum()
average_return = trades_df['Return (%)'].mean()
win_rate = (trades_df['Profit (Rs.)'] > 0).mean() * 100 if total_trades > 0 else 0
max_profit = trades_df['Profit (Rs.)'].max() if total_trades > 0 else 0
min_profit = trades_df['Profit (Rs.)'].min() if total_trades > 0 else 0

# Print Evaluation
print("\n==== STRATEGY EVALUATION ====")
print(f"Total Trades: {total_trades}")
print(f"Total Profit (Rs.): {round(total_profit, 2)}")
print(f"Average Return per Trade (%): {round(average_return, 2)}")
print(f"Win Rate: {round(win_rate, 2)}%")
print(f"Max Profit (Rs.): {round(max_profit, 2)}")
print(f"Min Profit (Rs.): {round(min_profit, 2)}")
print("\nTrade Details:")
print(trades_df)

# === Plotting ===
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

plt.title("Improved SMA Crossover Strategy on RELIANCE")
plt.xlabel("Date")
plt.ylabel("Price (INR)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
