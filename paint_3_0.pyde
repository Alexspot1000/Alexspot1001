
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
    if mousePressed:
        stroke(r,g,b)
        point(mouseX,mouseY)
    fill(255)
    stroke(0)
    rect(0,10,50,50)
    if mousePressed:
        stroke(r,g,b)
        point(mouseX,mouseY)
    fill(255)
    stroke(255,10,10)
    rect(200,10,50,50)
    if mousePressed:
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
        g = 10
        b = 10
    
