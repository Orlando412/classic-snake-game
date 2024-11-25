import turtle #imports turtle
import random



snakeDirections = "up" #sets snake direction
width = 600 #sets width
height = 600 #sets height
delay = 200 #sets delay
offset = { 
  "up": [0, 20],
  "down": [0, -20],
  "left": [-20, 0],
  "right": [20, 0]
} 
foodSize = 10

highScore = 0

try:
  with open("highscore.txt", "r") as file:
    highScore = int(file.read())
except FileNotFoundError:
  pass
  
def updateHighScore():
  global highScore
  if score > highScore:
    highScore = score
    with open("highscore.txt", "w") as file:
      file.write(str(highScore))



def directionKey():
  screen.onkey(lambda: snakeDirection("up"), "Up")
  screen.onkey(lambda: snakeDirection("down"), "Down")
  screen.onkey(lambda: snakeDirection("left"), "Left")
  screen.onkey(lambda: snakeDirection("right"), "Right")

#moves the snake up
def snakeDirection(direction):
  global snakeDirections
  
  if direction == "up" and snakeDirections != "down":
    snakeDirections = direction
  elif direction == "down" and snakeDirections != "up":
    snakeDirections = direction
  elif direction == "left" and snakeDirections != "right":
    snakeDirections = direction
  elif direction == "right" and snakeDirections != "left":
    snakeDirections = direction

def moveSnake():
  t.clearstamps() #clears stamps from the screen

  newHead = snake[-1].copy() #copies the last segment of the snake
  newHead[0] += offset[snakeDirections][0] #moves the snake in the direction of the head
  newHead[1] += offset[snakeDirections][1]

  #checks if the snake is out of bounds
  if newHead in snake or newHead[0] < -width/2 or newHead[0] > width/2 or newHead[1] < -height/2 or newHead[1] > height/2:
    reset()
  else:
    #adds new head to snake
    snake.append(newHead)

    if not foodCollision(): #checks for food collision
      #removes the last segment
      snake.pop(0)

    #draws snake
    for segment in snake:
      t.goto(segment[0], segment[1])
      t.stamp()

    #refreshes screen
    screen.title(f"Score: {score}  High Score: {highScore}")
    screen.update()
    screen.ontimer(moveSnake, delay) #repeats


def getRandomFoodPosition():
  x = random.randint(int(-width / 2 + foodSize), int(width / 2 - foodSize))
  y = random.randint(int(-height / 2 + foodSize), int(height / 2 - foodSize))
  return (x, y)

def foodCollision():
  global foodPosition, score
  if getDistance(snake[-1], foodPosition) < 20:
    score += 1
    updateHighScore()
    foodPosition = getRandomFoodPosition()
    food.goto(foodPosition)
    return True
  
  return False

def reset():
  global snake, snakeDirections, score, foodPosition
  snake = [[0,0], [20,0], [40,0], [60,0], [80,0]]
  snakeDirections = "up"
  score = 0
  foodPosition = getRandomFoodPosition()
  food.goto(foodPosition)
  moveSnake()

def getDistance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1)**2 + (x2 - x1)**2)**0.5
    return distance

#creates window for the drawing 
screen = turtle.Screen()
screen.setup(width, height) #sets window size and dimensions 
screen.title("Base Movement")
screen.bgpic("assets/image.png")
screen.tracer(0) #turns off auto animation

#event handler
screen.listen()
directionKey()

#creates turtle for binding 
t = turtle.Turtle()
t.shape("circle")
t.penup()


food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(foodSize / 20)
food.penup()

reset() #starts the game

turtle.done() #finishes program