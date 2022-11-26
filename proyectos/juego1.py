import turtle
import threading
import time
from playsound import playsound

# area de juego
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#marcador
score_a = 0
score_b = 0

#pantalla a 
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#pala b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#linea divisora
line = turtle.Turtle()
line.speed(0)
line.shape("square")
line.color("gray")
line.shapesize(stretch_wid=30, stretch_len=0.07)
line.penup()
line.goto(0, 0)

#pelota
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.5
static = True

#marcador inicial
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-2.5, 220)
pen.write("0  0", align="center", font=("fixedays", 60, "bold"))

#mensaje "enter"
pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(0, 120)
pen2.write("PRESS ENTER TO START", align="center", font=("fixedsys", 24, "bold"))

#mover pala "a" hacia arriba
def paddle_a_up():
  y = paddle_a.ycor()
  if y <= 240: 
    y += 20
  paddle_a.sety(y)

#mover pala "a" hacia abajo 
def paddle_a_down():
  y = paddle_a.ycor()
  if y >= -220:
    y -= 20
    paddle_a.sety(y)
  
#move para "b" hacia arriba 
def paddle_b_up ():
  y = paddle_b.ycor()
  if y <= 240:
    y += 20
    paddle_b.sety(y)

#reprodución de sonido 
def play_sound():
  play_sound("pong.mp3")

#inicar tarea en segundo plano
def init_playsoun():
  t = threading.Thread(target=play_sound)
  t.start()

#iniciar juego 
def init_game():
  global static
  static = False
  pen2.clear()

#restaurar pantalla de inicio
def reset_screen():
  ball.goto(0, 0)
  ball.dx *= -1
  pen2.write("PRESS ENTER TO START", 
  align="center", font=("fixedsys", 24, "bold"))
  paddle_a.goto(-350, 0)
  paddle_b.goto(350, 0)

  #actualiza marcador
  def update_score():
    pen.clear()
    pen.write("{}    {}".format(score_a,score_b), align="center", font=("fixedsys", 60, "bold"))
  
#registrar eventos de teclado
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_a_up, "Up")
wn.onkeypress(paddle_a_down, "Down")
wn.onkeypress(init_game, "Return")

while True:
    try:
        wn.update()

        #MOVE BALL
        if static == False:
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)

        #BORDER
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            init_playsoun()

        if ball.ycor() < -290:
           ball.sety(-290)
           ball.dy *= -1
           init_playsoun()

        if ball.xcor() > 390:
            score_a += 1
            update_score()
            static = True
            time.sleep(1)
            reset_screen()

        if ball.xcor() < -390:
            score_b += 1
            update_score()
            static = True
            time.sleep(1)
            reset_screen()
            
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
            ball.setx(340)
            ball.dx *= -1
            init_playsoun()

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
            ball.setx(-340)
            ball.dx *= -1        
            init_playsoun()

    except:
        break