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
motorcycles=['honda','yamaha','bajaj']

popped_motorcycles=motorcycles.pop()
motorcycles

first_owned=motorcycles.pop(0)

print("My first bike was a " + " " + first_owned.title() + " " + ".")

#motorcycles.remove('honda')

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

players[1:4]

players[:4]
players[2:]

players[-3:]

for player in players[:3]:
    print(player.title())

players2=players[:]

players.append('chahal')

dimensions=[200,50]

dimensions[0]=60 

dimensions=(200,50)
#dimensions[0]=60 


#Chapter 4
cars

for car in cars:
    if car == 'audi':
        print(car.upper())
    else:
        print(car.title())

car='Audi'
car.lower()=='audi'

topping='mushrooms'
if topping!='anchovies':
    print('Hold the anchovies')

age_0=18
age_1=21

age_0<=19 and age_1>=22

if 'abd' not in players:
    print("ABD rocks")    
    
if motorcycles:
    print("E baba")
else:
    print("OMG")
    
    
requested_toppings=['anchovies','olives','chicken sausages','paneer','capsicum']
available_toppings=['onions','chicken peri-peri','paneer','capsicum']


for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(requested_topping)
    else:
        print("Not available")
        
#Chapter 6
alien_0={'color':'green','points':'5'}       
alien_0
alien_0['color']


alien_0['x_position']=0
alien_0['y_position']=25
        
alien_0={}
alien_0['color']='green'
        
alien_0['color']='yellow'

#del alien_0['points']


for key,value in alien_0.items():
    print(key + " " +value)
    

for key in alien_0.keys():
    print(key.title())    
    print(alien_0[key])
    
for value in alien_0.values():
    print(value)
    
    
alien_1={'color':'yellow','points':'10'}
alien_2={'color':'red','points':'15'}


aliens=[alien_0,alien_1,alien_2]

for alien in aliens:
    print(alien)   
    
    
for alien_number in range(0,30):
    alien_new={'color':'green','points':'5'}
    aliens.append(alien_new)

for alien in aliens[0:6]:
    if alien['color']=='green':
        alien['color']='yellow'
    #if alien['points']=='5':
        #alien['points']='10'
        
        
        
pizza={'crust':'thick','toppings':['mushroom','extra cheese']}

print(pizza['crust'])
for topping in pizza['toppings']:
    print(topping)
    
for crust,toppings in pizza.items():
    print(crust)
    for topping in toppings:
        print(topping)
        
        
        
writers={'rabindra':{'fname':'rabindranath','lname':'tagore'},
         'bankim':{'fname':'bankimchandra','lname':'chattopadhyay'}}


for writer,info in writers.items():
    print(writer)
    fullname=info['fname']+" "+info['lname']
    print(fullname)    

#Chapter 7
prompt="What type of car would you like to rent?"
rental_car=input(prompt)
prompt2="Let me see if i can find you a"
print(prompt2+" "+rental_car)

num=input("Enter a number")
num=int(num)
if(num%10==0):
    print(str(num)+" is a multiple of 10")
else:
    print(str(num)+" is not a multiple of 10")
 
    
    
number=1;
while(number<=5):
    print(number)
    number=number+1;
    
    
prompt="Tell me something and i will repeat it"
prompt+="\n type quit to exit "

message=""
while message!='quit':
    message=input(prompt)
    print(message)
    
    
    
while ((message.lower()!='quit')==True):
    message=input(prompt)
    if message.lower()=='quit':
        break
    else:
        print(message)
        
        
current_number=0
while(current_number<10):
    current_number=current_number+1;
    if current_number%2==0:
        continue
    print(current_number)
    
unconfirmed_users=['brian','john','candace']
confirmed_users=[]

while unconfirmed_users:
    current_user=unconfirmed_users.pop()
    print(current_user)
    confirmed_users.append(current_user)
    
print(confirmed_users)
    
responses={}
polling_active=True

while polling_active:
    name=input("Enter name")
    response=input("Which party?")

    responses[name]=response

    yn=input("Another response to input?")
    if(yn=='no'):
        polling_active=False
        
print(responses)

#Chapter 8
def greet_user(username):
    print(username)
    
greet_user('Kaustav')

def pet_info(pet_type,pet_name='harry'):
    print("I have a "+ pet_type)
    print("His name is "+ pet_name)

pet_info('dog')

def pet_info(pet_type,pet_name='harry'):
    info= "I have a "+ pet_type + " " +"His name is "+ pet_name
    return info

