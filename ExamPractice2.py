# -*- coding: utf-8 -*-
"""
Created on Sun May 20 11:02:30 2018

@author: Kaustav Chatterjee
"""

#Import
from ExamPractice import Restaurant
my_new_restaurant=Restaurant('Magnolia','Indian')
my_new_restaurant.describe_restaurant()

from ExamPractice import PeterCat
my_new_restaurant=PeterCat('A1 Haji','Rolls')
my_new_restaurant.describe_restaurant()

from collections import OrderedDict
favorite_languages=OrderedDict()

favorite_languages['jen']='Python'
favorite_languages['men']='R'
favorite_languages['ken']='C'
favorite_languages['len']='Java'

for key,value in favorite_languages.items():
    print(key.title()+" "+value.title())