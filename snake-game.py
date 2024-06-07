#importing libraries
import turtle
import random
import time

# Global variables
game_started = False

# Function to start the game
def start_game(x, y):
    global score, delay, game_started, snake, fruit, old_fruit, scoring
    game_started = True

    # Reset score and delay
    score = 0
    delay = 0.1

    # Reset the snake
    snake.goto(0, 0)
    snake.direction = 'stop'

    # Reset the fruit
    fruit.goto(random.randint(-290, 270), random.randint(-240, 240))

    # Clear old fruits
    for f in old_fruit:
        f.hideturtle()
    old_fruit.clear()

    # Reset the scoring display
    scoring.clear()
    scoring.write("Score: {}".format(score), align="center", font=("Courier", 20, "bold"))

    # Hide buttons
    start_button.clear()
    start_button.hideturtle()
    play_again_button.clear()
    play_again_button.hideturtle()
    exit_button.clear()
    exit_button.hideturtle()

    # Set up key bindings
    screen.listen()
    screen.onkeypress(snake_go_up, "Up")
    screen.onkeypress(snake_go_down, "Down")
    screen.onkeypress(snake_go_left, "Left")
    screen.onkeypress(snake_go_right, "Right")

# Function to handle game over
def game_over():
    global game_started
    game_started = False
    scoring.clear()
    scoring.goto(0, 0)
    screen.bgcolor('turquoise')
    scoring.write("GAME OVER\nScore: {}\nClick 'Play Again' or 'Exit'".format(score), align="center", font=("Courier", 25, "bold"))
    play_again_button.showturtle()
    exit_button.showturtle()

# Function to play again
def play_again(x, y):
    play_again_button.hideturtle()
    exit_button.hideturtle()
    screen.clear()
    setup_game()
    start_game(x, y)

# Function to exit the game
def exit_game(x, y):
    turtle.bye()

# Function to setup the game screen and elements
def setup_game():
    global screen, snake, fruit, old_fruit, scoring, start_button, play_again_button, exit_button

    # Creating turtle screen
    screen = turtle.Screen()
    screen.title('SNAKE GAME')
    screen.setup(width=700, height=700)
    screen.tracer(0)
    screen.bgcolor('green')

    # Creating a border for our game
    border = turtle.Turtle()
    border.speed(3)
    border.pensize(4)
    border.penup()
    border.goto(-310, 250)
    border.pendown()
    border.color('red')
    border.forward(600)
    border.right(90)
    border.forward(500)
    border.right(90)
    border.forward(600)
    border.right(90)
    border.forward(500)
    border.penup()
    border.hideturtle()

    # Score
    scoring = turtle.Turtle()
    scoring.speed(0)
    scoring.color("black")
    scoring.penup()
    scoring.hideturtle()
    scoring.goto(0, 300)

    # Snake
    snake = turtle.Turtle()
    snake.speed(4)
    snake.shape('square')
    snake.color("black")
    snake.penup()
    snake.goto(0, 0)
    snake.direction = 'stop'

    # Food
    fruit = turtle.Turtle()
    fruit.speed(0)
    fruit.shape('circle')
    fruit.color('red')
    fruit.penup()
    fruit.goto(30, 30)

    old_fruit = []

    # Start button
    start_button = turtle.Turtle()
    start_button.speed(0)
    start_button.shape('square')
    start_button.color('white')
    start_button.shapesize(stretch_wid=1, stretch_len=7)
    start_button.penup()
    start_button.goto(0, 0)
    start_button.write("Play", align="center", font=("Courier", 20, "bold"))
    start_button.onclick(start_game)

    # Play again button
    play_again_button = turtle.Turtle()
    play_again_button.speed(0)
    play_again_button.shape('square')
    play_again_button.color('blue')
    play_again_button.shapesize(stretch_wid=2, stretch_len=5)
    play_again_button.penup()
    play_again_button.goto(-100, -50)
    play_again_button.hideturtle()
    play_again_button.onclick(play_again)

    # Exit button
    exit_button = turtle.Turtle()
    exit_button.speed(0)
    exit_button.shape('square')
    exit_button.color('red')
    exit_button.shapesize(stretch_wid=2, stretch_len=5)
    exit_button.penup()
    exit_button.goto(100, -50)
    exit_button.hideturtle()
    exit_button.onclick(exit_game)

# Define how to move
def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"

def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"

def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"

def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

# Main loop
def main_loop():
    global game_started
    while True:
        screen.update()
        if game_started:
            # Snake and fruit collisions
            if snake.distance(fruit) < 20:
                x = random.randint(-290, 270)
                y = random.randint(-240, 240)
                fruit.goto(x, y)
                scoring.clear()
                global score, delay
                score += 1
                scoring.write("Score: {}".format(score), align="center", font=("Courier", 20, "bold"))
                delay -= 0.001

                # Creating new_ball
                new_fruit = turtle.Turtle()
                new_fruit.speed(0)
                new_fruit.shape('square')
                new_fruit.color('yellow')
                new_fruit.penup()
                old_fruit.append(new_fruit)

            # Adding ball to snake
            for index in range(len(old_fruit) - 1, 0, -1):
                a = old_fruit[index - 1].xcor()
                b = old_fruit[index - 1].ycor()
                old_fruit[index].goto(a, b)

            if len(old_fruit) > 0:
                a = snake.xcor()
                b = snake.ycor()
                old_fruit[0].goto(a, b)

            snake_move()

            # Snake and border collision
            if snake.xcor() > 280 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() < -240:
                time.sleep(1)
                game_over()

            # Snake collision
            for food in old_fruit:
                if food.distance(snake) < 20:
                    time.sleep(1)
                    game_over()

            time.sleep(delay)

# Setup and start main loop
setup_game()
main_loop()
