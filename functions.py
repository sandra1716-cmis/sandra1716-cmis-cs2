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

addition = add(5,6)
addition2 = add(7,8)
subtraction = sub(6,5)
subtraction2 = sub(9,6)
multiplication = mul(2, 2)
multiplication2 = mul(3, 3)
divide = div(1.0,5)
divide2 = div(6.0,12)
hoursfromseconds= hours_from_seconds(97500, 4800)
hoursfromseconds2= hours_from_seconds(78900, 2400)
circlearea = circle_area(6)
circlearea2 = circle_area(7)
spherevolume = sphere_volume (6)
spherevolume2 = sphere_volume (8)
averagevolume = avg_volume (15,20)
averagevolume2 = avg_volume (20,25)
area1 = area (2,3,3.5)
area2 = area (0.5,1,0.5)
rightalign = right_align ("Yo")
rightalign2 = right_align ("Yo man")
center1 = center ("Hey")
center2 = center ("Heyy")
msgbox1 = msg_box("Hi")
msgbox2 = msg_box("Hei")

#print all the functions twice
print msg_box (str(addition))
print msg_box (str(addition2))
print msg_box (str(subtraction))
print msg_box (str(subtraction2))
print msg_box (str(multiplication))
print msg_box (str(multiplication2))
print msg_box (str(divide))
print msg_box (str(divide2))
print msg_box (str(hoursfromseconds))
print msg_box (str(hoursfromseconds2))
print msg_box (str(circlearea))
print msg_box (str(circlearea2))
print msg_box (str(spherevolume))
print msg_box (str(spherevolume2))
print msg_box (str(averagevolume))
print msg_box (str(averagevolume2))
print msg_box (str(area1))
print msg_box (str(area2))
print msg_box (str(rightalign))
print msg_box (str(rightalign2))
print msg_box (str(center1))
print msg_box (str(center2))
print msg_box (str(msgbox1))
print msg_box (str(msgbox2))


