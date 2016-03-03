#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for?
# It is an assignment operator. It gives value to a variable. 

#2 3pts) Write a technical definition for 'function'
# A function is a named sequence of statements that performs a computation 

#3 1pt) What does the keyword "return" do? -1
# The "return" gives an output to whatever value you gave a variable. It is used to call the function. 

#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below
#	1: boolean true, false
#	2: integer 0,1
#	3: floating point 0.4, 8.9
#	4: string "hello" "how are you"
#	5: tuple ("sandra", 16, "student") ("hungry", "food")
#
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
# Funtion definition specifies the name of a new function and the sequence of statements that execute when the function is called.
# Function call is when the flow jumps to the body of the function and executes all the statements there and then comes bak to pick up where it left off instead of going to the next statement. 

#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them
#	1:input : defining what you're going to do
#	2:data : giving value to your variables
#	3:output :calling or printing what you put in
#
#Part 2: Programming (25 points)
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:

import math

def circle_area(r):
	circlearea = math.pi * (r**2)
	return circlearea


circlearea1 = raw_input ("Area of C1:")
circlearea2 = raw_input ("Area of C2:")
circlearea3 = raw_input ("Area of C3:")

print circle_area

#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...

# Hint: Radius is the square root of the area divided by pi

