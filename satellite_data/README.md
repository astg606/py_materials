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
to confidently access satellite datasets, and to present sample workflows on how to
read and manipulate data from the files.
We will be able to read observations from files
(using pyhdf, h5py, Xarray), extract latitude/longitude information,
and use them to create Xarray DataSets.
The Xarray objects will then be utilized to facilitate the manilipulations of observations.
In particular, we will visualize the data on maps to create static and interactive plots.
Wherever possible, we will compare observations with model outputs.

The following topics are covered:

- Jan 31: Numpy

NumPy (Numerical Python) is a library consisting of multidimensional array objects and a 
collection of routines for processing those arrays. 
It is meant to provide an array object that is at least an order of magnitude faster than 
traditional Python lists. 
Using NumPy, mathematical and logical operations on arrays can be efficiently performed. 
NumPy is the foundation of an extensive ecosystem of Python products and Data Sciencelibraries
such as SciPy, Pandas, Scikit-Learn, Matplolib, Seaborn, etc.
This course introduces the structure of Numpy arrays, show various ways to create them 
to facilitate numerical calculations. We will also present how to perform array slicing, 
in-place arithmetic, etc. and how to use built-in mathematical functions for faster computations.

- Feb 07: Visualization with Matplotlib and Cartopy

Matplotlib is one of the most popular Python packages used for data visualization. 
It is a cross-platform library for making 2D plots from data in arrays. 
It can be used in python scripts, shell, web application servers and other 
graphical user interface toolkits. 
Cartopy is a Python package designed for geospatial data processing to produce 
maps and other geospatial data analyses.
In this course, we will present the anatomy of a Matplotlib figure and show how to 
produce various plots with Matplotlib.
We will also use the Matplotlib object oriented formulation (figure and axes)
to visualize geospatial data.

- Feb 14: Reading Scientific Data Format Files (netCDF4, pyhdf, h5py)

In this course, we will learn how to read netCDF, HDF4 and HDF5 files
using Python.

- Feb 21: Xarray: Creating Xarray DataSets using Numpy Arrays

Xarray is an open-source library providing high-level, easy-to-use data structures 
and analysis tools for working with multidimensional labeled datasets and arrays in Python. 
Xarray combines the convenience of labeled data structures inspired by Pandas 
with the multi-dimensional arrays of NumPy and parallel out-of-core computation from Dask 
to provide an intuitive, powerful and scalable platform for scientific analysis. 
Xarray introduces labels in the form of dimensions, coordinates and attributes on top of 
raw Numpy-like arrays. It is particularly tailored to working with netCDF files.
In this course, we will learn to create Xarray DataArrays and Xarray DataSets
using Numpy arrays.
We will also combine Xarray and Hvplot to produce interactive and live plots.


- Feb 28: Using netCDF4 and Xarray to Manipulate AOD and VIIRS Data


- Mar 07: Using Python to Access MODIS and Landsat Data Files

We use pyhdf to access MODIS and Landsat data files.
We create various workflows to extract data from the files, 
and create Xarray objects that are used for data manipulation and visualization.

- Mar 14: Using h5py and Xarray to Access OMI Data File

We use h5py to access Ozone Monitoring Instrument (OMI) data files.
We create a workflow to extract all the datasets from the files, 
and create Xarray objects that are used for data manipulation and visualization.


### Useful Pointers:

- [Examples of accessing NASA HDF/HDF-EOS files using Python](https://hdfeos.org/zoo/index_openLaRC_Examples.php)
- [Satellite Imagery Analysis in Python Part I: GOES-16 Data, netCDF Files, and The Basemap Toolkit](https://makersportal.com/blog/2019/7/8/satellite-imagery-analysis-in-python-part-i-goes-16-data-netcdf-files-and-the-basemap-toolkit)
- [STAR Atmospheric Composition Product Training](https://www.star.nesdis.noaa.gov/atmospheric-composition-training/)
- [Visualizing Global Land Temperatures in Python with scrapy, xarray, and cartopy](https://cbrownley.wordpress.com/category/python/)
- [How to work with satellite data in Python](https://coastwatch.gitbook.io/satellite-course/tutorials/python-tutorial/1.-how-to-work-with-satellite-data-in-python)



