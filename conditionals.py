import random

#This script will a game where you will eat at an italian restaurant if you are hungry
#if you are hungry you will eat at the restaurant and choose between two foods :pizza and lasagna
#if you are not hungry you will not eat and leave. 

def hunger (decision):
	
	if decision == "yes":
		
		print "Welcome to the World Famous Italian Restaurant!!"
		foodchoice =raw_input ("Would you like to have cheeze pizza or lasagna to eat?: ")
		return food(foodchoice)
	elif decision =="no":
		print "Goodbye, have a nice day!"
		return "0"	

def food(decision2):
	if decision2 == "cheeze pizza":
		print "Your cheeze pizza will be prepared in 15 min."
		return int(20)
	elif decision2 == "lasagna":
		print "Your lasagna will be prepared in 20 min." 
		return int(25)
		
def drink (drinkoption):
	if drinkoption == "yes":
		drinkchoice = raw_input("We have water and coke which one would you like?:")
		return drinkchoice2(drinkchoice)
	elif drinkoption == "no":
		print "Alright if that's all here's your check."
		return "0"
		
def drinkchoice2 (drinkanswer):
	if drinkanswer == "water":
		print "Okay, your water will come shortly, and if that's all i'll get you your check."
		return int(3)
	elif drinkanswer == "coke":
		print  "Okay, your coke will come shortly, and if that's all i'll get you your check."
		return int(2)

def desert():
	if random.random() > 5:
		winner= raw_input ("Question: Do you like this restaurant?:")
		return True
	else:
		return False

def question(prize):
	if 


def main():
	
	decision1 = raw_input("Are you hungry?: ")
	
	foodprice = hunger (decision1)
	
	decision3 = raw_input ("Would u like something to drink?: ")

	drinkprice = drink (decision3)

	total = int(foodprice) + int(drinkprice)
	out = """
Your total is {}.
""".format(total)
	print out
	
	
main()



