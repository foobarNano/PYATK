import pandas
import tkinter
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import normalize

def load_data() -> pandas.DataFrame:
    with open("PR/data/init") as init:
        train_path = init.readline().rstrip()
        headers = [e.rstrip() for e in init.readlines()]
        return pandas.read_csv(f"PR/data/{train_path}", names=headers)

def train_model(df):
    X = X = df.iloc[1:, :-1].values
    print(X)
    X = normalize(X)
    y = df.iloc[:, -1].values

    model = RandomForestClassifier(n_estimators=10, random_state=2137)
    model.fit(X, y)
    return model

def test_model(model, test_path: str) -> float:
    test_df = pandas.read_csv(f"PR/data/{test_path}")
    X = X = df.iloc[:, :-1].values
    X = normalize(X)
    true_y = df.iloc[:, -1].values

    pred_y = model.predict(X)
    return accuracy_score(true_y, pred_y)

df = load_data()
model = train_model(df)
acc = test_model(model, "test.data")
print(f"Accuracy: {acc}")
