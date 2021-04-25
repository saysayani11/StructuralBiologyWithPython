# Read More: https://jakevdp.github.io/PythonDataScienceHandbook/05.09-principal-component-analysis.html
# Principal component analysis is a fast and flexible unsupervised method for dimensionality reduction in data
import pandas as pd
import numpy as np
from pandas import DataFrame
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

# The dataset used is of size (270 X 19) and comprises the relative C-alpha backbone distances of different PDB structures of the human CK2 protein to a reference CK2 protein
# Load the prepared dataset; 
# Use <df>.shape to obtain the shape of the dataset
dist_data = pd.read_csv(r"C:\Users\saySa\OneDrive\Desktop\RMSD_data.csv")

# Use PCA to project data to a more manageable number of dimensions, say two
# Set the number of Principal Components
pca = PCA(2)  
projected = pca.fit_transform(dist_data)

# Check the projected data's dimensions, reduced to the specified number of components
# print(dist_data.shape)
# print(projected.shape)
# original shape:    (270,19)
# transformed shape: (200,2)

# Select a "target" column from the original dataset
y = dist_data['3bqc (30-300)']

# We can now plot the first two principal components of each point to learn about the data
plt.scatter(projected[:, 0], projected[:, 1],  c=y, edgecolor='none', alpha=0.7,cmap=plt.cm.get_cmap('nipy_spectral', 10))
plt.xlabel('Component 1')
plt.ylabel('Component 2')
plt.colorbar();
