r = 0

g = 0

b = 0

def setup():
    fullScreen()
    background(255)
    strokeWeight(50)
    
def draw():
    global r,g,b;
    if mousePressed and (mouseButton == RIGHT):
        background(255)
    fill(255)
    stroke(212, 32, 188)
    rect(100,10,50,50)
    if mousePressed and (mouseButton == LEFT):
        stroke(r,g,b)
        point(mouseX,mouseY)
    fill(255)
    stroke(0)
    rect(0,10,50,50)
    if mousePressed and (mouseButton == LEFT):
        stroke(r,g,b)
        point(mouseX,mouseY)
    fill(255)
    stroke(255,0,0)
    rect(200,10,50,50)
    if mousePressed and (mouseButton == LEFT):
        stroke(r,g,b)
        point(mouseX,mouseY)
    fill(255)
    stroke(0, 255, 0)
    rect(300,10,50,50)
    if mousePressed and (mouseButton == LEFT):
        stroke(r,g,b)
        point(mouseX,mouseY)
    fill(255)
    stroke(70, 130, 180)
    rect(400,10,50,50)
    if mousePressed and (mouseButton == LEFT):
        stroke(r,g,b)
        point(mouseX,mouseY)
    fill(255)
    stroke(255, 0, 127)
    rect(500,10,50,50)
    if mousePressed and (mouseButton == LEFT):
        stroke(r,g,b)
        point(mouseX,mouseY)
    fill(255)
    stroke(0, 153, 153)
    rect(600,10,50,50)
    if mousePressed and (mouseButton == LEFT):
        stroke(r,g,b)
        point(mouseX,mouseY)
    fill(255)
    stroke(132, 17, 220)
    rect(700,10,50,50)
    if mousePressed and (mouseButton == LEFT):
        stroke(r,g,b)
        point(mouseX,mouseY)
        
def mouseClicked():
    global r,g,b;
    
    if mouseX > 0 and mouseX < 50 and mouseY > 10 and mouseY < 50:
        r = 0 
        g = 0
        b = 0
    if mouseX > 100 and mouseX < 150  and mouseY > 10 and mouseY < 50:
        r = 212
        g = 32
        b = 188
    if mouseX > 200 and mouseX < 250  and mouseY > 10 and mouseY < 50:
        r = 255
        g = 0
        b = 0
    if mouseX > 300 and mouseX < 350  and mouseY > 10 and mouseY < 50:
        r = 0
        g = 255
        b = 0
    if mouseX > 400 and mouseX < 450  and mouseY > 10 and mouseY < 50:
        r = 70
        g = 130
        b = 180
    if mouseX > 500 and mouseX < 550  and mouseY > 10 and mouseY < 50:
        r = 255
        g = 0
        b = 127
    if mouseX > 600 and mouseX < 650  and mouseY > 10 and mouseY < 50:
        r = 0
        g = 153
        b = 153
    if mouseX > 700 and mouseX < 750  and mouseY > 10 and mouseY < 50:
        r = 132
        g = 17
        b = 220
