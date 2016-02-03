myname = "Sandra" #defined my name
myageindecimals = 16.9 #defined my age in decimals
myheightinmeters = 1.62 #defined my height in meters
onesideofsquare = 2 #define one side of a square
lengthofrectangle = 4 #defined one length of a rectangle
heightofrectangle = 5 #defined the height of the rectangle
oneyearinmonths = 12 #defined the number of months in a year
myage = 16 #defined my age
myageinmonths = oneyearinmonths * myage #calculated my age in months using two codes
averagefemalelifeexpectancy = 71 #defined the average female life expectancy 
myage =16 #defined my age
yearstolive = averagefemalelifeexpectancy - myage #calculated the number of years i had left to live
onemeterinfeet = 3.28084 #defined how many feet are in meters
myheightinfeet = myheightinmeters * onemeterinfeet #calculated my height in feet
averagefemaleheightthailand = 157.3 #defined the average female height in Thailand. 
myheight = 162 #defined my height
differenceofmyheightandaverageheight = myheight - averagefemaleheightthailand #calculated the difference between my height and the average female height in Thailand. 
areaofsquare = onesideofsquare * onesideofsquare #calculated the area of a square with a previous defined side. 
volumeofhalfacube = (onesideofsquare ** 3 )/2 #calculated the volume of half a cube
oneninethareaofrectangle = (heightofrectangle * lengthofrectangle) * (1.0/9) #calculated one ninth of the area of a rectangle 
print "Hello, people." + "My name is" + " " + myname + "." + "I am" + " " + str(myage) + "years old." + "I am" + " " + str(myageinmonths) + " " + "months old." + "I have approximately" + " " + str(yearstolive) + " " + "years to live." + "I am" + " " + str(myheight) + " " + "centimeters tall."
print "Hi there","i have a square and a rectangle.","The square has a side of",str(onesideofsquare),"units.","Its area is",str(areaofsquare),"units squared.","The volume of half the square is",str(volumeofhalfacube),"units cubed.","The rectangle has a lenth of",str(lengthofrectangle),"and height of",str(heightofrectangle),"units."
winkyface = ";)" 
print winkyface * int(10000)
