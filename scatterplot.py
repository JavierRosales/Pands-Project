# David Markham
# Fisher Iris Data set

# Use a Multivariate scatter-plot to distinguish the relationship between the flowers.


# Import Libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
from pandas.plotting import scatter_matrix


# Load dataset
data = ("iris.csv")
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'species']
dataset = pd.read_csv(data, header = 0)


scatter_matrix(dataset)
plt.show()