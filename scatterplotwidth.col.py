# David Markham
# Fisher Iris Data set

# Use a colour Scatterplot to determine relationship between species.
# Sepal width versus petal width.

# Import Libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import seaborn as sns
from sklearn import datasets



# Load data
iris = datasets.load_iris()
iris_df = pd.DataFrame(iris['data'], columns=iris['feature_names'])
iris_df['species'] = iris['target']

colours = ['red', 'green', 'blue']
species = ['I. setosa', 'I. versicolor', 'I. virginica']

# Specify the species colours 
for i in range(0, 3):    
    species_df = iris_df[iris_df['species'] == i]    
    plt.scatter(        
        species_df['sepal width (cm)'],        
        species_df['petal width (cm)'],
        color=colours[i],        
        alpha=0.5,        
        label=species[i]   
    )
# Label the X and Y axis
# Legend will display the species colours on the graph location (center right)
plt.xlabel('Sepal width (cm)')
plt.ylabel('Petal width (cm)')
plt.title('Iris dataset: Petal width vs Sepal width')
plt.legend(loc='center right')

plt.show()