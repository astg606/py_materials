#!/usr/bin/env python

import def_converter

# Python Program to convert temperature

# Calculate Fahrenheit
cel = 37.5
fahr = def_converter.from_C_to_F(cel)
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(cel,fahr))

# Calculate Celcius
fahr = 67.8
cel = def_converter.from_F_to_C(fahr)
print('%0.1f degree Fahrenheit is equal to %0.1f degree Celcius' %(fahr,cel))

kel = def_converter.from_F_to_K(fahr)
print('%0.1f degree Fahrenheit is equal to %0.1f degree Kelvin' %(fahr,kel))
