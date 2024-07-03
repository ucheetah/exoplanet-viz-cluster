# Exoplanet functions

# Imports
import pandas as pd
import numpy as np
import requests
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.patches as mpatches
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import exoplanet_functions
from exoplanet_functions import load_data, rename_columns, perform_kmeans, return_describe_table

def load_data(nasa_url, local_path):
    """Load data taking in the TAP protocol URL for NASA and the local path
    """
    request_csv = requests.get(nasa_url)
    with open(local_path, 'w') as f:
        f.write(request_csv.text)
    data = pd.read_csv(local_path)
    return data

def rename_columns(data, column_renames):
    """Rename columns and convert distance from parsec to light years
    """
    data = data.rename(columns=column_renames)
    data['distance_ly'] = data['distance_pc'] * 3.26
    data = data.drop(columns = 'distance_pc')
    return data

def perform_kmeans(exoplanet_data_processed, kmeans_columns, n_clusters, n_init):
    """Perform Kmeans on processed data for planet radius and mass specifying clusters and inits
    """
    scaler = StandardScaler()
    exoplanet_scaled =scaler.fit_transform(exoplanet_data_processed[kmeans_columns])
    kmeans = KMeans(n_clusters=n_clusters, n_init=n_init)
    kmeans.fit(exoplanet_scaled)
    clusters = kmeans.predict(exoplanet_scaled)
    centroids_scaled = kmeans.cluster_centers_
    centroids_original_scale = scaler.inverse_transform(centroids_scaled)
    return clusters, centroids_original_scale

def return_describe_table(exoplanet_data):
  exo_describe = exoplanet_data.describe()
  exo_describe_rounded = exo_describe.copy()
  if 'planet_radius' in exo_describe.columns:
    exo_describe_rounded['planet_radius'] = exo_describe['planet_radius'].round(1)
  if 'planet_mass' in exo_describe.columns:
    exo_describe_rounded['planet_mass'] = exo_describe['planet_mass'].round(1)
  for column in exo_describe.columns:
    if column not in ['planet_radius', 'planet_mass']:
      exo_describe_rounded[column] = exo_describe[column].round(0).astype(int)
  exo_describe_rounded = exo_describe_rounded.astype('str').T
  return exo_describe_rounded
