import turtle
#Pygame과 달리 Built-in 이므로 바로 import 가능한 모듈
import os

wn = turtle.Screen()
wn.title("PingPong_Demo")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)
#tracer는 윈도우 강제 업데이트를 막아준다 라고 해야하나...게임 실행 속도를 높이는 일종의 트릭이라고 한다.

# Main Game Loop
while True:
    wn.update()

# #Score
score_a = 0
score_b = 0

# #Paddle_A
paddle_a = turtle.Turtle()
paddle_a.speed = 0
paddle_a.shape("square")
paddle_a.color("white")

# #Paddle_B
paddle_b = turtle.Turtle()
paddle_b.speed = 0
paddle_b.shape("square")
paddle_b.color("white")

# Ball