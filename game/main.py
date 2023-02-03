import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

#Create Screen
screen = t.Screen()
screen.setup(width=800, height=800)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)




#Game variables
game_is_on = True
    
def game():
    screen.reset()
    global food, snake, scoretext, game_is_on
    food = Food()
    snake = Snake()
    scoretext = Scoreboard()
    game_is_on = True
    screen.update()
    #Event listener
    screen.listen()
    screen.onkey(snake.up,'Up')
    screen.onkey(snake.down,'Down')
    screen.onkey(snake.left,'Left')
    screen.onkey(snake.right,'Right')
    while game_is_on:
        scoretext.displayScore()
        screen.update()
        time.sleep(0.1)
        snake.move()
        #Collision with food
        if snake.head.distance(food) < 15:
            food.move_food()
            scoretext.score += 1
            snake.new_segment()
            # print(snake.segments)
        #Collision with walls
        if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 380 or snake.head.ycor() < -380:
            game_is_on = False
            scoretext.gameover()
        #Collision with tail
        if snake.collision() == True:
            game_is_on = False
            scoretext.gameover()
        #Restart the game
        if game_is_on == False:
            screen.onkeypress(game,'space')
game()

screen.exitonclick()