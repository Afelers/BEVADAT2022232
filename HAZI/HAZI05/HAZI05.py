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