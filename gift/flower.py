import math
import turtle

class Flower(object):

	def __init__(self):
		self.window = turtle.Screen()
		self.window.bgcolor('white')
		self.window.title('Draw flower')
		self.pen = turtle.Turtle()
		self.pen.color('red')
		self.pen.shape('turtle')
		self.pen.speed(0)


	def draw(self):
		# 画花瓣
		self.flower(7,60,100,360)
		# 画花梗
		self.pen.color('brown')
		self.pen.rt(90)
		self.pen.fd(100)
		for _ in range(50):
			self.pen.lt(1)
			self.pen.fd(2)
		#画叶子
		self.pen.width(1)
		self.leaf()

	def leaf(self):
		# first leaf
		self.pen.rt(270)
		self.pen.color('green')
		self.__leaf(40,80,180)
		self.pen.rt(140)
		self.pen.color('black')
		self.pen.fd(30)
		self.pen.lt(180)
		self.pen.fd(30)
		# second leaf
		self.pen.rt(120)
		self.pen.color('green')
		self.__leaf(40,80,180)
		self.pen.color('black')
		self.pen.rt(140)
		self.pen.fd(30)
		self.pen.ht()
		self.window.exitonclick()

	
	def __leaf(self,r,angle,p):
		self.pen.begin_fill()
		self.pen.down()
		self.flower(1,r,angle,p)
		self.pen.end_fill()

	def flower(self,n,r,angle,p):
		""" Draw a flower with n petals."""
		for i in range(n):
			self.petal(r,angle)
			self.pen.lt(p/n)

	def petal(self,r,angle):
		"""Draw a petal using two arcs"""
		for i in range(2):
			self.arc(r,angle)
			self.pen.lt(180-angle)

	def arc(self,r,angle):
		"""Draw an arc with the given radius and angle"""
		arc_len = 2*math.pi*r*abs(angle)/360
		n = int(arc_len/4)+1
		step_len = arc_len/n
		step_angle = float(angle)/n
		self.pen.lt(step_angle/2)
		self.p_line(n,step_len,step_angle)
		self.pen.rt(step_angle/2)

	def p_line(self,n,len,angle):
		for i in range(n):
			self.pen.fd(len)
			self.pen.lt(angle)

	def draw_name():
		turtle.bgcolor('black')
		t = turtle.Pen()
		name = turtle.textinput('input','your name:')
		colors = ['red','yellow','purple','blue']
		for i in range(100):
			t.pencolor(colors[i%4])
			t.penup()
			t.fd(i*4)
			t.pendown()
			t.write(name, font=('Arial',int((i+4)/4),'bold'))
			t.lt(90)
if __name__ == '__main__':
	flower = Flower()
	flower.draw()