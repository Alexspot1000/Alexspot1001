slowa=[u"еда",u"еда",u"еда",u"еда"]
col=[1,0,0,0]
x = 0
def setup():
    fullScreen()
    background(255)
def draw():
    global x
    for x in range (3):
        if col[x]=1:
            fill(127, 255, 0)
        else:
            fill(255)
