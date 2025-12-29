import turtle
import math
import random
import time

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Pinball_V1")
wn.setup(width=610,height=610)
images=["Panel.gif","Block.gif","Blocks1.gif","Blocks2.gif"]
[wn.register_shape(i) for i in images]

class Ani(turtle.Turtle):
    def __init__(self, shape):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape(shape)
        self.penup()

class Player(Ani):
    def __init__(self, shape):
        Ani.__init__(self, shape)
        self.goto(0, -280)
        self.score=0
        self.lives=3
    def Lt(self):
        if not(self.xcor()<-255):
            self.setx(self.xcor()-10)      
    def Rt(self):
        if not(self.xcor()>245):
            self.setx(self.xcor()+10)
    
class Border(Ani):
    def __init__(self, shape):
        Ani.__init__(self, shape)
        self.color("white")
        self.goto(290, -320)
        self.pd()
        self.pensize(3)
        self.ht()
        self.goto(290,300)
        self.goto(-300,300)
        self.goto(-300,-320)
        self.goto(-300,280)
        self.goto(290,280)

class Score(Ani):
    def __init__(self, shape):
        Ani.__init__(self, shape)
        self.color("white")
        self.goto(-295, 280)
        self.pd()
        self.pensize(3)
        self.ht()
        self.write("SCORE:{}  LIVES:{}".format(player.score,player.lives), False, align="left", font=("Arial", 12, "normal"))

    def up(self):
        player.score+=10
        self.clear()
        self.write("SCORE:{}  LIVES:{}".format(player.score,player.lives), False, align="left", font=("Arial", 12, "normal"))
    def heart(self):
        player.lives-=1
        self.clear()
        self.write("SCORE:{}  LIVES:{}".format(player.score,player.lives), False, align="left", font=("Arial", 12, "normal"))
    def over(self):
            ball.ht()
            self.clear()
            self.pu()
            self.home()
            self.pd()
            self.write("GAME OVER\nClick to exit", False, align="center", font=("Arial", 24, "normal"))
            

class Ball(Ani):
    def __init__(self, shape):
        Ani.__init__(self, shape)
        self.color("white")
        self.bx=0.4
        self.by=0.4
    def move(self):
        self.x=self.xcor()+self.bx
        self.y=self.ycor()+self.by
        self.goto(self.x,self.y)
        ycoll=math.fabs(self.y-player.ycor())<20
        xcoll=math.fabs(self.x-player.xcor())<42
        if xcoll and ycoll:
            self.by *= (-1)
        if self.xcor()>283 or self.xcor()<-290:
            self.bx *= (-1)
        if self.ycor()>270:
            self.by *= (-1)
        if self.ycor()<-300:
            self.home()
            wn.update()
            score.heart()
            self.by=math.fabs(self.by)
            time.sleep(1)

    def check(self):
        if pin.isvisible():
            acoll=math.fabs(self.y-pin.y)<26
            bcoll=math.fabs(self.x-pin.x)<43
            if acoll and bcoll:
                if math.fabs(self.x-pin.x)-17>math.fabs(self.y-pin.y):
                    self.bx *= (-1)
                else:
                    self.by *= (-1)
                pin.check()
                score.up()

class Obj(Ani):
    def __init__(self, shape):
        Ani.__init__(self, shape)
        self.col=random.choice([("Block.gif",1),("Blocks1.gif",2),("Blocks2.gif",3)])
        self.x=random.randrange(-255,245,80)
        self.y=random.randrange(165,266,25)
        self.arr=(self.x,self.y)
        while self.arr in objarr:
            self.x=random.randrange(-255,245,80)
            self.y=random.randrange(165,266,25)
            self.arr=(self.x,self.y)
        objarr.add(self.arr)
        self.goto(self.x,self.y)
        self.shape(self.col[0])
        self.c=self.col[1] 
    def check(self):
        self.c-=1
        if self.c==0:
            self.ht()
        elif self.c==1:
            self.shape("Block.gif")
        else:
            self.shape("Blocks1.gif")

objarr=set()
player=Player("Panel.gif")
border=Border("triangle")
ball=Ball("circle")
score=Score("triangle")

blocks=10
chat=[Obj("Block.gif") for pin in range(blocks)]

turtle.onkeypress(player.Lt, "Left")
turtle.onkeypress(player.Rt, "Right")

wn.listen()
wn.tracer(0)
while True:
    wn.update()
    ball.move()
    c=0
    for pin in chat:
        ball.check()
        if not(pin.isvisible()):
            c+=1
        if c>blocks-1:
            c=0
            chat.clear()
            chat=[Obj("Block.gif") for pin in range(blocks)]
            ball.home()
            ball.bx+=1
            ball.by+=1
            wn.update()
    if player.lives<1:
        score.over()
        border.clear()
        player.ht()
        ball.ht()
        [pin.ht() for pin in chat]
        wn.update()
        break

wn.exitonclick()
print("Score:",player.score)