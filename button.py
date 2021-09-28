Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 

def buttons():
	left = Rectangle(Point(25, 55), Point(55, 85))  
	right = Rectangle(Point(145, 55), Point(175, 85))

	left.setFill("red")
	right.setFill("green")

	text1= Text(Point(40,70), "Choose a kids card")
	text1.draw(win)

	text2= Text(Point(160, 70), "Choose an adult card")
	text2.draw(win)
	


	
>>> 
