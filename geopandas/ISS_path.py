# https://medium.com/@katehayes.m51/tracking-the-international-space-station-a-mini-project-with-geopandas-e682e8a3489f

import numpy as np
import pandas as pd
from shapely.geometry import Point
import matplotlib.pyplot as plt
import requests
import time


# Create a loop to get the ISS info over 10 minutes every 5 seconds
#------------------------------------------------------------------
max_count = 3000 # 2160
ISS_loc = list()
count = 0
while count <= max_count:    
    
# Reachout to the ISS API
    response = requests.get("http://api.open-notify.org/iss-now.json")
    status = response.status_code
    
    # Check status code for an appropriate response fromt the API
    if status != 200:
        print(f'Error improper response code. Code is {status}')
        break
    else:
        
    # Turn the API response into JSON
        resp = response.json()
        # append each API response to the list of ISS locations
        ISS_loc.append(resp)
        # pause the loop for 5 seconds to allow the ISS to move slightly
        time.sleep(5)
        # Add to the count so it doesn't access the API too many times
        print(count)
        count = count + 1


# Initialize empy dictionary (will become the ISS dataframe)
ISS_dict={'latitude': None, 'longitude': None, 'timestamp': None}

# Initialize empty lists to populate with values from the API
lat_list = list()
long_list = list()
time_list = list()

# Loop through the API list and extract latitude, longitude, and timestamp
for i in range(0,len(ISS_loc)):
    lat_list.append(ISS_loc[i]['iss_position']['latitude'])
    long_list.append(ISS_loc[i]['iss_position']['longitude'])
    time_list.append(ISS_loc[i]['timestamp'])

# Populate ISS dictionary
ISS_dict['latitude'] = lat_list
ISS_dict['longitude'] = long_list
ISS_dict['timestamp'] = time_list

# Turn the ISS position dictionary into a data frame 
ISS_df = pd.DataFrame.from_dict(ISS_dict)

# Change values to integers from strings
ISS_df['latitude'] = ISS_df['latitude'].astype(float)
ISS_df['longitude'] = ISS_df['longitude'].astype(float)
ISS_df['timestamp'] = ISS_df['timestamp'].astype(float)

# Make a coordinates column that has a value of a list of longitude and latitude
ISS_df['geometry'] = ISS_df[['longitude', 'latitude']].values.tolist()

# Make the coordinate column a Point object
ISS_df['geometry'] = ISS_df['geometry'].apply(Point)

# Save in a cvs file
ISS_df.to_csv("ISS_timeseries_path.csv", sep=',', index=False)
#ISS_df.to_csv("ISS_timeseries_path.csv", sep='\t', encoding='utf-8', index=False)
