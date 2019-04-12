# David Markham 
# Fisher Iris Data Set-April 2019
# Display the Iris data using a Histogram 

# Import Libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt




# Load dataset
data = ("iris.csv")
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'species']
dataset = pd.read_csv(data, header = 0)


# Displays a Histogram.
dataset.hist()
plt.show()