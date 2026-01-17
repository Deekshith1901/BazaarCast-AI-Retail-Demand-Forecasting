from sklearn.metrics import mean_absolute_error

def train_model(model, train_df):
    model.fit(train_df[["t"]], train_df["Sales"])
    return model

def evaluate_model(model, test_df):
    preds = model.predict(test_df[["t"]])
    return mean_absolute_error(test_df["Sales"], preds)
