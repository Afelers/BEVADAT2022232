import pandas as pd
from typing import Tuple
from scipy.stats import mode
from sklearn.metrics import confusion_matrix
import seaborn as sns

class KNNClassifier:
    
    def __init__(self, k:int, test_split_ratio:float):
        self.k = k
        self.test_split_ratio = test_split_ratio

    @property
    def k_neighbors(self):
        return self.k
    
    @staticmethod
    def load_csv(csv_path : str):
        df = pd.read_csv(csv_path)
        new_df = df.sample(frac=1, random_state=42)
        x, y = new_df.iloc[:, : -1], new_df.iloc[:, -1]
        return (x, y)
    
    def train_test_split(self, features : pd.core.frame.DataFrame,
                        labels : pd.core.series.Series):
        test_size = int(len(features) * self.test_split_ratio)
        train_size = len(features) - test_size
        assert len(features) == test_size + train_size, "Size mismatch!"    # False kiértékelésre AssertionErrort dob a megadott üzenettel
        self.x_train, self.y_train = features.iloc[: train_size, :], labels.iloc[: train_size]
        self.x_test, self.y_test = features.iloc[train_size :, :], labels.iloc[train_size :]
        self.y_train.reset_index(inplace=True, drop=True)
        self.y_test.reset_index(inplace=True, drop=True)
    
    def euclidean(self, element_of_x : pd.core.series.Series) -> pd.core.series.Series:
        return ((self.x_train - element_of_x) ** 2).sum(axis=1).pow(1/2)
    
    def predict(self, x_test : pd.core.frame.DataFrame):
        labels_pred = []
        for i in range(len(x_test)):
            distances = self.euclidean(x_test.iloc[i])
            distances = pd.DataFrame(sorted(zip(distances, self.y_train)))
            label_pred = mode(distances.iloc[:self.k, 1], keepdims=False).mode
            labels_pred.append(label_pred)
        self.y_preds = pd.Series(labels_pred)
    
    def accuracy(self) -> float:
        true_positive = (self.y_test == self.y_preds).sum()
        return true_positive / len(self.y_test) * 100
    
    def confusion_matrix(self):
        return confusion_matrix(self.y_test, self.y_preds)
    
    def best_k(self) -> Tuple[int, float]:
        accuracies = []
        for i in range(1, 21):
            self.k = i
            self.predict(self.x_test)
            accuracies.append(self.accuracy())
        return (accuracies.index(max(accuracies)) + 1, round(max(accuracies), 2))