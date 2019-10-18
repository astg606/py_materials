#!/usr/bin/env python
 
import subprocess
import os
 
def find():
 
    y = input("Enter a text you want to search on the system!")
 
    s = y.rstrip("\n")
 
    print("string", s)
 
    find = subprocess.Popen([r"/usr/bin/find", "/", "-name", y, "-print"], stdout=subprocess.PIPE)
 
    for line in find.stdout.readlines():
        print("line", line)
        l = line.rstrip("\n")
        list = subprocess.Popen([r"ls", "-l", l], stdout=subprocess.PIPE)
        list_stdout = list.communicate()[0]
        print(list_stdout)
 
    file = subprocess.Popen([r"file", l], stdout=subprocess.PIPE)
 
    file_stdout = file.communicate()[0]
 
    print(file_stdout)
 
def main():
    find()
 
main()
