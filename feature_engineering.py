import pandas as pd
import numpy as np

# Load price and volume data
close = pd.read_csv('close_prices.csv', index_col=0, parse_dates=True)
volume = pd.read_csv('volumes.csv', index_col=0, parse_dates=True)

print("Data loaded")
# Calculate 30-day average & std of volume
volume_mean = volume.rolling(window=30).mean()
volume_std = volume.rolling(window=30).std()

volume_zscore = (volume - volume_mean) / volume_std

# Save herding signal: when z-score > 2
herding_signal = (volume_zscore > 2).astype(int)

herding_signal.to_csv('herding_signal.csv')
print("Herding signal saved")
# 20-day moving average & std
ma20 = close.rolling(window=20).mean()
std20 = close.rolling(window=20).std()

upper_band = ma20 + (2 * std20)
lower_band = ma20 - (2 * std20)

# Overreaction: price closes above upper band or below lower band
overreaction_signal = ((close > upper_band) | (close < lower_band)).astype(int)

overreaction_signal.to_csv('overreaction_signal.csv')
print("Overreaction signal saved")
# Short & long-term MAs
ma20 = close.rolling(window=20).mean()
ma50 = close.rolling(window=50).mean()
ma200 = close.rolling(window=200).mean()

momentum_signal = ((ma20 > ma50) & (ma50 > ma200)).astype(int)

momentum_signal.to_csv('momentum_signal.csv')
print("Momentum signal saved")