out=pet_info('dog')
print(out)

def name(first_name,last_name,middle_name=''):
    if middle_name:
        namenew=first_name+" "+middle_name+" "+last_name
        return namenew
    else:
        namenew=first_name+" "+last_name
        return namenew
    
name2=name(first_name='tom',middle_name='dick',last_name='harry')
print(name2)
    
dict={}
def build_dict(firstname,lastname):
    dict={'first':firstname,'last':lastname}
    return dict

name=build_dict('tom','dick')
print(name)

def fullname(firstname,lastname):
    fullname=firstname + " " + lastname
    return fullname

while True:
    fname=input("Enter your first name")
    if (fname=='q'):
        break
    lname=input("Enter your last name")
    if (lname=='q'):
        break
    name=fullname(fname,lname)
    print(name)
    
def get_names(characters):
    for character in characters:
        print(character.title())

c=['Chandler','Monica','Ross']
get_names(c)
    
def print_completed_models(unprinted_models,completed_models):
    while unprinted_models:
        completed_model=unprinted_models.pop()
        completed_models.append(completed_model)
        
def show_completed_models(completed_models):
    for completed_model in completed_models:
        print(completed_model)
        
unprinted_models=['circle','square','rectangle']
completed_models=[]

print_completed_models(unprinted_models,completed_models)
show_completed_models(completed_models)

def make_pizza(size,*toppings):
    print(size)
    for topping in toppings:
        print(topping)
        
make_pizza(16,'mushroom')
make_pizza(12,'green chillies','pepperoni')

#Chapter-9
class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(self.name.title())
        print(self.age)
        
    


my_dog=Dog('willie',6)
print(my_dog.name.title())
my_dog.sit()

class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.ppp=0
    def describe_restaurant(self):
        print(self.restaurant_name+" "+self.cuisine_type+" ")
    def describe_ppp(self,pppinput):
        self.ppp=pppinput
        print(str(self.ppp))
    def open_restaurant(self):
        print(self.restaurant_name+" "+"restaurant is open")
        
        
        
restaurant=Restaurant('Mocambo','Continental')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.describe_ppp(799)

class PeterCat(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        super().__init__(restaurant_name,cuisine_type)
    def print_cost(self,costinput):
        self.cost=costinput
        print(str(self.cost))
    
myfav=PeterCat('Peter Cat','Mughlai')
myfav.describe_restaurant()
myfav.print_cost(80)

filepath='F:/Python_New/pi_digits.txt'
with open(filepath)as file_object:
    for line in file_object:    
        print(line.rstrip())
        
with open(filepath)as file_object:
    lines=file_object.readlines()
    pi_string=''
    for line in lines:
        print(line)
        pi_string+=line.rstrip()
        
print(pi_string)

prompt='Enter bday in mmddyy'
birthday=input(prompt)
if birthday in pi_string:
    print("Yeeeaaaahhhhh")
else:
    print("Awwwwwwww")
    
with open(filepath,'w') as file_object:
    file_object.write('I love programming\n')
    file_object.write('I love creating new games\n')
    
with open(filepath) as file_object:
    contents=file_object.read()
    print(contents)    

with open(filepath,'a') as file_object:
    file_object.write('I love data science\n')
    file_object.write('I love ML\n')
    
with open(filepath) as file_object:
    contents=file_object.read()
    print(contents)

prompt="please enter your name"
guest=input(prompt)
with open('guests.txt','a') as file_object:
    file_object.write(guest+"\n")


try:
    5/0
except ZeroDivisionError:
    print("You can't divide by zero")
  
    

while True:
    first_number=input("Enter a number")
    if first_number=='q':
        break
    second_number=input("Enter another number")
    try:
        answer=int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero")
    else:
        print(answer)
    
try:
    with open('bhangra.txt') as file_object:
        contents=file_object.read()
except FileNotFoundError:
    print("dada file nei")
    
    
def file_word_count(filename):
    try:
        with open(filepath) as file_object:
            contents=file_object.read()
    except FileNotFoundError:
        print("blah")
    else:
        words=contents.split()
        num=len(words)
        print(num)


filename="guests.txt"
file_word_count(filename)    
    

import json
numbers=[1,3,5,7,9]
filename='numbers.json'
with open(filename,'w')as file_object:
    json.dump(numbers,file_object)

import json
with open(filename) as file_object:
    numbers=json.load(file_object)
    
print(numbers)





