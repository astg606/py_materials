# Manipulating Satellite Data

In this course series, we use Python tools to read NASA and NOAA related satellite data files,
process the data and perform basic visualizations.
We limit the scope of our analysis to datasets with netCDF, HDF4 and HDF5
file formats. 

In the satellite data files we will be working with, the latitude/longitude
information of the covered areas, might not be readily available.
We need to understand the metadata of each file and write code
segments to extract appropriate information and data from the file.
The goal of this course series is to provide the necessary Python skills
to confidently access satellite datasets.
We will be able to read observations from files
(using pyhdf, h5py, Xarray), extract latitude/longitude information,
and use them to create Xarray DataSets.
The Xarray objects will then be utilized to facilitate the manilipulations of observations.
In particular, we will visualize the data on maps to create static and interactive plots.
Wherever possible, we will compare observations with model outputs.

The following topics are covered:

- Jan 31: Numpy
- Feb 07: Visualization with Matplotlib and Cartopy
- Feb 14: Reading Scientific Data Format Files (netCDF4, pyhdf, h5py)
- Feb 21: Xarray: Creating Xarray DataSets using Numpy Arrays
- Feb 28: Using netCDF4 and Xarray to Manipulate AOD and VIIRS Data
- Mar 07: Using pyhdf and Xarray to Manipulate MODIS and Landsat Data
- Mar 14: Using h5py and Xarray to Manipuate OMI Data

### Useful Pointers:

- [Examples of accessing NASA HDF/HDF-EOS files using Python](http://hdfeos.org/zoo/index_openPODAAC_Examples.php#MODIS)
- [Satellite Imagery Analysis in Python Part I: GOES-16 Data, netCDF Files, and The Basemap Toolkit](https://makersportal.com/blog/2019/7/8/satellite-imagery-analysis-in-python-part-i-goes-16-data-netcdf-files-and-the-basemap-toolkit)
- [STAR Atmospheric Composition Product Training](https://www.star.nesdis.noaa.gov/atmospheric-composition-training/)
- [Visualizing Global Land Temperatures in Python with scrapy, xarray, and cartopy](https://cbrownley.wordpress.com/category/python/)
- [How to work with satellite data in Python](https://coastwatch.gitbook.io/satellite-course/tutorials/python-tutorial/1.-how-to-work-with-satellite-data-in-python)



