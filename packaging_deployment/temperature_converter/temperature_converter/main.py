
import sys
import os
import yaml

#---------------------
# Import local modules
#---------------------
cur_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(cur_dir)
sys.path.append(cur_dir + os.sep + 'functions')
sys.path.append(cur_dir + os.sep + 'shared')
import temperature_functions

#print(sys.path)

# Obtain the YAML file name from the command line
#-------------------------------------------
file_name = sys.argv[1]

#------------------------------------------------
# Read the YAML file name
# Each section in the YAML file has:
#   - The type of conversion we want to do (key)
#   - A list of values we want to convert
#------------------------------------------------
with open(file_name, 'r') as yaml_file:
     yaml_content = yaml.load(yaml_file, yaml.Loader)

#--------------------------------------------
# Loop over all the sections on the YAML file
# to perform the temperature conversions.
#--------------------------------------------
for key, value in yaml_content.items():
    if key == 'KtoC':
        print("Kelvin to Celcius")
              #-----------------
        for val in value['vals']:
            var = temperature_functions.convert_kelvin_to_celcius(val)
            print("\t {:7.3f} degree K --> {:7.3f} degree C".format(val, var))

    if key == 'KtoF':
        print("Kelvin to Fahrenheit")
              #---------------------
        for val in value['vals']:
            var = temperature_functions.convert_kelvin_to_fahrenheit(val)
            print("\t {:7.3f} degree K --> {:7.3f} degree F".format(val, var))

    if key == 'CtoK':
        print("Celcius to Kelvin")
              #-----------------
        for val in value['vals']:
            var = temperature_functions.convert_celcius_to_kelvin(val)
            print("\t {:7.3f} degree C --> {:7.3f} degree K".format(val, var))

    if key == 'CtoF':
        print("Celcius to Fahrenheit")
              #----------------------
        for val in value['vals']:
            var = temperature_functions.convert_celcius_to_fahrenheit(val)
            print("\t {:7.3f} degree C --> {:7.3f} degree F".format(val, var))

    if key == 'FtoK':
        print("Fahrenheit to Kelvin")
              #-----------------
        for val in value['vals']:
            var = temperature_functions.convert_fahrenheit_to_kelvin(val)
            print("\t {:7.3f} degree F --> {:7.3f} degree K".format(val, var))

    if key == 'FtoC':
        print("Fahrenheit to Celcius")
              #----------------------
        for val in value['vals']:
            var = temperature_functions.convert_fahrenheit_to_celcius(val)
            print("\t {:7.3f} degree F --> {:7.3f} degree C".format(val, var))
