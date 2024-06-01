# Exoplanet functions

def plot_palette(list):
    """Return visualization of palette with list of desired colors
    """
    fig, ax = plt.subplots(figsize=(6, 2), dpi=150)
    for idx, color in enumerate(list):
        ax.add_patch(plt.Rectangle((idx, 0), 1, 1, color=color))
        ax.text(idx + 0.5, -0.1, list[idx], ha='center', va='top', fontsize=10)
    ax.set_xlim(0, len(list))
    ax.set_ylim(0, 1)
    ax.set_xticks(range(len(list)))
    ax.set_xticklabels([])
    ax.set_yticks([])
    plt.show()

def load_data(nasa_url, local_path):
    """Load data taking in the TAP protocol URL for NASA and the local path
    """
    request_csv = requests.get(url)
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

def clean_data(data):
    """Perform listwise deletion and drop duplicate rows
    """
    data_cleaned = data.dropna()
    data_cleaned = data_cleaned.drop_duplicates(subset='planet_name')
    return data_cleaned

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

def return_describe_table(exoplanet_data_raw):
    """Return description table for raw data
    """
    exo_describe = exoplanet_data_raw.describe()
    exo_describe = exo_describe.T
    exo_describe = exo_describe.round(0).astype(int)
    return exo_describe