import turtle
import random
import math
import os

# setup screen
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Simple Python Turtle Graphics Game (Class Version")

turtle.register_shape("heart.gif")
turtle.register_shape("buddy_angry.gif")
turtle.register_shape("buddy_happy.gif")

class Border(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup()
		self.hideturtle()
		self.speed(0)   # animation speed, 0 means fastest.
		self.color("black")
		self.pensize(5)
	def draw_border(self):
		self.penup()
		self.goto(-300,-300)
		self.pendown()
		self.goto(-300,300)
		self.goto(300,300)
		self.goto(300,-300)
		self.goto(-300,-300)


class Player(turtle.Turtle):
	def __init__(self, shape):       #class constructor, setting default of player
		turtle.Turtle.__init__(self)   #initializing the parent class
		self.penup()
		self.speed(0)
		self.shape(shape)
		self.color("white")
		self.speed = 1

	def move(self):
		self.forward(self.speed)

		#border checking
		if self.xcor() > 290 or self.xcor() < -290:
			self.left(60)
		if self.ycor() > 290 or self.ycor() < -290:
			self.left(60)		
	def turnleft(self):
		self.left(30)
	def turnright(self):
		self.right(30)
	def speedup(self):
		self.speed += 1
	def speeddown(self):
		self.speed += -1
	def is_collision(self, object):
		a = self.xcor() - object.xcor()
		b = self.ycor() - object.ycor()
		distance = math.sqrt(a ** 2 + b ** 2)
		if distance < 50:
			return True
		else:
			return False


class Goal(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup()
		self.speed(0)
		self.color("green")
		self.shape("heart.gif")
		self.speed = 3
		self.goto(random.randint(-250,250), random.randint(-250,250))
		self.setheading(random.randint(0,360))
	def move(self):
		self.forward(self.speed)
		#border checking
		if self.xcor() > 280:
			self.left(121)
			self.goto(279, self.ycor())
		if self.xcor() < -280:
			self.left(121)
			self.goto(-279, self.ycor())
		if self.ycor() > 280:
			self.left(121)
			self.goto(self.xcor(), 279)
		if self.ycor() < -280:
			self.left(121)
			self.goto(self.xcor(), -279)

	# def jump(self):
		# self.goto(random.randint(-250,250), random.randint(-250,250))
		# self.setheading(random.randint(0,360))
	def jump(self, object):	
		self.goto(object.xcor() + 100 * math.cos(math.radians(object.heading())), object.ycor() + 100 * math.sin(math.radians(object.heading())))
		self.setheading(object.heading())	

class Game(turtle.Turtle):
	def __init__(self, x, y):
		turtle.Turtle.__init__(self)
		self.penup()
		self.hideturtle()
		self.speed(0)
		self.color("black")
		self.goto(x, y)
		self.score = 0		
	def update_score(self):
		self.clear()
		self.write("Score: {}".format(self.score), False, align="left", font=("Arial", 24, "normal"))
	def change_score(self, points):
		self.score += points
		self.update_score()

#create instance
player = Player("buddy_happy.gif")
player2 = Player("buddy_angry.gif")
border = Border()
game = Game(-290, 310)
game2 = Game(200, 310)
#create multiple goals
goals = []
for i in range(1):
	goals.append(Goal())
	
# draw the border
border.draw_border()
# Set keyboard binding
turtle.listen()
turtle.onkey(player.turnleft, "Left")
turtle.onkey(player.turnright, "Right")
turtle.onkey(player.speedup, "Up")
turtle.onkey(player.speeddown, "Down")
turtle.onkey(player2.turnleft, "a")
turtle.onkey(player2.turnright, "d")
turtle.onkey(player2.speedup, "w")
turtle.onkey(player2.speeddown, "s")

# speed up game
wn.tracer(0)   #stop creen from updated

game.change_score(0)
game2.change_score(0)
#Main loop
while True:
	wn.update()  ## update in the main loop, drawing in offscreen (memory), then update screen.
	player.move()
	player2.move()

	for goal in goals:
		goal.move()
		# check collision
		if player.is_collision(goal):
			goal.jump(player)
			game.change_score(10)
			os.system("afplay bounce.wav &")
		if player2.is_collision(goal):
			goal.jump(player2)
			game2.change_score(10)
			os.system("afplay bounce.wav &")



