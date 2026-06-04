# ============================================================
# PROJECT: Stock Market Trend Classifier - Finance
# ============================================================
#
# DATASET:
#   Source 1: IndianAPI /historical_data endpoint
#             - TCS (TCS.NS) and Infosys (INFY.NS)
#             - Period: max (full history to present)
#             - One-time fetch, saved as tcs_raw.json / infy_raw.json
#
#   Source 2: IndianAPI /stock endpoint (M3 only)
#             - Live current-day price for real-time inference
#
# FEATURES (X columns):
#   1. RSI_14        → 14-day Relative Strength Index
#   2. MACD          → MACD line (12-day EMA - 26-day EMA)
#   3. MACD_Signal   → 9-day EMA of MACD line
#   4. MA_50         → 50-day Moving Average of closing price
#
# TARGET (y column):
#   label → 1 (Up) if closing price 5 days later > today's close
#           0 (Down) otherwise
#
# QUESTION THIS MODEL ANSWERS:
#   "Based on today's technical indicators for TCS or Infosys,
#    will the stock price be higher or lower 5 trading days
#    from now?"
#
# ============================================================