import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from scipy.stats import mode
from sklearn.metrics import confusion_matrix
from sklearn.datasets import load_digits
import sklearn
import pandas as pd
from typing import Tuple

class KMeansOnDigits:

    def __init__(self, n_clusters, random_state) -> None:
        self.n_clusters = n_clusters
        self.random_state = random_state

    def load_dataset(self):
        self.digits = load_digits()
    
    def predict(self):
        model = KMeans(n_clusters=self.n_clusters, random_state=self.random_state)
        self.clusters = model.fit_predict(self.digits.data)
    
    def get_labels(self):
        result_array = np.zeros(self.clusters.shape)
        for c in self.clusters:
            mask = self.clusters == c
            modes = mode(self.digits.target[mask], keepdims=False).mode
            result_array[mask] = modes
        self.labels = result_array

    def calc_accuracy(self):
        self.accuracy = round(accuracy_score(self.digits.target, self.labels), 2)

    def confusion_matrix(self):
        self.mat = confusion_matrix(self.digits.target, self.labels)