from pmdarima import auto_arima
import pandas as pd
import ta
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


def master_mind(df: pd.DataFrame, timeFrame):
    print("Try to determine ...")
    if df is not None:
        df["SMA"] = ta.trend.sma_indicator(
            df["close"], window=20, fillna=True
        )  # Simple Moving Average
        df["RSI"] = ta.momentum.rsi(df["close"], fillna=True)  # Relative Strength Index
        # Prepare the data for regression
        X = df[['open', 'high', 'low', 'volume', 'SMA', 'RSI']]
        y = df['close']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

        # Create and fit the Linear Regression model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Generate predictions for future data
        future_features = X.iloc[-1, :].values.reshape(1, -1)

        future_features_df = pd.DataFrame(future_features, columns =X.columns)
        prediction = model.predict(future_features_df)

        print("Predicted close Price:", prediction)
        return prediction
