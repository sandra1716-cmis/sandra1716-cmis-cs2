#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#a) <
#b) >
#c) <=
#
#2) What does 'return' do?
# It gives the function a value. 1
# 
#
#
#3) What are 2 ways indentation is important in python code?
#a) It defines the functions boundaries. 1
#b) It helps keep your script organized. 1
#
#

#PART 2: Reading
#Type the values for 12 of the 16 of the variables below.
#
#problem1_a) -36 1
#problem1_b) -9 1
#problem1_c) 0 1 
#problem1_d) -5 1
#
#problem2_a) true 1
#problem2_b) false 1
#problem2_c) false 1
#problem2_d) false 
#
#problem3_a) 0.3 1
#problem3_b) 0.5 1
#problem3_c) 1 
#problem3_d) 0.5 1  
#
#problem4_a) 7 
#problem4_b) 5
#problem4_c) 0.25 /2
#problem4_d) 5 1 
#

#PART 3: Programming
#Write a script that asks the user to type in 3 different numbers.
#If the user types 3 different numbers the script should then print out the
#largest of the 3 numbers.
#If they don't, it should print a message telling them they didn't follow 
#the directions.
#Be sure to use the program structure you've learned (main function, processing function, output function)
# 23 1
#24 1
#25 1
#26 1
#27 
#28 1 
#29 
#30 
#31 1
#32 1
import math

def numberchoice (number1, number2, number3):
	if number1 == number1:
		print "your choice will work"
	elif number1 == number2:
		print "You have failed to follow instructions"

	
def main():
	number1= int(raw_input("Type in a number:"))
	number2= int(raw_input("Type in a different number:"))
	number3= int(raw_input("Type in a number different from the first two numbers:"))
	
	
main()

