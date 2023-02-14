#Python program which accepts the radius of a circle from the user and computes area.

import math as m
Radius = float (input ("Input the radius of the circle: ")) 
areaofcircle= m.pi*Radius*Radius
print ("The area of the cicrle with",Radius,"is:",areaofcircle)

# Python program to accept a filename from the user and print the extension of that.
import os 
Filename= (input("Input the filename:"))
Break= os.path.splitext(Filename)[-1].lower()
print("The extension of the file is:",Break)
