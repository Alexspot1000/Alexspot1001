ABOBA = [100,1,300,200,225,888,777,333,101]
cveta = [0,255,123,168,201,222,111,211,266]
obvodka = [100,1,300,200,225,888,777,333,101]
def setup():    
    fullScreen
def draw():
    global cveta, ABOBA, obvodka
    fill(cveta[int(random(0,9))],cveta[int(random(0,9))],cveta[int(random(0,9))])
    
