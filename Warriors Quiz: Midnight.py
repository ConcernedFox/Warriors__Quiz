import pgzrun

WIDTH = 870
HEIGHT = 650

Rectangle_1 = Rect((0),(0),(880),(80))
Rectangle_1.move_ip(0,0)

Rectangle_2 = Rect((0),(50),(720),(80))
Rectangle_2.move_ip(0,50)

Rectangle_3 = Rect((755),(100),(80),(80)
Rectangle_3.move_ip(0,0)

Rectangle_4 = Rect((755),(200),(80),400)
Rectangle_4.move_ip(0,0)

Rectangle_5 = Rect((0),(200),(300),(80))
Rectangle_5.move_ip(0,0)

Rectangle_6 = Rect((0),(350),(300),(80))
Rectangle_6.move_ip(0,0)

Rectangle_7 = Rect((350),(200),(300),(80))
Rectangle_7.move_ip(0,0)

Rectangle_8 = Rect((350),(350),(300),(80))
Rectangle_8.move_ip(0,0)

Rectangle_9 = Rect((175),(500),(300),(80))
Rectangle_9.move_ip(0,0)

Score = 0
Time = 10
Question_File = "/Users/puspendra/Pro Game Dev/other_questions.txt"
Display = ""
Game_Over = False

Questions = []
Question_Count = 0
Question_Index = 0


def draw():
    screen.draw.filled_rect(Rectangle_1, "Green" )
    screen.draw.filled_rect(Rectangle_2, "Green" )
    screen.draw.filled_rect(Rectangle_3, "Green" )
    screen.draw.filled_rect(Rectangle_4, "Green" )
    screen.draw.filled_rect(Rectangle_5, "Green" )
    screen.draw.filled_rect(Rectangle_6, "Green" )
    screen.draw.filled_rect(Rectangle_7, "Green" )
    screen.draw.filled_rect(Rectangle_8, "Green" )
    screen.draw.filled_rect(Rectangle_9, "Green" )
    global Display
    Display = "Welcome to Quizmaster"
    screen.draw.textbox(Display, Rectangle_1, color = "Black")

def update():
    move_display_box()

def move_display_box():
    Rectangle_1.x = Rectangle_1.x - 1

pgzrun.go()    