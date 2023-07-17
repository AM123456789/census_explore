import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
from census import Census
from us import states
import os


c = Census("6f46a7532e0317f2318ad51b2aa17a2643edcc72")
va_census = c.acs5.state_county_tract(fields = ('NAME', 'C17002_001E', 'C17002_002E', 'C17002_003E', 'B01003_001E'),
                                      state_fips = states.VA.fips,
                                      county_fips = "*",
                                      tract = "*",
                                      year = 2017)
va_df = pd.DataFrame(va_census)
print(va_df.head(2))
print('Shape: ', va_df.shape)
va_tract = gpd.read_file("https://www2.census.gov/geo/tiger/TIGER2019/TRACT/tl_2019_51_tract.zip")
va_tract = va_tract.to_crs(epsg = 32617)
print(va_tract.head(2))
print('Shape: ', va_tract.shape)
print("\nThe shapefile projection is: {}".format(va_tract.crs))
va_df["GEOID"] = va_df["state"] + va_df["county"] + va_df["tract"]
va_df.head(2)
va_df = va_df.drop(columns = ["state", "county", "tract"])
va_df.head(2)
print("Column data types for census data:\n{}".format(va_df.dtypes))
print("\nColumn data types for census shapefile:\n{}".format(va_tract.dtypes))
va_merge = va_tract.merge(va_df, on = "GEOID")
print(va_merge.head(2))
print('Shape: ', va_merge.shape)
va_poverty_tract = va_merge[["STATEFP", "COUNTYFP", "TRACTCE", "GEOID", "geometry", "C17002_001E", "C17002_002E", "C17002_003E", "B01003_001E"]]
print(va_poverty_tract.head(2))
print('Shape: ', va_poverty_tract.shape)
va_poverty_county = va_poverty_tract.dissolve(by = 'COUNTYFP', aggfunc = 'sum')
print(va_poverty_county.head(2))
print('Shape: ', va_poverty_county.shape)
va_poverty_county["Poverty_Rate"] = (va_poverty_county["C17002_002E"] + va_poverty_county["C17002_003E"]) / va_poverty_county["B01003_001E"] * 100
va_poverty_county.head(2)
fig, ax = plt.subplots(1, 1, figsize = (20, 10))
va_poverty_county.plot(column = "Poverty_Rate",
                       ax = ax,
                       cmap = "RdPu",
                       legend = True)
ax.set_title('Poverty Rates (%) in Virginia', fontdict = {'fontsize': '25', 'fontweight' : '3'})
