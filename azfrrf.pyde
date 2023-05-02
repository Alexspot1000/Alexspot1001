slovo1 = ["A","B","O","B","A"]
slovo2 = [u"Х",u"О",u"М",u"Я",u"К"]
def setup():
    textSize(60)
    fullScreen()
    strokeWeight(1)
    
    fill(0,0,255)
    rect(50,50,60,60)# КВ 1
    rect(110,50,60,60)# КВ 2
    rect(170,50,60,60)# КВ 3
    rect(230,50,60,60)# КВ 4
    rect(290,50,60,60)# КВ 5
    fill(0)
    text("eng",370,100)
    fill(0,0,255)
    # СЛЕДУШЕЕ СТРОКИ ЭТО 2 СЛОВО
    rect(50,150,60,60)# КВ 1
    rect(110,150,60,60)# КВ 2
    rect(170,150,60,60)# КВ 3
    rect(230,150,60,60)# КВ 4
    rect(290,150,60,60)# КВ 5
    fill(0)
    text(u"рус",370,200)
    textSize(60)
    fill(255)
def draw():
    global slovo1,slovo2
    if keyPressed:
        if key == slovo1[0]:
            text(slovo1[0],60,100)# Б 1
    if keyPressed:
        if key == slovo1[1]:
            text(slovo1[1],120,100)# Б 2
    if keyPressed:
        if key == slovo1[2]:
            text(slovo1[2],180,100)# Б 3
    if keyPressed:
        if key == slovo1[3]:
            text(slovo1[3],240,100)# Б 4
    if keyPressed:
        if key == slovo1[4]:
            text(slovo1[4],300,100)# Б 5
    if keyPressed:
        if key == slovo2[0]:
    # 2 С Б
            text(slovo2[0],60,200)# Б 1
    if keyPressed:
        if key == slovo2[1]:
            text(slovo2[1],120,200)# Б 2
    if keyPressed:
        if key == slovo2[2]:
            text(slovo2[2],170,200)# Б 3
    if keyPressed:
        if key == slovo2[3]:
            text(slovo2[3],240,200)# Б 4
    if keyPressed:
        if key == slovo2[4]:
            text(slovo2[4],300,200)# Б 5
        
        
