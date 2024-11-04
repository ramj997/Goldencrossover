import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

# Set page configuration
st.set_page_config(page_title="Golden Crossover App", layout="wide")

# Title and description
st.title("Golden Crossover Signal")
st.write("This application displays buy and sell signals based on the Golden Crossover strategy.")

# Input for file selection and number of data points
file_name = st.text_input("Enter the stock symbol (file name without extension)", value="ALPA")
data_point = st.slider("Select the number of recent data points to display", min_value=100, max_value=1000, value=400,
                       step=1)


# Define the Golden Crossover Signal function with data handling and plotting
def GoldenCrossoverSignal(name, data_point):
    # path = f'../Data/{name}.csv'  # Update this path as needed
    path = f'Data/{name}.csv'  # Update this path as needed

    try:
        # Load and preprocess data
        data = pd.read_csv(path)
        data = data.drop(index=[0, 1])
        data = data.rename(columns={'Price': 'Date'})
        data['Date'] = pd.to_datetime(data['Date'])
        data['Date'] = data['Date'].dt.date
        data = data.set_index('Date')
        data = data[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]
        tochange = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
        data[tochange] = data[tochange].apply(pd.to_numeric, errors='coerce')

        # Calculate moving averages and positions
        data['20_SMA'] = data['Close'].rolling(window=20, min_periods=1).mean()
        data['50_SMA'] = data['Close'].rolling(window=50, min_periods=1).mean()
        data['Signal'] = np.where(data['20_SMA'] > data['50_SMA'], 1, 0)
        data['Position'] = data['Signal'].diff()

        # Plot data with Streamlit
        fig, ax = plt.subplots(figsize=(15, 8))
        data.iloc[-data_point:]['Close'].plot(color='k', label='Close Price', ax=ax)
        data.iloc[-data_point:]['20_SMA'].plot(color='b', label='20-day SMA', ax=ax)
        data.iloc[-data_point:]['50_SMA'].plot(color='g', label='50-day SMA', ax=ax)

        # Plot buy and sell signals
        ax.plot(data.iloc[-data_point:][data.iloc[-data_point:]['Position'] == 1].index,
                data.iloc[-data_point:]['20_SMA'][data.iloc[-data_point:]['Position'] == 1],
                '^', markersize=15, color='g', label='Buy')
        ax.plot(data.iloc[-data_point:][data.iloc[-data_point:]['Position'] == -1].index,
                data.iloc[-data_point:]['20_SMA'][data.iloc[-data_point:]['Position'] == -1],
                'v', markersize=15, color='r', label='Sell')

        ax.set_xlabel('Date')
        ax.set_ylabel('Price in Rupees')
        ax.set_title(f"{name} Golden Crossover")
        ax.legend()
        ax.grid()
        st.pyplot(fig)  # Display plot in Streamlit

        # Display table of buy and sell signals
        df_pos = data.iloc[-data_point:][(data.iloc[-data_point:]['Position'] == 1) | (data['Position'] == -1)].copy()
        df_pos['Position'] = df_pos['Position'].apply(lambda x: 'Buy' if x == 1 else 'Sell')
        st.write("### Buy and Sell Signals")
        st.write(tabulate(df_pos[['Close', 'Position']], headers='keys', tablefmt='pipe'))

    except FileNotFoundError:
        st.error(f"File '{path}' not found. Please check the file name or path.")


# Call the function with user input
if st.button("Generate Signals"):
    GoldenCrossoverSignal(file_name, data_point)

# streamlit run golden_crossover_app.py








