def trade_decision(market_trend):
    if market_trend == "bullish":
        return "Consider buying growth stocks or ETFs."
    elif market_trend == "bearish":
        return "Consider selling volatile assets or holding cash."
    elif market_trend == "volatile":
        return "Use hedging strategies like options or stay defensive."
    elif market_trend == "stable":
        return "Focus on long-term investments and diversification."
    else:
        return "Trend not recognized. Please consult an analyst."

# --- Example Usage ---
market_trend = input("Enter market trend (bullish/bearish/volatile/stable): ").lower()
print(trade_decision(market_trend))