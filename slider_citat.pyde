citaty = [u"Люди делятся на две половины. Одни, войдя в комнату, восклицают: О, кого я вижу!; другие: А вот и я!.",u"Люди могут забыть, что вы сказали. Могут забыть, что вы сделали. Но никогда не забудут, что вы заставили их почувствовать..",u"Одна из самых серьёзных потерь — потеря времени.",u"Чтобы было легко потом, нужно пройти через трудности сейчас.",u"За сладкое приходится горько расплачиваться.",u"Люби тех, кто любит тебя.",u"Время утекает сквозь пальцы опущенных рук.",u"Самая большая ошибка — это боязнь совершить ошибку.",u"Не обязательно жить, но обязательно жить счастливо."]
def setup ():
    background(255)
    fullScreen()
    fill(0) 
    textSize(25)
def draw():
    global citaty
    if keyPressed:
        if key == "1":
            background(255)
            textSize(25)
            text(citaty[0],20,350)
    if keyPressed:
        if key == "2":
            background(255)
            textSize(20)
            text(citaty[1],20,350)
    if keyPressed:
        if key == "3":
            background(255)
            textSize(25)
            text(citaty[2],20,350)
    if keyPressed:
        if key == "4":
            background(255)
            textSize(25)
            text(citaty[3],20,350)
    if keyPressed:
        if key == "5":
            background(255)
            textSize(25)
            text(citaty[4],20,350)
    if keyPressed:
        if key == "6":
            background(255)
            textSize(25)
            text(citaty[5],20,350)
    if keyPressed:
        if key == "7":
            background(255)
            textSize(25)
            text(citaty[6],20,350)
    if keyPressed:
        if key == "8":
            background(255)
            textSize(25)
            text(citaty[7],20,350)
    if keyPressed:
        if key == "9":
            background(255)
            textSize(25)
            text(citaty[8],20,350)



    
