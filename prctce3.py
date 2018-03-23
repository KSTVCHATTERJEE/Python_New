# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 10:13:01 2018

@author: KAUSTAV
"""

str_numbers=str(input("Enter the numbers separated by, :: "))
numbers = [int(x) for x in str_numbers.split(",")]

i=max(numbers)
while i>=1:
    j=0
    while j<len(numbers):
        if numbers[j]-i>=0:
            print(' * ',end='')
        else:
            print('   ',end='')
        j+=1
    i-=1
    print("\n")
    
    
input=int(input("Enter a number"))
for i in range(1,input):
    