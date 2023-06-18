import pandas as pd
import ssl
from sklearn.model_selection import train_test_split, KFold, cross_val_score, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

ssl._create_default_https_context = ssl._create_unverified_context
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
headers = ["sepal_length", "sepal_width", "petal_length", "petal_width", 
"class"]
df = pd.read_csv(url,names=headers)
print(df.head())

X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=2023, shuffle=True)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train,y_train)

fold = KFold(n_splits=5, shuffle=True, random_state=2023)
scores = cross_val_score(knn, X=X_train, y=y_train, cv=fold, scoring="accuracy")
print(scores.mean())

param_grid = {
    'n_neighbors': list( range(1,21)),
    'metric': ['euclidean','manhattan']
}

grid_search = GridSearchCV(knn,param_grid,cv=fold)
grid_search.fit(X_train,y_train)
results = pd.DataFrame(grid_search.cv_results_)
#print(results)

best_model = grid_search.best_estimator_
#print(best_model)

print(grid_search.best_params_, "\n", grid_search.best_score_)

best_predict = best_model.predict(X_test)
#print(best_predict)
print(accuracy_score(y_test,best_predict))

best_predict_train = best_model.predict(X_train)
print(accuracy_score(y_train,best_predict_train))

cm_train = confusion_matrix(y_train, best_predict_train)
print(cm_train)

cm_test = confusion_matrix(y_test, best_predict)
print(cm_test)

report = classification_report(y_train,best_predict_train)
print(report)