g = 0
x1 = 300
y1 = 300
x2 = 300
y2 = 300
x3 = 300
y3 = 300
x4 = 300
y4 = 300
def setup():
    size(1000,1000)
    img=loadImage("cat.jpg")
    image(img,200,300)
def draw():
    global g,x1, y1, x2, y2, x3, y3, x4, y4
    rotate(0)
    img=loadImage("cat.jpg")
    image(img,200,300)
    image(img,x1,y1)
    image(img,x2,y2)
    image(img,x3,y3)
    image(img,x4,y4)
    strokeWeight(random(1,5))
    stroke(random(0,255),random(0,255),random(0,255))
    point(random(0,1000),random(0,1000))
    y1 = y1 - 0.1
    x1 = x1 + 0.1
    y2 = y2 - 0.1
    x2 = x2 - 0.1
    x3 = x3 - 0.1
    y3 = y3 + 0.1
    x4 = x4 + 0.1
    y4 = y4 + 0.1
    g+=0.1

    
    
    
