# David Markham 2019-04-01
# Fisher Iris Data Set 

# Display the mean, min and max of each column along with some percentiles.

# First Import the libaries we will need for examining this data set.
# Found a site which goes into great detail to help users new to programming.
# https://machinelearningmastery.com/machine-learning-in-python-step-by-step/ 

# Import all the required libraries.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt




# Load dataset
data = ("iris.csv")
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'species']
dataset = pd.read_csv(data, header=0) 


# This will print the mean, min, max and more data.
print(dataset.describe())
