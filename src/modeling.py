from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

def run_model(df):
    print("Running logistic regression model...")

    features = ["loan_amnt", "int_rate", "annual_inc", "dti", "emp_length"]
    X = df[features].dropna()
    y = df.loc[X.index, "default"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    probs = model.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, probs)

    return auc
