import pgzrun
import time

WIDTH=700
HEIGHT=700
questions=[]
timer = 16
anscorrect = 0
game=True


welcome=Rect(10,10,680,50)
question=Rect(15,85,500,140)
answer1=Rect(15,240,270,140)
answer2=Rect(15,410,270,140)
answer3=Rect(300,240,270,140)
answer4=Rect(300,410,270,140)
skipbutton=Rect(580, 241, 95, 308)
timerbox=Rect(530,85,140,140)
ansbox=[answer1,answer2,answer3,answer4]

def draw():
    screen.fill("black")
    screen.draw.filled_rect(welcome,"black")
    screen.draw.filled_rect(question,"red")
    screen.draw.textbox("Welcome to QuizMaster!", welcome, color="white")
    screen.draw.textbox(Q[0], question, color="white")
    screen.draw.filled_rect(skipbutton, "green")
    screen.draw.textbox("Skip", skipbutton, color="white", angle=90)
    screen.draw.filled_rect(timerbox, "blue")
    screen.draw.textbox(str(timer), timerbox, color="white")
    qnumbers=1
    for box in ansbox:
        screen.draw.filled_rect(box,"#e0e304")
        screen.draw.textbox(Q[qnumbers],box, color="white")
        qnumbers=qnumbers+1


def update():
    movewelcome()

def movewelcome():
    welcome.x=welcome.x-2
    if welcome.x < -620:
        welcome.x=700

def upd():
    global timer
    if timer > 0:
      timer=timer-1 
    else:
        gamover()  

def on_mouse_down(pos):
    boxnumber = 1
    global anscorrect
    for box in ansbox:
        if box.collidepoint(pos):
            if boxnumber == int(Q[5]) and game==True:
                correctans()
                anscorrect=anscorrect+1
                if anscorrect==10:
                    gamwon()
            else:
                gamover()
        boxnumber=boxnumber+1
    
    if skipbutton.collidepoint(pos):
        if questions and game==True:
            correctans()
        else:
            gamwon()    

def correctans():
   global Q
   global timer
   if questions:
      Q=splitting()
      timer=16  

def readquestions():
    global questions
    file=open("quizmastrV.1.5-main/questions.txt", "r")        
    for i in file:
      questions.append(i)

def splitting():
  Q1=questions.pop(0).split(",")
  return Q1

def gamwon():
    global Q
    global timer
    global game
    Q=["Good job on making it to the end! you scored :"+str(anscorrect),"-","-","-","-",2]
    timer=0
    print(anscorrect)
    game=False

def gamover():
    global Q
    global timer
    global game
    Q=["Game over, You scored"+str(anscorrect),"-","-","-","-",3]
    timer=0
    game=False
    

readquestions()     
Q=splitting()
print(Q)
clock.schedule_interval(upd, 1)

pgzrun.go()