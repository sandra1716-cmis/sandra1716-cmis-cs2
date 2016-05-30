def countdown(x):

	while x > 0:
		print x
		x -=1
countdown (10)

def counter(x):
	while x<= 0:
		print x
		x+=1
	
	
def sumOfOdds(n):
	total =0
	if n>0:
		while n>0:
			if n% 2 ==1:
				total += n
			n -= 1
	elif n<0:
		while n<0:
			if n% 2==1:
				total +=n
			n+= 1
	return total

print sumOfOdds(10)


def grid (w,h):
	out =""
	while w>0:
		out += "."
		w-= 1
	return out
	

print grid (10,10)
