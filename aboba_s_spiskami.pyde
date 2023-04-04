slowa=[u"еда",u"еда",u"еда",u"еда"]
x = 1
def setup():
    fullScreen()
    background(255)
    textSize(50)
def keyPressed():
    global x
    if key == CODED:
        if keyCode == UP:
            x + 1
def draw():
    global x
    
    if x==1:
        fill(127, 255, 0)
        text(slowa[0],20,50)
    else:
        fill(0)
        text(slowa[0],20,50)
    if x==2:
        fill(127, 255, 0)
        text(slowa[1],20,100)
    else:
        fill(0)
        text(slowa[1],20,100)



    
