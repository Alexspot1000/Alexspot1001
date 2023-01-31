bg = 255

onetwo = 0

one = 255

two = 255

three = 255

def setup():
    size(600,400)
    background(bg)
    strokeWeight(50)
    
def draw():
    global bg,one,two,three,onetwo;
    #кнопка прямоугольная
    fill(0)
    stroke(0)
    # левый верхний угол 250 150, размеры 100 на 50
    rect(10,10,50,50) # x от 250 до 250+100, y от 150 до 150 + 50  
    if mousePressed:
        stroke(onetwo)
        point(mouseX,mouseY)
        #кнопка прямоугольная
    fill(255)
    stroke(212, 32, 188)
    # левый верхний угол 250 150, размеры 100 на 50
    rect(100,10,50,50) # x от 250 до 250+100, y от 150 до 150 + 50  
    if mousePressed:
        stroke(one,two,three)
        point(mouseX,mouseY)
        
    
def mouseClicked():
    global bg,one,two,three,onetwo;
    # если прямоугольная кнопка нажата
    
    if mouseX > 10 and mouseX < 60 and mouseY > 10 and mouseY < 60:
        onetwo = 0
    if mouseX > 100 and mouseX < 150  and mouseY > 10 and mouseY < 50:
        one = 212
        two = 32
        three = 188
    
