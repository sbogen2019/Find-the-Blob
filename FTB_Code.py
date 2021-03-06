import Myro
from Myro import *
from Graphics import *
from random import *

width = 500
height = 500
sim = Simulation("Maze World", width, height, Color("gray"))

#outside walls
sim.addWall((10, 10), (490, 20), Color("black"))
sim.addWall((10, 10), (20, 490), Color("black"))
sim.addWall((480, 10), (490, 490), Color("black"))
sim.addWall((10, 480), (490, 490), Color("black"))

#blue spot
poly = Circle((50, 50), 45)
poly.bodyType = "static"
poly.color = Color("blue")
poly.outline = Color("black")
sim.addShape(poly)

#red spot
poly = Circle((450, 50), 45)
poly.bodyType = "static"
poly.color = Color("red")
poly.outline = Color("black")
sim.addShape(poly)

#green spot
poly = Circle((50, 450), 45)
poly.bodyType = "static"
poly.color = Color("green")
poly.outline = Color("black")
sim.addShape(poly)

#yellow spot
poly = Circle((450, 450), 45)
poly.bodyType = "static"
poly.color = Color("yellow")
poly.outline = Color("black")
sim.addShape(poly)

#begin simulation and sets robot's position
makeRobot("SimScribbler", sim)
sim.setPose(0, width/2, height/2, 0)

sim.setup()

# 1-RED
# 2-GREEN
# 3-BLUE
# 4-YELLOW

#The following is a helper function 
#Inputs: A picture and a color represented by the list above
#Returns the average x location of the color in the picture or -1 if the robot has found the color spot

def findColorSpot(picture, color):
    xPixelSum = 0
    totalPixelNum = 0
    averageXPixel = 0

    show(picture)

    for pixel in getPixels(picture):
        if(color == 1 and getRed(pixel) > 150 and getGreen(pixel) < 50 and getBlue(pixel) < 50):
            xPixelSum += getX(pixel)
            totalPixelNum += 1
        elif(color == 2 and getRed(pixel) < 50 and getGreen(pixel) > 100 and getBlue(pixel) < 50):
            xPixelSum += getX(pixel)
            totalPixelNum += 1
        elif(color == 3 and getRed(pixel) < 50 and getGreen(pixel) < 50  and getBlue(pixel) > 150):
            xPixelSum += getX(pixel)
            totalPixelNum += 1
        elif(color == 4 and getRed(pixel) > 200 and getGreen(pixel) > 150 and getBlue(pixel) < 50):
            
            xPixelSum += getX(pixel)
            totalPixelNum += 1
    if(totalPixelNum != 0):
        averageXPixel = xPixelSum/totalPixelNum

    #Handles the case where robot has found the spot if it is near it
    #If necessary adjust the value
    if(totalPixelNum/(getWidth(picture)*getHeight(picture)) > 0.21):
        averageXPixel = -1

    return averageXPixel
    

# Use the following integers for colors:
# 1-RED
# 2-GREEN
# 3-BLUE
# 4-YELLOW 

#code starts here

pic = takePicture()
x = findColorSpot(pic,1) # for red
y = findColorSpot(pic,2) # for green
z = findColorSpot(pic,3) # for blue
q = findColorSpot(pic,4) # for yellow

#confirming that these values are 0
print(x)
print(y)
print(z)
print(q)

show(pic)
while True:
    q1 = askQuestion("Do you want to find a color?", ["Yes", "No"])
    if q1 == "No":
        print("Come Back Soon!")
        break
    if q1 == "Yes":    
        q2 = askQuestion("What color do you want to find?", ["Red", "Blue", "Green", "Yellow"])
        if q2 == "Red":
            while (x == 0):
                turnBy(randrange(90,270))
                pic = takePicture()
                x = findColorSpot(pic,1)
                show(pic)
                print(x)
                stop()
            if x != 0:
                    stop()
                    print(x)
                    while x < 118:
                        turnBy(3.14159)
                        pic = takePicture()
                        x = findColorSpot(pic,1)
                        print(x)
                        stop()
                    while x > 138:
                        turnBy(-3.14159)
                        pic = takePicture()
                        x = findColorSpot(pic,1)
                        print(x)
                        stop()
                    if x >= 118 and x <= 138:
                        forward(2,2.25)
                        pic = takePicture()
                        x = findColorSpot(pic,1)
                        print(x)
                        print("Found Red Blob!")
                        backward(2,2.25)
                        continue
        if q2 == "Green":
            while (y == 0):
                turnBy(randrange(90,270))
                pic = takePicture()
                y = findColorSpot(pic,2)
                show(pic)
                print(y)
                stop()
            if y != 0:
                    stop()
                    print(x)
                    while y < 118:
                        turnBy(3.14159)
                        pic = takePicture()
                        y = findColorSpot(pic,2)
                        print(y)
                        stop()
                    while y > 138:
                        turnBy(-3.14159)
                        pic = takePicture()
                        y = findColorSpot(pic,2)
                        print(y)
                        stop()
                    if y >= 118 and y <= 138:
                        forward(2,2.25)
                        pic = takePicture()
                        y = findColorSpot(pic,2)
                        print(y)
                        print("Found Green Blob!")
                        backward(2,2.25)
                        continue
        if q2 == "Blue":
            while (z == 0):
                turnBy(randrange(90,270))
                pic = takePicture()
                z = findColorSpot(pic,3)
                show(pic)
                print(z)
                stop()
            if z != 0:
                    stop()
                    print(z)
                    while z < 118:
                        turnBy(3.1415)
                        pic = takePicture()
                        z = findColorSpot(pic,3)
                        print(z)
                        stop()
                    while z > 138:
                        turnBy(-3.1415)
                        pic = takePicture()
                        z = findColorSpot(pic,3)
                        print(z)
                        stop()
                    if z >= 118 and z <= 138:
                        forward(2,2.25)
                        pic = takePicture()
                        z = findColorSpot(pic,3)
                        print(z)
                        print("Found Blue Blob!")
                        backward(2,2.25)
                        continue
        if q2 == "Yellow":
            while (q == 0):
                turnBy(randrange(90,270))
                pic = takePicture()
                q = findColorSpot(pic,4)
                show(pic)
                print(q)
                stop()
            if q != 0:
                    stop()
                    print(q)
                    while q < 118:
                        turnBy(3.1415926535897932)
                        pic = takePicture()
                        q = findColorSpot(pic,4)
                        print(q)
                        stop()
                    while q > 138:
                        turnBy(-3.1415926535897932)
                        pic = takePicture()
                        q = findColorSpot(pic,4)
                        print(q)
                        stop()
                    if q >= 118 and q <= 138:
                        forward(2,2.25)
                        pic = takePicture()
                        q = findColorSpot(pic,4)
                        print(q)
                        print("Found Yellow Blob!")
                        backward(2,2.25)
                        continue