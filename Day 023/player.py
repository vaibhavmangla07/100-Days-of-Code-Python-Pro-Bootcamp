from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
MOVE_DELAY = 100  # ms for smooth long press movement


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)
        self.moving = False

    def go_up(self):
        """Single tap step"""
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    # --- New methods for long press ---
    def start_moving(self):
        if not self.moving:
            self.moving = True
            self.keep_moving()

    def keep_moving(self):
        if self.moving:
            self.forward(MOVE_DISTANCE)
            # use the global screen object (lazy way)
            from turtle import Screen
            screen = Screen()
            screen.ontimer(self.keep_moving, MOVE_DELAY)

    def stop_moving(self):
        self.moving = False
