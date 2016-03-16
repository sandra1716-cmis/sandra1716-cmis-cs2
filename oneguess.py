import random

def guessdifference(target,guess):
	guessdif= target-guess
	return guessdif

def guessnumbers():
	number =int(raw_input("Type the min number(0-10):"))
	if number > 10 or number < 0:
		number= random.randint (0,10)
	guessminnumber = float(number)/10
	return guessminnumber


def output (minnumber,maxnumber):
	return"""
The target was {}.
Your guess was {}.
That's under by {}.
""".format(target,yourguess,guessdifference)


def main():
	minnumber = raw_input("What is the minimum number?:")
	maxnumber = raw_input("What is the maximum number?:")
	thinking= raw_input("I'm thinking of a number from {} to {}")
	yourguess= raw_input("What do you think it is?")
main()


