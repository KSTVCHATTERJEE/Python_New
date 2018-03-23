# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 23:44:01 2018

@author: KAUSTAV
"""

C=input("Enter a string ")
C
N=eval(input("Enter number by which you want to shift "))
N
CSHIFT=""

for i in range(0, len(C)):
    a=C[i]
    o=ord(a)
    b=o+N
    c=chr(b)
    CSHIFT=CSHIFT+c
    
CSHIFT