# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 22:39:50 2018

@author: acer
"""

########################      PYTHON 2 SESSION ASSIGNMENT 2   ############################
#   Date   : 14-12-2018
#   Author : Mitesh Chandra    
##########################################################################################
# 1. Write a program which accepts a sequence of comma-separated numbers from console and
#    generate a list.
##########################################################################################
values = input("Input some comma seprated numbers : ")
list = values.split(",")
print('List : ',list)

#
##########################################################################################
# 2. Create the below pattern using nested for loop in Python.

##########################################################################################
print("Program to print start pattern: \n");
rows = input("Enter max star to be display on single line")
rows = int (rows)
for i in range (0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")
for i in range (rows, 0, -1):
    for j in range(0, i -1):
        print("*", end=' ')
    print("\r")

##########################################################################################
# 3. Write a Python program to reverse a word after accepting the input from the user.
##########################################################################################
word = input("Input a word to reverse: ")

for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")

##########################################################################################
# 4. Write a Python Program to print the given string in the format specified in the sample
#    output.
# WE, THE PEOPLE OF INDIA, 
#    having solemnly resolved to constitute India into a SOVEREIGN,
#       SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC 
#            and to secure to all its citizens
##########################################################################################

print("WE, THE PEOPLE OF INDIA \n\thaving solemnly resolved to constitute India into a SOVEREIGN,\n\t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n\t\t\tand to secure to all its citizens \n")


    
    
    
