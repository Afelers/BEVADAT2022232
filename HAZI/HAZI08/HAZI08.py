# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error
from typing import Tuple
import sklearn

# %%
'''
Készíts egy függvényt, betölti majd vissza adja az iris adathalmazt.


Egy példa a kimenetre: iris
return type: sklearn.utils.Bunch
függvény neve: load_iris_data
'''

# %%
# 1
def load_iris_data() -> sklearn.utils.Bunch:
    return load_iris()

# %%
'''
Készíts egy függvényt, ami a betölti az virágokhoz tartozó levél méreteket egy dataframebe, majd az első 5 sort visszaadja.
Minden oszlop tartalmazza, hogy az milyen mérethez tartozik.

Egy példa a bemenetre: iris
Egy példa a kimenetre: iris_df
return type: pandas.core.frame.DataFrame
függvény neve: check_data
'''

# %%
# 2
def check_data(iris) -> pd.core.frame.DataFrame:
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    return df.head(5)

# %%
''' 
Készíts egy függvényt ami előkészíti az adatokat egy lineáris regressziós model feltanításához.
Featurejeink legyenek a levél méretek kivéve a "sepal length (cm)", ez legyen a targetünk.

Egy példa a bemenetre: iris
Egy példa a kimenetre: X, y
return type: (numpy.ndarray, numpy.ndarray)
függvény neve: linear_train_data
'''

# %%
# 3
def linear_train_data(iris) -> Tuple[np.ndarray, np.ndarray]:
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    return (df[["sepal width (cm)", "petal length (cm)", "petal width (cm)"]].values, df["sepal length (cm)"].values)

# %%
''' 
Készíts egy függvényt ami előkészíti az adatokat egy logisztikus regressziós model feltanításához.
Featurejeink legyenek a levél méretek, targetünk pedig a 0, 1-es virág osztályok.
Fontos csak azokkal az adatokkal tanítsunk amihez tartozik adott target. 

Egy példa a bemenetre: iris
Egy példa a kimenetre: X, y
return type: (numpy.ndarray, numpy.ndarray)
függvény neve: logistic_train_data
'''

# %%
# 4
def logistic_train_data(iris) -> Tuple[np.ndarray, np.ndarray]:
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df["target"] = iris.target
    idxs = df.index[df["target"] < 2].tolist()
    return (df.iloc[idxs, : -1].values, df.iloc[idxs, -1].values)

# %%
'''
Készíts egy függvényt ami feldarabolja az adatainkat train és test részre. Az adatok 20%-át használjuk fel a teszteléshez.
Tegyük determenisztikussá a darabolást, ennek értéke legyen 42.

Egy példa a bemenetre: X, y
Egy példa a kimenetre: X_train, X_test, y_train, y_test
return type: (numpy.ndarray, numpy.ndarray, numpy.ndarray, numpy.ndarray)
függvény neve: split_data
'''

# %%
# 5
def split_data(X : np.ndarray , y : np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return (X_train, X_test, y_train, y_test)

# %%
'''
Készíts egy függvényt ami feltanít egy lineáris regressziós modelt, majd visszatér vele.

Egy példa a bemenetre: X_train, y_train
Egy példa a kimenetre: model
return type: sklearn.linear_model._base.LinearRegression
függvény neve: train_linear_regression
'''

# %%
# 6
def train_linear_regression(X_train, y_train) -> sklearn.linear_model.LinearRegression:
    return LinearRegression().fit(X_train, y_train)

# %%
'''
Készíts egy függvényt ami feltanít egy logisztikus regressziós modelt, majd visszatér vele.

Egy példa a bemenetre: X_train, y_train
Egy példa a kimenetre: model
return type: sklearn.linear_model._base.LogisticRegression
függvény neve: train_logistic_regression
'''

# %%
# 7
def train_logistic_regression(X_train, y_train) -> sklearn.linear_model.LogisticRegression:
    return LogisticRegression().fit(X_train, y_train)

# %%
''' 
Készíts egy függvényt, ami a feltanított modellel predikciót tud végre hajtani.

Egy példa a bemenetre: model, X_test
Egy példa a kimenetre: y_pred
return type: numpy.ndarray
függvény neve: predict
'''

# %%
# 8
def predict(model, X_test) -> np.ndarray:
    return model.predict(X_test)

# %%
'''
Készíts egy függvényt, ami vizualizálni tudja a label és a predikciók közötti eltérést.
Használj scatter plotot a diagram elkészítéséhez.

Diagram címe legyen: 'Actual vs Predicted Target Values'
Az x tengely címe legyen: 'Actual'
Az y tengely címe legyen: 'Predicted'

Egy példa a bemenetre: y_test, y_pred
Egy példa a kimenetre: scatter plot
return type: matplotlib.figure.Figure
függvény neve: plot_actual_vs_predicted
'''

# %%
# 9
def plot_actual_vs_predicted(y_test, y_pred):
    fig, ax = plt.subplots()
    ax.set_title('Actual vs Predicted Target Values')
    ax.set_xlabel('Actual')
    ax.set_ylabel('Predicted')
    ax.scatter(y_test, y_pred)
    return fig

#X, y = linear_train_data(load_iris())
#X_train, X_test, y_train, y_test = split_data(X, y)
#model = train_linear_regression(X_train, y_train)
#y_pred = predict(model, X_test)
#plot_actual_vs_predicted(y_test, y_pred)

# %%
''' 
Készíts egy függvényt, ami a Négyzetes hiba (MSE) értékét számolja ki a predikciók és a valós értékek között.

Egy példa a bemenetre: y_test, y_pred
Egy példa a kimenetre: mse
return type: float
függvény neve: evaluate_model
'''

# %%
# 10
def evaluate_model(y_test, y_pred) -> float:
    return np.mean((y_pred - y_test)**2)


