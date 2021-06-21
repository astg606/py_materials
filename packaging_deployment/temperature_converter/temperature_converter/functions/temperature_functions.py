#!/usr/bin/env python

"""
   Module containing utility functions for converting temperatures
   from one unit to another. It has the following functions:

      - convert_celcius_to_kelvin
      - convert_celcius_to_fahrenheit
      - convert_kelvin_to_celcius
      - convert_kelvin_to_fahrenheit
      - convert_fahrenheit_to_celcius
      - convert_fahrenheit_to_kelvin
"""

# Local modules
import constants

#--------------------------------------------------------------------------

def convert_celcius_to_kelvin(temperatureC):
    """
       Convert temperature from Celcius to Kelvin.
       
       Input Value:
          - temperatureC: float, temperature in degree Celcius
       Returned Value
          - float, temperature in degree Kelvin
    """
    return temperatureC + constants.zeroCelcius

#--------------------------------------------------------------------------

def convert_celcius_to_fahrenheit(temperatureC):
    """
       Convert temperature from Celcius to Fahrenheit.

       Input Value:
          - temperatureC: float, temperature in degree Celcius
       Returned Value
          - float, temperature in degree Fahrenheit
    """
    return (9.0/5.0)*temperatureC + 32.0

#--------------------------------------------------------------------------

def convert_kelvin_to_celcius(temperatureK):
    """
       Convert temperature from Kelvin to Celcius.
       
       Input Value:
          - temperatureC: float, temperature in degree Kelvin
       Returned Value
          - float, temperature in degree Celcius
    """
    return temperatureK - constants.zeroCelcius

#--------------------------------------------------------------------------

def convert_kelvin_to_fahrenheit(temperatureK):
    """
       Convert temperature from Kelvin to Fahrenheit.

       Input Value:
          - temperatureK: float, temperature in degree Kelvin
       Returned Value
          - float, temperature in degree Fahrenheit
    """
    return (9.0/5.0)*(temperatureK - constants.zeroCelcius) + 32.0

#--------------------------------------------------------------------------

def convert_fahrenheit_to_celcius(temperatureF):
    """
       Convert temperature from Fahrenheit to Celcius.

       Input Value:
          - temperatureF: float, temperature in degree Fahrenheit
       Returned Value
          - float, temperature in degree Celcius
    """
    return (9.0/5.0)*(temperatureF - 32.0)

#--------------------------------------------------------------------------

def convert_fahrenheit_to_kelvin(temperatureF):
    """
       Convert temperature from Fahrenheit to Kelvin

       Input Value:
          - temperatureF: float, temperature in degree Fahrenheit
       Returned Value
          - float, temperature in degree Kelvin
    """
    return (5.0/9.0)*(temperatureF - 32.0) +  constants.zeroCelcius


#--------------------------------------------------------------------------



if __name__ == '__main__':
   print (convert_celcius_to_kelvin(15.7))
   print (convert_kelvin_to_celcius(302.9))
