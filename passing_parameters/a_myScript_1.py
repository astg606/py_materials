#!/usr/bin/env python

# Load the module
#----------------
import argparse

# Instantiate the OptionParser class
#-----------------------------------
#aparser = argparse.ArgumentParser(version='%(prog)s version 0.0',
aparser = argparse.ArgumentParser(description='How to use the script: %(prog)s')

# Add the options
#----------------
aparser.add_argument('--version', action='version', version='%(prog)s 0.0') 

aparser.add_argument('-x', '--exec', help='Execution file',
                  dest='myExecFile', action='store', metavar='executionFile')

aparser.add_argument('-i', '--input', help='Input file',
                  dest='myInputFile', action='store',
                  type=argparse.FileType('rt'), metavar='inputFile')

aparser.add_argument('-o', '--output', help='Output file',
                  dest='myOutputFile', action='store', default='ouput.txt',
                  type=argparse.FileType('wt'), metavar='outputFile')

aparser.add_argument('-p', '--param', help='Input parameter',
                  dest='myParameter', action='store', type=float,
                  default=1.0, metavar='inputParameter')

# Parse the command line
#-----------------------
aargs = aparser.parse_args()
#print aparser.parse_args()

