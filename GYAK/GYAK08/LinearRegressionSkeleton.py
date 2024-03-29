import numpy as np
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt


class LinearRegression:
    def __init__(self, epochs: int = 1000, lr: float = 1e-3):
        self.epochs = epochs
        self.lr = lr

    def fit(self, X: np.array, y: np.array):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.m = 0
        self.c = 0

        self.n = float(len(self.X_train)) # Number of elements in X

        # Performing Gradient Descent 
        losses = []
        for i in range(self.epochs): 
            y_pred = self.m*self.X_train + self.c  # The current predicted value of Y

            residuals = y_pred - self.y_train
            loss = np.sum(residuals ** 2)
            losses.append(loss)
            D_m = (-2/self.n) * sum(self.X_train * residuals)  # Derivative wrt m
            D_c = (-2/self.n) * sum(residuals)  # Derivative wrt c
            self.m = self.m + self.lr * D_m  # Update m
            self.c = self.c + self.lr * D_c  # Update c
            if i % 100 == 0:
                print(np.mean(self.y_train-y_pred))
            
    def predict(self, X):
        pred = []
        for X in self.X_test:
            self.y_pred = self.m*X + self.c
            pred.append(self.y_pred)
        print(pred)
        print(self.y_test)
        self.y_pred = self.m*self.X_test + self.c
        plt.scatter(self.X_test, self.y_test)
        plt.plot([min(self.X_test), max(self.X_test)], [min(self.y_pred), max(self.y_pred)], color='red') # predicted
        plt.show()