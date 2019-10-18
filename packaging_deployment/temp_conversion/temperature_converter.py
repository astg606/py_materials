#!/usr/bin/env python

"""
  Python Program to convert temperature from unit to another
"""

import converter_functions

#---------------------------
# From Celcius to Fahrenheit
#---------------------------
temperatureC = 37.5
temperatureF = converter_functions.from_celcius_to_fahrenheit(temperatureC)
print('{:0.1f} degree Celsius is equal to {:0.1f} degree Fahrenheit'
      .format(temperatureC, temperatureF))

#---------------------------
# From Fahrenheit to Celcius
#---------------------------

temperatureF = 67.8
temperatureC = converter_functions.from_fahrenheit_to_celcius(temperatureF)
print('{:0.1f} degree Fahrenheit is equal to {:0.1f} degree Celcius'
      .format(temperatureF, temperatureC))

#---------------------------
# From Fahrenheit to Kelvin
#---------------------------

temperatureK = converter_functions.from_fahrenheit_to_kelvin(temperatureF)
print('{:0.1f} degree Fahrenheit is equal to {:0.1f} degree Kelvin'
      .format(temperatureF, temperatureK))
