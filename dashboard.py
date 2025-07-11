import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

close = pd.read_csv('close_prices.csv', index_col=0, parse_dates=True)
herding = pd.read_csv('herding_signal.csv', index_col=0, parse_dates=True)
overreaction = pd.read_csv('overreaction_signal.csv', index_col=0, parse_dates=True)
momentum = pd.read_csv('momentum_signal.csv', index_col=0, parse_dates=True)

st.title("📈 Behavioral Finance Bias Detector")

# 📋 Stock & date selector
stocks = close.columns.tolist()
stock = st.selectbox("Select Stock", stocks)
start_date = st.date_input("Start Date", value=close.index[0].date())
end_date = st.date_input("End Date", value=close.index[-1].date())

price = close[stock][str(start_date):str(end_date)]
herd = herding[stock][str(start_date):str(end_date)]
over = overreaction[stock][str(start_date):str(end_date)]
mom = momentum[stock][str(start_date):str(end_date)]

# 📊 Plot
fig, ax = plt.subplots(figsize=(14,7))
ax.plot(price, label='Close Price', color='black')
ax.scatter(price.index[herd==1], price[herd==1], label='Herding', marker='^', color='blue')
ax.scatter(price.index[over==1], price[over==1], label='Overreaction', marker='o', color='red')
ax.scatter(price.index[mom==1], price[mom==1], label='Momentum', marker='s', color='green')
ax.set_title(f'{stock} Price with Behavioral Signals')
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.legend()
st.pyplot(fig)

# 📈 Heatmap option
if st.checkbox("Show Herding Heatmap (last 100 days)"):
    import seaborn as sns
    fig2, ax2 = plt.subplots(figsize=(12,6))
    sns.heatmap(herding.T.iloc[:, -100:], cmap='Blues', cbar=True, ax=ax2)
    ax2.set_title('Herding Signal Heatmap (last 100 days)')
    ax2.set_ylabel('Stock')
    ax2.set_xlabel('Time')
    st.pyplot(fig2)
