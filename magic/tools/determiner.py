
from pmdarima import auto_arima
import pandas as pd

def determiner(df, timeFrame):
    print('Try to determine ...')
    if df is not None:
        # Fit the AutoARIMA model
        model = auto_arima(df['y'], seasonal=False, suppress_warnings=True)

        print(df)
        print(df.index[-1].ds)
        # Forecast future values
        future_dates = pd.date_range(start=df.index[-1]['ds'], periods=14, freq=timeFrame)
        forecasted_values = model.predict(n_periods=len(future_dates))

        # Print the forecasted values
        forecast_df = pd.DataFrame({'ds': future_dates, 'yhat': forecasted_values})
        forecast_df = forecast_df.set_index('ds')
        print(forecast_df)