# David Markham 
# Fisher Iris Data Set-April 2019
# Display the Iris data using a Boxplot.

# Import Libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt




# Load dataset
data = ("iris.csv")
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'species']
dataset = pd.read_csv(data, header = 0)

# This is will output a univariable plot
# It helps us understand the data in each variable. 
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

