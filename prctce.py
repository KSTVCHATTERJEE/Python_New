# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 10:30:32 2018

@author: KAUSTAV
"""

message = 'One of Python\'s strengths is its diverse community.'
print(message)

3 ** 2

age=23
message = "Happy" + " " + str(age) + "rd birthday"
print(message)

motorcycles = ['honda','yamaha','suzuki']
motorcycles

motorcycles.insert(0,'ducati')

popped_motor = motorcycles.pop()
popped_motor
motorcycles

first_owned=motorcycles.pop(0) #Not to be used this way
first_owned

motorcycles

cars = ['bmw','audi','toyota','subaru']
sorted(cars)

print(cars[4])

magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    
for value in range(1,5):
    print(value)
    
even_numbers = list(range(2,11,2))
print(even_numbers)

squares = [value **2 for value in range(1,11)]
print(squares)

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        
        
        
    
