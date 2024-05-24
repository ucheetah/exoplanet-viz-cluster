## Visualization and Clustering with NASA Exoplanet Data

This project grabs from the [**NASA exoplanets archive**](https://exoplanetarchive.ipac.caltech.edu/index.html), a collaboration between Caltech and NASA under its Exoplanet Exploration Program. I'm drawing from the **`Planetary Systems`** dataset, which provides in-depth data on every confirmed exoplanet known to astronomists to date. The table contains one row per planet per reference and collects data such as its radius and mass, distance, stellar systems.

<ul>
  <li>Languages and packages: one humble SQL query, Python (Pandas, Matplotlib, Seaborn, Scikit-learn)</li>
  <li>Techniques: Data querying, data cleaning, missing value detection, outlier handling, visualization, machine learning (clustering)</li>
</ul>

I have a few goals associated with this project:
<ol>
  <li>Query and collect current data from NASA exoplanet archive's API;</li>
  <li>Perform exploratory data analysis on select exoplanet features and visualize them for analysis using `matplotlib` and `seeaborn`;</li>
  <li>Employ a clustering algorithm on the exoplanets using `scikit-learn` in hopes of generating groups that resemble existing exoplanet classifications (gas giants, terrestrials);</li>
  <li>Explore planet habitability using accepted astronomical science, such as stellar luminosity and star-planet distance.</li>
</ol>

<p align="center">
  <img src="https://github.com/ucheetah/exoplanet-viz-cluster/blob/main/nasa_exoplanet_homepage.png" width = "550" height = "400" alt="NASA Homepage" style="border: 2px solid black; border-radius: 5px;">
</p>
