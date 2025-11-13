import yfinance as yf, pandas as pd
PORT, HEDGE = "QQQ", "SPY"
end = pd.Timestamp.today().normalize(); start = end - pd.DateOffset(months=36)
def pull(t):
    df = yf.download(t, start=start, end=end, interval="1d", auto_adjust=True)[["Close"]]
    return df.reset_index().rename(columns={"Close":t})
df = pull(PORT).merge(pull(HEDGE), on="Date", how="inner")
df = df.rename(columns={PORT:"PortfolioClose", HEDGE:"HedgeClose"})
df.to_csv("prices_clean.csv", index=False)