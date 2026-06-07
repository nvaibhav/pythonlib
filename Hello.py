#!/usr/bin/env python3.14
print("Hello")
fruit = 'apple'
Fruit = 'orange'
my_fruit = "mango"
mysentence = "She said, \"That's the\""
print(fruit,Fruit,my_fruit)
print(mysentence)
print(my_fruit[1])
print(len(my_fruit))
print(my_fruit.upper())
print("-"*6)
mynum=5
print(mynum)
print(str(mynum)+':')
print('I {} '.format('love'))
print('{0:8}'.format('vaib'))
#my_fruit = input("Enter fruit")
print(my_fruit)
print("-"*len(my_fruit))

my_num = 4/3
print(my_num)
print("My number:{}".format(my_num))
print("My number:{}"+str(my_num))
"""This is a long comment
This is a free form content
"""

def say_hi(name):
  print('Hi {}'.format(name))

say_hi('Cool')

say_hi(name="hhh")

def odd_or_even(num):
      "Determine o or e"
      if num % 2 == 0:
        return True
      else:
        return False
print(odd_or_even(7))

#lists
animlas = ['man','bear','pig']
print(animlas[0])
print(animlas[-1])
animlas.extend(['horse'])
print(animlas)
animlas.insert(2,'cat')
print(animlas)
print(animlas[2:3])
print(animlas[:3])
print(animlas[1:])
try:
    myindex=animlas.index['horse']
except:
    print("exception")
#print('index:{}'.format(myindex))

for item in animlas:
  print(item.upper())
sorted_animals=sorted(animlas)
print(sorted_animals)

for number in range (1,3):
    print(number)

todo_list = [];
for number in range (0,3):
    #task = input("Enter a task for your to-do list.Press <enter> when done:")
    task=''
    todo_list.append(task)
title = "Your To-Do List:"    
print(title)
print("-"*len(title))

for task in todo_list:
    print(task)

contacts = {'Jason':'555','Carl':'999'}
jason_phone = contacts['Jason']
print('Dial {} for Jason\'s phone'.format(jason_phone))
contacts['Jason']='000'
contacts['Tony']='777'
print(contacts)
if 'Jason' in contacts.keys():
    print('Jason exists')
print("Type of contacts:{}".format(type(contacts)))
mycontacts = {'jeff':'afriad','David':'small','Jason':'cool'}
print(mycontacts)
mycontacts['jeff']='big'
print(mycontacts)
mycontacts['myself']='Thai'
print(mycontacts)
print(mycontacts)
print(mycontacts)

print()
for key in mycontacts:
    print('key:{},value:{}'.format(key,mycontacts[key]))

airports = ("O'Hare Airport","ORD")
for ports in airports:
    print("Port:{}".format(ports))
print()
airports = [("O'Hare Airport","ORD"),
            ("Pune Airport","PNE")]
for (port,code) in airports:
    print("Port:{} Code:{}".format(port,code))

airports = "ttt"
print()
print(airports)
print()

file_content = []
#Files
with open('file.txt') as file:
    line_number = 1
    for line in file:
        file_line = '{}:{}'.format(line_number,line.rstrip())
        file_content.append(file_line)
        line_number += 1
          

print('File contents:{}'.format(file_content))
try:
    with open('file1.txt','w') as file:
          file.write(str(file_content));
except:
    print("Couldn't open file file1.txt");

#Module
import time
from time import asctime, sleep

print("time:{}".format(time.asctime()))
print(asctime())
sleep(3)
print(asctime())
print("__name__:"+__name__)

from Cat import meow,custom_meow
meow()
custom_meow("Me")

import logging
logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(format="%(levelname)s:%(name)s:%(message)s vvv")
logging.warning("This is a warning")
logging.error("This is a error")
logging.info("This is a info")
logging.debug("This is a debug")
logging.critical("This is a critical")

mylogger = logging.getLogger(__name__)
mylogger.warning("This is my logger")

print("Employee")
import Employee
employeeOne = Employee.Employee("")
print("Employee name="+employeeOne.name)
employeeOne.hasAchievedTarget()

employeeTwo = Employee.Employee("")
employeeTwo.name = "Vaibhav"

Employee.name = "Nakil"
print("employeeTwo.name="+employeeTwo.name)

employeeOne = Employee.Employee("")
employeeOne.employeeDetails()
employeeOne.printEmployeeDetails()
print(employeeOne.name)
employeeOne.printme()

employeeThree = Employee.Employee("Mihir")
employeeThree.printEmployeeDetails()
