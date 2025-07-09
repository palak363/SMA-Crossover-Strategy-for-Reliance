import yfinance as yf

# Download data from Yahoo Finance
df = yf.download("RELIANCE.NS", start="2024-01-01", end="2025-07-01", interval="1d")

# Save to CSV
df.to_csv("reliance.csv")

print("File saved as 'reliance.csv'")
