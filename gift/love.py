import turtle
import threading
import time

def move(t,x,y):
	t.pu()
	t.goto(x,y)
	t.pd()

def draw_circle(t1):
	for i in range(200):
		t1.rt(1)
		t1.fd(1)

def draw_love(t1):
	t1.color('purple','red')
	t1.hideturtle()
	t1.pensize(2)
	t1.speed(3)
	move(t1,100,0)
	time.sleep(2)

	t1.begin_fill()
	t1.lt(140)
	t1.fd(112)
	t1.circle(-57.3,200)  # 半径57.3,圆心角200，顺时针转

	t1.lt(120)
	t1.circle(-57.3,200)
	t1.fd(112)
	t1.end_fill()

	draw_word(t1)

def draw_word(t1):
	t1.pensize(5)
	move(t1,50,110)
	time.sleep(1)
	t1.write("Dear XiXi",font=('Segoe Script',18,'normal'))
	move(t1,5,70)
	time.sleep(1)
	t1.write("Happy Birthday",font=('Segoe Script',18,'normal'))
	move(t1, 80, -100)
	time.sleep(3)
	t1.write("Xi Xi",font=(u'方正舒体',22,'normal'))
	move(t1, 50, -150)
	time.sleep(2)
	t1.write("生日快乐~ ~",font=(u'方正舒体',22,'normal'))


def draw_rose(t2):
	t2.speed(10)   #  画笔移动的速度:1<3<6<10<0
	t2.pensize(2)
	t2.hideturtle()
	move(t2,-100,200)
	# 花蕊  
	t2.fillcolor("red")  #填充颜色

	t2.begin_fill()  #开始填充

	t2.circle(10,180)  

	t2.circle(25,110)  

	t2.left(50)  

	t2.circle(60,45)  

	t2.circle(20,170)  

	t2.right(24)  

	t2.fd(30)  

	t2.left(10)  

	t2.circle(30,110)  

	t2.fd(20)  

	t2.left(40)  

	t2.circle(90,70)  

	t2.circle(30,150)  

	t2.right(30)  

	t2.fd(15)  

	t2.circle(80,90)  

	t2.left(15)  

	t2.fd(45)  

	t2.right(165)  

	t2.fd(20)  

	t2.left(155)  

	t2.circle(150,80)  

	t2.left(50)  

	t2.circle(150,90)  

	t2.end_fill()  #结束填充

	   

	# 花瓣1  

	t2.left(150)  

	t2.circle(-90,70)  

	t2.left(20)  

	t2.circle(75,105)  

	t2.setheading(60)  

	t2.circle(80,98)  

	t2.circle(-90,40)  

	  

	# 花瓣2  

	t2.left(180)  

	t2.circle(90,40)  

	t2.circle(-80,98)  

	t2.setheading(-83)  

	  

	# 叶子1  

	t2.fd(30)  

	t2.left(90)  

	t2.fd(25)  

	t2.left(45)  

	t2.fillcolor("green")  

	t2.begin_fill()  

	t2.circle(-80,90)  

	t2.right(90)  

	t2.circle(-80,90)  

	t2.end_fill()  

	   

	t2.right(135)  

	t2.fd(60)  

	t2.left(180)  

	t2.fd(85)  

	t2.left(90)  

	t2.fd(80)  

	   

	# 叶子2  

	t2.right(90)  

	t2.right(45)  

	t2.fillcolor("green")  

	t2.begin_fill()  

	t2.circle(80,90)  

	t2.left(90)  

	t2.circle(80,90)  

	t2.end_fill()  

	   

	t2.left(135)  

	t2.fd(60)  

	t2.left(180)  

	t2.fd(60)  

	t2.right(90)  

	t2.circle(200,50)

def present():
	t1 = turtle.Turtle()
	th1 = threading.Thread(target=draw_love,args=(t1,))
	th1.start()
	t2 = turtle.Turtle()
	th2 = threading.Thread(target=draw_rose,args=(t2,))
	th2.start()

if __name__ == '__main__':
	window = turtle.Screen()
	present()
	window.exitonclick()
