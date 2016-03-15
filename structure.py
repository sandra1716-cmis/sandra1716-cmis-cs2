import math



def BMR (weight,height,age):
	bmr = 655 + (4.35*weight_pounds) + (4.7*height_inches) - (4.7*age_years)
	return bmr


def output (name,weight_pounds, height_inches, age_years, bmr):
	return """

Hey {}!
Did you know your BMR is:
655 + (4.35*{}) + (4.7*{}) - (4.7*{}) = {}
""".format (name,weight_pounds, height_inches, age_years, bmr)


def main():
	name = raw_input ("What's your name?:")
	weight_pounds = raw_input ("Type your weight in pounds:")
	height_inches= raw_input ("Type your height in inches:")
	age_years= raw_input ("Type your age in years:")
	bmr = 655 + (4.35*int(weight_pounds)) + (4.7*int(height_inches)) - (4.7*int(age_years))
	print output(name,weight_pounds, height_inches, age_years, bmr)

main()




