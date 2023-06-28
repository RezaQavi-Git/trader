
from pmdarima import auto_arima
import pandas as pd
import ta
from sklearn.linear_model import LinearRegression


def master_mind(df: pd.DataFrame, timeFrame):
    print('Try to determine ...')
    if df is not None:
        df['SMA'] = ta.trend.sma_indicator(df['close'], window=20, fillna=True)  # Simple Moving Average
        df['RSI'] = ta.momentum.rsi(df['close'], fillna=True)  # Relative Strength Index

        # Prepare the data for regression
        X = df[['SMA', 'RSI']] 
        y = df['close']

        # Create and fit the Linear Regression model
        model = LinearRegression()
        model.fit(X, y)


        # Generate predictions for future data
        future_sma = df['SMA'].iloc[-1] 
        future_rsi = df['RSI'].iloc[-1] 
        future_data = pd.DataFrame({'SMA': [future_sma], 'RSI': [future_rsi]})
        prediction = model.predict(future_data)

        print("Predicted close Price:", prediction)

        return prediction