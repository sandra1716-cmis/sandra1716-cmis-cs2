#Section 1: Terminology 1
# 1) What is a recursive function?
# a function that repeats itself
#
#
# 2) What happens if there is no base case defined in a recursive function? 1
#The recursice funcion will be repeated continuously until it hits the max limit. 
#
#
# 3) What is the first thing to consider when designing a recursive function? 1
# What you want as your base case and the recursive case. 
#
#
# 4) How do we put data into a function call?
# By defining a function and giving the variable a value.    1
#
# 
# 5) How do we get data out of a function call?
# By printing the function or calling it. 
#
#

#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables a1-d3.

#a1 = 1 + (2,5) = 8     1
#a2 = 1 + (6,1) = 8     1
#a3 = -1              1

#b1 = 2      1
#b2 = 1+(1,0) = 2     1
#b3 = 1 + (-1,-4) = 4     1

#c1 = 2     1
#c2 = 4     1
#c3 = 19      

#d1 = -4      
#d2 = 8     1
#d3 = 4     1

#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.

def number (n, oddtotal):
	#beforebasecase+2
	if n =="" :
		return "The average of the odd numbers are:" +str(oddtotal) 
	#beforerecursivecase+2+	
	else:
		oddtotal += int(n) 
		n = raw_input("Running total:" +str(oddtotal) + "\n Next number:")
		return number (n,oddtotal)
	

def main():	#1
	outcome = number (0,0)
	print outcome
	
main()


