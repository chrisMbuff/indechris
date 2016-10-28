from graphics import *
import random
import time

text_file = open("dataNumbers.txt", "r")
dataNumbers = text_file.read().split('\n')
text_file.close()

#for word in dataNumbers: print(">" + word + "<")
window = GraphWin("Results", 500, 500)

while True:
    for word in dataNumbers:
        posx = random.randrange(0,400)
        posy = random.randrange(0,400)
        col = random.randrange (0,255)
        ball = Circle(Point(posx,posy), int(word))
        ball.setFill(color_rgb(int(word),int(word)*3,col))
        time.sleep(0.4)
        ball.draw(window)
    
window.getMouse()