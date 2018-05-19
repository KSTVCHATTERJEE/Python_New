# -*- coding: utf-8 -*-
"""
Created on Sat May 19 10:48:16 2018

@author: Kaustav Chatterjee
"""

# Chapter 1 
name='ada lovelace'
print(name.title())
print(name.upper())
print(name.lower())
first_name='ada'
last_name='lovelace'
full_name=first_name+" "+last_name
print(full_name)
print("Hello" + " "+ full_name.title() + '!')

print("Python")
print("\tPython")
print("Languages:\n\tPython\n\tC\n\tJavascript")

favorite_language=" python "
favorite_language.rstrip()
favorite_language.lstrip()
favorite_language.strip()

age=22
message = "Happy " + str(age) + "nd birthday!"
print(message)

# Chapter 2
bicycles=['trek','cannondale','redline','specialized']
bicycles[0]

bicycles[0].title()

bicycles[1]
bicycles[3]

bicycles[-1]
motorcycles=['honda','yamaha','bajaj']

motorcycles[0]='ducati'

motorcycles.append('tvs')

motorcycles=[]

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

motorcycles.insert(0,'bajaj')

motorcycles

del motorcycles

popped_motorcycles=motorcycles.pop()
motorcycles

first_owned=motorcycles.pop(0)

print("My first bike was a " + " " + first_owned.title() + " " + ".")

motorcycles.remove('honda')


cars=['maruti','jaguar','mercedes','audi']
cars
cars.sort()
cars.sort(reverse=True)

sorted(cars)

cars.reverse()

len(cars)


#Chapter 3

for i in range(0,4):
    print(cars[i])   

for car in cars:
    print(car)
    
    
    
numbers=list(range(1,6))
numbers

even_numbers=list(range(2,11,2))
even_numbers


squares=[]
for i in range(1,11):
    squares.append(i**2)
    
    
squares
len(squares)
sorted(squares,reverse=True)
squares.reverse()    

min(squares)
max(squares)    
sum(squares)


cubes=[value**3 for value in range(1,11)]
cubes  

players=['virat','dhoni','rohit','shikhar','bumrah']
players[0:3]


  