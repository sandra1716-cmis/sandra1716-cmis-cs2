import random


def outputtemplate (random1,yourguess, result):
	outputtemplate_1="Guess higher"
	return outputtemplate_1

def outputtemplate2 (random1, yourguess, result):
	outputtemplate_2="Guess lower"
	return outputtemplate_2

def outputtemplate3 (random1, yourguess):
	outputtemplate_3="""
The target was {}.
Your guess was {}.
That's correct!!!
""".format(random1,yourguess)
	return outputtemplate_3


def guess(randomNumber, runs):
	yourguess = int(raw_input("Your Guess: "))
	result = abs(yourguess-randomNumber)
	if runs >= 5:
		print "You've run out of tries"
	elif randomNumber > abs(yourguess) and runs < 4:
		outputtemplate_1 = outputtemplate(randomNumber, yourguess, result)
		print outputtemplate_1
		guess(randomNumber, runs+1)
	elif randomNumber < abs(yourguess) and runs < 4:
		outputtemplate_2 = outputtemplate2(randomNumber, yourguess, result)
		print outputtemplate_2
		guess(randomNumber, runs+1)	
	elif randomNumber == abs(yourguess):
		outputtemplate_3 = outputtemplate3(randomNumber, yourguess)
		print outputtemplate_3

def rounds(randomNumber, runs):
	if runs < 5:
		guess(randomNumber, runs)
	else:
		print "You've run out of tries"





def main():
	minnumber = int(raw_input("What is the minimum number?: "))
	maxnumber = int(raw_input("What is the maximum number?: "))
	output = """ the number is between {} and {}""".format(minnumber, maxnumber)
	random1 = random.randint (minnumber, maxnumber)
	print output
	rounds(random1, 0)


main()
