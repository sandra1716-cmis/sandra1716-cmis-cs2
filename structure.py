import math

def add (x,y):
	return x+y


def output (name,x,y,z):
	out = """

Hey {}!
Did you know:
{}+{}={}
""".format(name,x,y,z)
	return out


def main():
name = raw_input ("What's your name?:")
x = raw_input ("Type a number:")
y= raw_input ("Type another:")

z = add(int
