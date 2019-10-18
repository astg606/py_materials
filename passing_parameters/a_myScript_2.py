#!/usr/bin/env python

# Load the modules
#-----------------
import sys
import argparse

# Instantiate the OptionParser class
#-----------------------------------
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

aparser.add_argument('--optional', nargs='*', help='Optional arguments')

# Parse the command line
#-----------------------
aargs = aparser.parse_args()

ne = 0

# Make sure arguments are provided
#---------------------------------
if aargs.myExecFile is None:
   print "You need to provide the execution file"
   aparser.print_help()
   ne += 1
   sys.exit(ne)

if aargs.myInputFile is None:
   print "You need to provide an input file"
   aparser.print_help()
   ne += 1
   sys.exit(ne)

# Print all the options
#----------------------
print 'Execution file  :', aargs.myExecFile
print 'Input file      :', aargs.myInputFile
print 'Output file     :', aargs.myOutputFile
print 'Input parameter :', aargs.myParameter
print 'Other arguments :', aargs.optional
