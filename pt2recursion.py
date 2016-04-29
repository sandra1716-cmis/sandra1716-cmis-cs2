def biggest (num):
	new = raw_input ("Next:")
	if new == "":
		return num
	elif float(new) > float(num):
		return biggest (float(new))
	elif num > float (new):
		return biggest (num)

def main():
	answer = biggest (-float("inf"))
	print answer
main()

def smallest (num):
	new = raw_input ("Next:")
	if new == "":
		return num
	elif float(new) < float(num):
		return smallest (float(new))
	elif num < float (new):
		return smallest (float(num))

def main():
	answer = smallest (float("inf"))
	print answer
main()
