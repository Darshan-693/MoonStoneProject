import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Load the CSV data
csv_path = "./moon_lat_long_smoothed_values.csv"  # Replace with your CSV file path
data = pd.read_csv(csv_path)

# Create a grid for latitude and longitude
latitudes = np.unique(data['Latitude'])
longitudes = np.unique(data['Longitude'])

# Reshape the values into a 2D grid for plotting
values = data['Value'].values.reshape(len(latitudes), len(longitudes))

# Map the data to an image (color mapping)
plt.figure(figsize=(10, 5))
plt.imshow(values, extent=[-180, 180, -90, 90], cmap='viridis', origin='lower')
plt.colorbar(label='Value')

# Save the overlay as a PNG image
output_image_path = "moon_overlay.png"
plt.axis('off')
plt.savefig(output_image_path, bbox_inches='tight', pad_inches=0, dpi=300)
plt.close()

# Confirm output
print(f"Overlay image saved to {output_image_path}")
