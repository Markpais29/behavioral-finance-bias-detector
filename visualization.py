import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

close = pd.read_csv('close_prices.csv', index_col=0, parse_dates=True)
herding = pd.read_csv('herding_signal.csv', index_col=0, parse_dates=True)
overreaction = pd.read_csv('overreaction_signal.csv', index_col=0, parse_dates=True)
momentum = pd.read_csv('momentum_signal.csv', index_col=0, parse_dates=True)

print("Data loaded for visualization")

stock = 'AAPL'
start_date = '2023-01-01'

price = close[stock][start_date:]
herd = herding[stock][start_date:]
over = overreaction[stock][start_date:]
mom = momentum[stock][start_date:]
plt.figure(figsize=(14,7))
plt.plot(price, label='Close Price', color='black')

# Overlay signals
plt.scatter(price.index[herd==1], price[herd==1], label='Herding', marker='^', color='blue')
plt.scatter(price.index[over==1], price[over==1], label='Overreaction', marker='o', color='red')
plt.scatter(price.index[mom==1], price[mom==1], label='Momentum', marker='s', color='green')

plt.title(f'{stock} Price with Behavioral Signals')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.tight_layout()
plt.show()
plt.figure(figsize=(12,6))
sns.heatmap(herding.T.iloc[:, -100:], cmap='Blues', cbar=True)
plt.title('Herding Signal Heatmap (last 100 days)')
plt.ylabel('Stock')
plt.xlabel('Time')
plt.tight_layout()
plt.show()

#Overreaction / Mean-Reversion Plot
plt.figure(figsize=(14,7))
plt.plot(price, label='Close Price', color='black')
plt.scatter(price.index[over==1], price[over==1], label='Overreaction', marker='o', color='red')
plt.title(f'{stock} Overreaction Signals')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.tight_layout()
plt.show()

#Momentum Plot
plt.figure(figsize=(14,7))
plt.plot(price, label='Close Price', color='black')
plt.scatter(price.index[mom==1], price[mom==1], label='Momentum', marker='s', color='green')
plt.title(f'{stock} Momentum Signals')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.tight_layout()
plt.show()

