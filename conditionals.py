import random

#This script will a game where you will eat at an italian restaurant if you are hungry
#if you are hungry you will eat at the restaurant and choose between two foods :pizza and lasagna
#if you are not hungry you will not eat and leave. 

def hunger (decision):
	
	if decision == "yes":
		print "The choices are"
		foodchoice =raw_input ("Would you like to have cheeze pizza or lasagna?:")
		food(foodchoice)
	elif decision =="No":
		print "Thank you for coming, have a nice day!"

def food(decision2):
	if decision2 == "cheeze pizza":
		print "Your cheeze pizza will be prepared in 15 min."
	elif decision2 == "lasagna":
		print "Your lasagna will be prepared in 20 min." 



def main():
	decision1 = raw_input("Are you hungry?:")
	
	hunger (decision1)
	

	
main()



