import math



def BMR (weight,height,age):
	bmr = 655 + (4.35*weight) + (4.7*height) - (4.7*age)
	return bmr


def output (name,weight_pounds, height_inches, age_years, bmr):
	return """

Hey {}!
Did you know your BMR is:
655 + (4.35*{}) + (4.7*{}) - (4.7*{}) = {}
""".format (name,weight_pounds, height_inches, age_years, bmr)


def main():
	name = raw_input ("What's your name?:")
	weight_pounds = int(raw_input ("Type your weight in pounds:"))
	height_inches= int(raw_input ("Type your height in inches:"))
	age_years= int(raw_input ("Type your age in years:"))
	bmr=BMR(weight_pounds, height_inches,age_years)
	print output(name,weight_pounds, height_inches, age_years, bmr)

main()




