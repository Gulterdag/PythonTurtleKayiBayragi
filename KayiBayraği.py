import turtle
t=turtle.Turtle()

from turtle import*
title("Kayı Bayrağı")
a=turtle.Screen()
a.bgcolor("blue")
a.setup(width=600,height=400)

def write(message,pos):
  x,y=pos
  t.penup()
  t.goto(x,y)
  t.color("white")
  sytle=("Intro cont black free",200)
  t.write(message,font=sytle)

write("I",(-150,-200))
write("Y",(-75,-200))
write("I",(85,-200))
t.hideturtle()
turtle.done()
