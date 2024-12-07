from astropy.table import Table
import pandas as pd

table_data = Table.read("./ch2_cla_l1_20240704T233844921_20240704T233850671.fits", hdu=1)
df = table_data.to_pandas()
print(df.head())

# Assuming 'latitude', 'longitude', and 'signal' columns are identified
df['normalized_signal'] = (df['COUNTS'] - df['COUNTS'].min()) / (df['COUNTS'].max() - df['COUNTS'].min())
print(df)
# Check the normalized data
#print(df[['latitude', 'longitude', 'normalized_signal']].head())
