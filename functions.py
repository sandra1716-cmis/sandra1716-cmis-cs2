def add(a, b): #defined a function with variables through additon 
	return a+b

c= add(3,4)


def sub(a, b): #defined a function with variables through subtraction
	return a-b

d= sub(5,3)


def mul(a,b): #defined a function with variables through multiplication 
	return a*b

e= mul(4, 4)

def div(a,b): #defined a function with variables through division
	return a/b

f= div(2.0,3)


def hours_from_seconds(a,b): #defined a function by changing seconds to hours
	return a/b

g= hours_from_seconds(86400, 3600)

import math
def circle_area(r): #defined a function by returning an area of a circle
	return math.pi * (r**2)


import math
def sphere_volume (a): #defined a function by representing an argument and changing it into the volume
	return 1.33333333333 * math.pi * (a**3)

import math
def avg_volume (a,b): #defined a function by finding the average of the volumes
	return ((1.0/6 * math.pi * a**3) + (1.0/6 * math.pi * b**3)) / 2

def area (a,b,c) : # defined a function by finding a triangles area
	n= (a+b+c)/2
	return (n*(n-a)*(n-b)*(n-c))**0.5


def right_align(word):#defined a function by right aligning a word
	return  (80-len(word))*(" ") + word

def center(word): #defined a function by centering a word 
	return  (40-len(word))*(" ") + word


def msg_box(word):
    return "+" + ((len(word)+4)*"-") + "+" + "\n" + "|" + (2*" ") + (word)+ (2*" ") + "|" + "\n" + "+" + ((len(word)+4)*"-") + "+"

#call all the functions again twice
print c
print c
print d
print d
print e
print e
print f
print f
print g
print g
print circle_area(5)
print circle_area(5)
print sphere_volume (5)
print sphere_volume (5)
print avg_volume (10,20)
print avg_volume (10,20)
print area (1,2,2.5)
print area (1,2,2.5)
print right_align ("Hello")
print right_align ("Hello")
print center ("Hello")
print center ("Hello")
print msg_box("Hello")
print msg_box("Hello")
print msg_box("I eat cats!")
print msg_box("I eat cats!")


