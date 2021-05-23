lags = [x for x in range(28, 28+8)]
windows = [3, 7]

lag_cols = [f"lag_{lag}" for lag in lags ]
for lag, lag_col in zip(lags, lag_cols):
    print('Lag {}'.format(lag))
    X[lag_col] = X.groupby("id")["demand"].shift(lag)

lags = [28]
for window in windows:
    for lag,lag_col in zip(lags, lag_cols):
        print("Lag {}, window {}".format(lag, window))
        X[f"rmean_{lag}_{window}"] = X[["id", lag_col]].groupby("id")[lag_col].\
        transform(lambda x : x.rolling(window).mean())
