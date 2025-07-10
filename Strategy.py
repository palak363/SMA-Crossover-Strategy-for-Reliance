import pandas as pd
import matplotlib.pyplot as plt

# Loading CSV with multi-level headers
df = pd.read_csv(r"C:\Users\L2\Desktop\x\reliance.csv", skiprows=2, header=[0, 1], index_col=0, parse_dates=True)

# Flatten multi-index columns
df.columns = [f"{col[0]}_{col[1]}" for col in df.columns]

# Extract the Close price
df['Close'] = df['Unnamed: 1_level_0_1290.7442626953125']

# Calculate Moving Averages
df['SMA_5'] = df['Close'].rolling(window=5).mean()
df['SMA_20'] = df['Close'].rolling(window=20).mean()

# Generate Signals
df['Signal'] = 0
df['Signal'][df['SMA_5'] > df['SMA_20']] = 1
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
