import random




def outputtemplate (random1,yourguess, result):
	outputtemplate_1="""
The target was {}.
Your guess was {}.
That's under by {}.
""".format(random1,yourguess, result)
	return outputtemplate_1

def outputtemplate2 (random1, yourguess, result):
	outputtemplate_2="""
The target was {}.
Your guess was {}.
That's over by {}.
""".format(random1,yourguess,result)
	return outputtemplate_2

def outputtemplate3 (random1, yourguess):
	outputtemplate_3="""
The target was {}.
Your guess was {}.
That's correct!!!
""".format(random1,yourguess)
	return outputtemplate_3

def main():
	minnumber = int(raw_input("What is the minimum number?:"))
	maxnumber = int(raw_input("What is the maximum number?:"))
	output = """ The number is between {} and {}""".format(minnumber, maxnumber) 
	random1 = random.randint (minnumber, maxnumber)
	print output 
	yourguess= int(raw_input("What do you think it is?:"))
	result =abs(yourguess-random1)
	

	if random1>abs(yourguess):
		outputtemplate_1 =outputtemplate (random1,yourguess,result)
		print outputtemplate_1
	elif random1 < abs(yourguess):
		outputtemplate_2 = outputtemplate2(random1, yourguess, result)
		print outputtemplate_2
	elif random1 == abs(yourguess):
		outputtemplate_3 =outputtemplate3(random1, yourguess)
		print outputtemplate_3
main()







