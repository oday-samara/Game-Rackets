# import turtle module
import turtle

wind = turtle.Screen() # intialize screen
wind.title('Ping Pong By Samara') # set the title of the window
wind.bgcolor('black') # set the background color of the window
wind.setup(width=800, height=600) # ste the width and height of the window
wind.tracer(0) # stops the window from updating automatically



#madrab1
madrab1 = turtle.Turtle() # intializes turtle object(shape)
madrab1.speed(0) # set the speed of the animation
madrab1.shape('square') #set the speed of the object
madrab1.color('blue') # ste the color of the shape
madrab1.penup() # stretches he shape to meet the size
madrab1.goto(-350, 0) # stops the object from drawing lines
madrab1.shapesize(stretch_wid=5, stretch_len=1) #set the object of the object
#madrab2
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape('square')
madrab2.color('red')
madrab2.penup()
madrab2.goto(350, 0)
madrab2.shapesize(stretch_wid=5, stretch_len=1)
#ball
bool = turtle.Turtle()
bool.speed(0)
bool.shape('square')
bool.color('white')
bool.penup()
bool.goto(0, 0)
bool.dx = 0.3
bool.dy = 0.3

# score
score1=0
score2=0
score = turtle.Turtle()
score.speed(0)
score.color('white')
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write('Player 1: 0 Player 2: 0',align='center',font=('Courier',24,'normal'))

#functions
def madrab1_up():
    y = madrab1.ycor() # get the y coordinate of the madrab1
    y += 20 # set the y to increase be 20
    madrab1.sety(y)# set the y of the madrab1 to the new y coordinate

def madrab1_down():
    y = madrab1.ycor()
    y -= 20# set the y to decrease be 20
    madrab1.sety(y)


def madrab2_up():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)

def madrab2_down():
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y)



# keyboard bindngs
wind.listen() # tell the window to expect kewbord input
wind.onkeypress(madrab1_up, 'w') # the pressing w the function madrab1_up is invoked
wind.onkeypress(madrab1_down, 's')
wind.onkeypress(madrab2_up, 'Up')
wind.onkeypress(madrab2_down, 'Down')

# main game loop
while True:
    wind.update() # updates the screen everytime the loop run

    #move the ball
    bool.setx(bool.xcor() + bool.dx) # bool start at 0 and evrytime loops run -->+0.7 xaxis
    bool.sety(bool.ycor() + bool.dy)

    # border check , top border +300px, bottom border -300px , ball is 2-px
    if bool.ycor() > 290: #if ball is at top border
        bool.sety(290) # set y coordinate + 290
        bool.dy *= -1 # reverse direction , marking +0.7-->0.7

    if bool.ycor() < -290: #if ball is at bottom border
        bool.sety(-290)
        bool.dy *= -1

    if bool.xcor() > 390: # if ball is at right border
        bool.goto(0, 0) # return ball to center
        bool.dx *= -1 # reverse the x direction
        score1 += 1
        score.clear()
        score.write(f'Player 1: {score1} Player 2: {score2}', align='center', font=('Courier', 24, 'normal'))

    if bool.xcor() < -390:# if ball is at left border
        bool.goto(0, 0)
        bool.dx *= -1
        score2 += 1
        score.clear()
        score.write(f'Player 1: {score1} Player 2: {score2}', align='center', font=('Courier', 24, 'normal'))




    #bomb madrab and bool
    if (bool.xcor() > 340 and bool.xcor() < 350) and (bool.ycor() < madrab2.ycor() + 40 and bool.ycor() > madrab2.ycor() -40):
        bool.setx(340)
        bool.dx *= -1

    if (bool.xcor() < -340 and bool.xcor() > -350) and (bool.ycor() < madrab1.ycor() + 40 and bool.ycor() > madrab1.ycor() -40):
        bool.setx(-340)
        bool.dx *= -1



