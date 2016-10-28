from graphics import *
import random
#Colour = [(255,255,0),(0,255,0),(0,128,0),(127,0,255),(255,0,0)]
text_file = open("dataNumbers.txt", "r")
dataNumbers = text_file.read().split('\n')
list = []
for word in dataNumbers:
    list.append(int(word))
text_file.close()

for word in dataNumbers: print(">" + word + "<")
window = GraphWin("Results", 500, 500)
posxBar = 0
posxBar2 = 0
while True:
    for word in list:
        rect = Rectangle(Point(200,30),Point(283,70))
        rect.setOutline(color_rgb(175,190,196))
        rect.setWidth(7)
        rect.setFill(color_rgb(192,175,196))
        rect.draw(window)
        
        text = Text(Point(240,50),word)
        text.setSize(36)
        text.setStyle('bold')
        text.draw(window)
        
        if word <= 45:
            rect = Rectangle(Point(posxBar,500),Point(posxBar+20,500-int(word)*2))
            rect.setFill('yellow')
            rect.draw(window)
            posxBar = posxBar + 20
        elif word > 45 and word <= 50:
            rect = Rectangle(Point(posxBar,500),Point(posxBar+20,500-int(word)*2))
            rect.setFill('green')
            rect.draw(window)
            posxBar = posxBar + 20
        elif word > 50 and word <= 57:
            rect = Rectangle(Point(posxBar,500),Point(posxBar+20,500-int(word)*2))
            rect.setFill('blue')
            rect.draw(window)
            posxBar = posxBar + 20
        elif word > 57 and word <= 67:
            rect = Rectangle(Point(posxBar,500),Point(posxBar+20,500-int(word)*2))
            rect.setFill('red')
            rect.draw(window)
            posxBar = posxBar + 20
        elif word > 67 and word <= 100:
            rect = Rectangle(Point(posxBar,500),Point(posxBar+20,500-int(word)*2))
            rect.setFill('purple')
            rect.draw(window)
            posxBar = posxBar + 20
#        time.sleep(0.7)
        #box = Rectangle(Point(0,0),Point (520,520))
        #box.setFill(color_rgb(int(word),int(word)*2,int(word)*3))
#        time.sleep(0.9)
        #box.draw(window)
        posx = random.randrange(0,450)
        posy = random.randrange(0,450)
        col = random.randrange (0,255)
        
#        ball = Circle(Point(250,250), int(word)*2)
    # ball.setFill(color_rgb(int(word)+30,int(word)*2,int(word)+20))
        #ball.draw(window)
        time.sleep(0.6)
    
window.getMouse() 