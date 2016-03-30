import random

#This script will a game where you will eat at an italian restaurant if you are hungry
#if you are hungry you will eat at the restaurant and choose between two foods :pizza and lasagna
#if you are not hungry you will not eat and leave. 

def hunger (decision):
	
	if decision == "yes":
		print "Welcome to the World Famous Italian Restaurant!!"
		foodchoice =raw_input ("Would you like to have cheeze pizza or lasagna to eat?: ")
		food(foodchoice)
	elif decision =="no":
		print "Goodbye, have a nice day!"

def food(decision2):
	if decision2 == "cheeze pizza":
		print "Your cheeze pizza will be prepared in 15 min."
	elif decision2 == "lasagna":
		print "Your lasagna will be prepared in 20 min." 
	
		
def drink (drinkoption):
	if drinkoption == "yes":
		print "We have water and coke which one would you like?"
	elif drinkoption == "no":
		print "Alright if that's all here's your check."



def main():
	
	decision1 = raw_input("Are you hungry?: ")
	
	hunger (decision1)
	
	decision3 = raw_input ("Would u like something to drink?: ")

	drink (decision3)
main()



