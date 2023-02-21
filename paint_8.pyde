r = 0

g = 0

b = 0

size1 = 50

x = 0

def setup():
    fullScreen()
    background(255)
    strokeWeight(50)
    
def draw():
    global r,g,b,size1,x;
    
    strokeWeight(size1)
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
    global r,g,b,size1,x;
    
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
    if mousePressed and (mouseButton == CENTER):
            for x in range(1000):
                ellipse(mouseX,mouseY,20,20)
    fill(0,0,0)
    textSize(30)
    text(size1,1250,40)
    text("+",1290,38)
    text("-",1230,38)
    if mouseX > 1290 and mouseX < 1315 and mouseY > 18 and mouseY < 38:
        fill(255,255,255)
        rect(1250,10,40,35)
        size1 = size1 + 1
        
    if mouseX > 1230 and mouseX < 1251 and mouseY > 18 and mouseY < 38:
        fill(255,255,255)
        rect(1250,10,40,35)
        size1 = size1 - 1
def keyPressed():
   def keyPressed():
    global x
    if key == CODED:
        if keyCode == UP: 
            for x in range(1000):
                fill(132, 17, 220)
                ellipse(mouseX,mouseY,20,20)
