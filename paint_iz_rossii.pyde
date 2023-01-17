bg = 255;

def setup():
    size(600,400)
    background(bg)
    strokeWeight(50)
    
def draw():
    global bg
    #кнопка прямоугольная
    fill(0)
    # левый верхний угол 250 150, размеры 100 на 50
    rect(250,150,100,50) # x от 250 до 250+100, y от 150 до 150 + 50  
    if mousePressed:
        stroke(0)
        point(mouseX,mouseY)
        
    
def mouseClicked():
    global bg
    # если прямоугольная кнопка нажата
    
    if mouseX > 250 and mouseX < 350 and mouseY > 150 and mouseY < 200:
        stroke(0)
        strokeWeight(255)
