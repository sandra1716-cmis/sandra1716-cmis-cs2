import math

BMR(Basal Meabolic Rate) this formula uses your gender, height, weight, & age to calculate your Basal Metabolic Rate. This calculates the amount of calories you need based on your body weight. 

Women BMR = 655 + (4.35*wp) + (4.7*hi) - (4.7*age)
BMR = Basal Metabolic Rate
wp = weight_in_pounds
hi = height_in_inches
age = age_in_years

def BMR (wight,height,age):
	bmr = 655 + (4.35*weight_pounds) + (4.7*height_inches) - (4.7*age_years)
	return bmr


def output (name,weight_pounds, height_inches, age_years, bmi):
	return = """

Hey {}!
Did you know your BMR is:
655 + (4.35*{}) + (4.7*{}) - (4.7*{}) = {}
""".format (name,weight_pounds, height_inches, age_years, bmr):


def main():
	name = raw_input ("What's your name?:")
	weight_pounds = raw_input ("Type your weight in pounds:")
	height_inches= raw_input ("Type your height in inches:")
	age_years= raw_input ("Type your age in years")
	bmr = BMR(float(weight_pounds), float(height_inches), float(age_years))
	print output(name,weight_pounds, height_inches, age_years, bmi)

main()


z = add(int(x), int(y))

out = output(name,x,y,z)
print out







