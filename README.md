# SMA Crossover Strategy for Reliance (with Evaluation & Improvements)

This project implements and improves a basic algorithmic trading strategy on Reliance Industries stock data using a Simple Moving Average (SMA) crossover technique. Initially, the strategy resulted in negative returns, which led to the development of an evaluation script and an improved version of the strategy that now delivers consistent positive returns.

---

## Project Overview

This repository contains:

* A basic SMA crossover strategy
* An enhanced strategy version with signal confirmation logic
* A backtesting and evaluation framework to assess trade performance

---

## Strategy Logic

### Basic Strategy

The initial approach is based on the following conditions:

* **SMA-5**: 5-day Simple Moving Average
* **SMA-20**: 20-day Simple Moving Average

**Signals:**

* **Buy Signal**: When SMA-5 crosses above SMA-20
* **Sell Signal**: When SMA-5 crosses below SMA-20

This strategy is simple but prone to false signals and frequent whipsaws, which led to negative overall returns in backtesting.

---

### Improved Strategy

To improve the performance, a confirmation threshold was introduced to reduce noise:

* **Buy** when: `SMA_5 > SMA_20 * 1.002`
* **Sell** when: `SMA_5 < SMA_20 * 0.998`
* Trades are only accepted if the **return > 0.5%**

This reduces overtrading and filters out low-confidence signals.

---

## Evaluation Metrics

The improved strategy evaluates the following:

* Total number of trades executed
* Total profit (in INR)
* Average return per trade (%)
* Win rate (%)
* Maximum and minimum profit per trade

Results are printed in the console along with trade-wise details.

---

## Files Included

| File Name                         | Description                                                                   |
| --------------------------------- | ----------------------------------------------------------------------------- |
| `reliance.csv`                    | Historical price data for Reliance Industries (e.g., downloaded from Zerodha) |
| `Strategy_Evaluation-1.py`        | Basic SMA crossover strategy and evaluation                                   |
| `Improved_Strategy_Evaluation.py` | Enhanced strategy with filtered signals and trade evaluation                  |

---

## Output

Both versions of the script generate a plot showing:

* Close Price
* SMA-5 and SMA-20
* Buy signals (green upward arrows)
* Sell signals (red downward arrows)

This visualizes key entry and exit points across the historical period.

---

## Results Summary

The improved strategy delivered positive results compared to the original approach by:

* Filtering out low-confidence trades
* Avoiding unnecessary entries and exits
* Setting a minimum profit threshold

These enhancements resulted in a more robust and profitable trading strategy.
