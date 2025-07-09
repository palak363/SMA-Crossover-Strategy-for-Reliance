# SMA Crossover Strategy for Reliance

This project demonstrates a simple algorithmic trading strategy using historical stock data for Reliance Industries. The strategy is based on identifying crossover points between two simple moving averages (SMAs) to generate buy and sell signals.

---

## Project Overview

The SMA crossover strategy implemented here uses:

- SMA-5: 5-day Simple Moving Average  
- SMA-20: 20-day Simple Moving Average  

Signals are generated as follows:
- Buy Signal: When SMA-5 crosses above SMA-20  
- Sell Signal: When SMA-5 crosses below SMA-20  

---

## Files Included

- `reliance.csv` – Historical price data (downloaded from Zerodha)
- `Strategy.py` – Python script for signal generation and chart plotting

---

## Output

The script produces a line chart with:
- Close Price
- 5-day and 20-day SMAs
- Buy signals (marked with green arrows)
- Sell signals (marked with red arrows)

This helps visualize key trend reversal points.

---

## How to Run

1. Download this repository
2. Ensure `reliance.csv` is in the same directory as `Strategy.py`
3. Run the script:

```bash
python Strategy.py
```

The chart window will open displaying the crossover signals.
