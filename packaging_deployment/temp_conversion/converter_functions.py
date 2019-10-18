#!/usr/bin/env python
"""
Functions for temperature conversion:
   - from_celcius_to_fahrenheit
   - from_celcius_to_fahrenheit
   - from_fahrenheit_to_celcius
   - from_celcius_to_kelvin
   - from_kelvin_to_fahrenheit
"""

zeroCelcius = 273.5  # zero degree Celcius in Kelvin

def from_celcius_to_fahrenheit(temperatureC):
    """
    Convert the temperature from
    Celcius to Fahrenheit
    """
    return (temperatureC * 1.8) + 32

def from_fahrenheit_to_celcius(temperatureF):
    """
    Convert the temperature from
    Fahrenheit to Celcius
    """
    return (temperatureF - 32) * 5.0 / 9.0

def from_celcius_to_kelvin(temperatureC):
    """
    Convert the temperature from
    Celcius to Kelvin
    """
    return temperatureC + zeroCelcius

def from_kelvin_to_fahrenheit(temperatureK):
    """
    Convert the temperature from
    Kelvin to Fahrenheit
    """
    temperatureC = temperatureK - zeroCelcius
    return from_celcius_to_fahrenheit(temperatureC)

def from_fahrenheit_to_kelvin(temperatureF):
    """
    Convert the temperature from
    Fahrenheit to Kelvin
    """
    return from_fahrenheit_to_celcius(temperatureF) + zeroCelcius
