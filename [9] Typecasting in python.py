# tpyecasting or type conversion: conversion from one to another data type 

'''
Two types of type casting 
(i) Explict conversion -  conversion done via developer
(ii) Implict conversion - conversion done by python 
'''

#Examples of Explict conversion 
str = '34'
num = 2
print(int(str) + num)       #int convert string to integer 


#Examples of Implict conversion     
a = 8   #python automatically convert 'a into int
print (type(a))     #output: int

b = 3.2     #python automatically convert 'b' into float
print(type(b))      #output: float


c = a +b        #automatically covnert c into float
print(type(c))      #output: float
