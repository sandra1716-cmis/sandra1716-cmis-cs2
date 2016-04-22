
def countup(n):
	if n>= 10:
		print "Blastoff!"
	else:
		print n
		countup(n+1)

def countdown(n):
	if n<=0:
		print "Ok"
	else:
		print n
		countdown(n-1)

def countup_from(start, stop):
	pass
def countdown_from(start, stop):
	pass

def main():
	countdown(10)
	countup(2)
	return

main()
def countdown_from (start, stop):
	if start < stop:
		print "Blastoff"
	else:
		print start
		countdown_from(start -1, stop)
def main():
	countdown_from(50,0)
main()

def adder (n, total):
	if n =="" :
		return "The sum is" +str(total) 
	else:
		total += float(n) 
		n = raw_input("Running total:" +str(total) + "\n Next number:")
		return adder (n,total)
	

def main():	
	outcome = adder (0,0)
	print outcome
	
main()
		  
