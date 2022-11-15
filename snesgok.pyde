a = 0
def setup ():
    size (600,600)
    
def draw ():
        global a
        background(0)
        ellipse (a,a,50,50)
        a = a + 10
