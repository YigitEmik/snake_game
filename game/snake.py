import turtle as t
COLOR = 'green'
SHAPE = 'square'
MOVE_DISTANCE = 20
        
class Snake():
    def __init__(self):
        #Creates 3 segments for the snake when initialized.
        self.starting_pos = [(0,0), (-20,0), (-40,0)]
        self.segments = []
        for position in self.starting_pos:
            self.create_segment(position)
        self.head = self.segments[0]
        
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)
        self.head.color('lightgreen')
    
    #Creates a new segment
    def create_segment(self,position):
        snake = t.Turtle(SHAPE)
        snake.color(COLOR)
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)
        
    #Directions    
    def up(self):
        if self.head.heading() != 270.0:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90.0:
            self.head.setheading(270)
    def right(self):
        if self.head.heading() != 180.0:
            self.head.setheading(0)
    def left(self):
        if self.head.heading() != 0.0:
            self.head.setheading(180)
            
    #Adds a new segment to snake's last segment
    def new_segment(self):
        self.create_segment(self.segments[len(self.segments)-1].pos())
    #Detect collision with tail 
    #(Starts from index 2 because first two segment always close to each other)
    def collision(self):
        for segment in range(2,len(self.segments)-1):
            if self.head.distance(self.segments[segment]) < 10:
                return True
        return False
        
    
        
        