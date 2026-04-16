from turtle import *
import random
import time
from math import cos, radians, sin


tracer(6,6)

is_clicked = False
welcome_message = "Welcome to the Lucky Wheel game"
start_message = "Click on the screen to begin"
restart_message = "Click on the screen to restart"

number_style = ("Arial", 14, "bold")
message_style = ("Comic Sans MS", 20, "bold")
result_style = ("Comic Sans MS", 60, "bold")
Screen().bgcolor("steelblue")
speed(0)
ht()
colormode(255)






plum_coler_list = [
    "thistle",
    "plum",
    "lightpink",
    "mistyrose",
    "palevioletred",
    "rosybrown"
]

blue_color_list = [
    "cadetblue",
    "cornflowerblue",
    "slateblue",
    "lightsteelblue",
    "powderblue",
    "navy"
]

red_color_list = [
    "firebrick",
    "indianred",
    "brown",
    "maroon",
    "darkred",
    "rosybrown",
    "sienna",
    "salmon",
    "darksalmon",
    "tomato"
]
yellow_color_list = [
    "goldenrod",
    "darkkhaki",
    "wheat",
    "burlywood",
    "palegoldenrod"
]

vintage_colors_list = [
    "goldenrod", "darkkhaki", "wheat", "burlywood",
    "darkolivegreen", "olivedrab", "darkseagreen", 
    "cadetblue", "slateblue", "lightsteelblue",
    "firebrick", "indianred", "sienna", "maroon",
    "palevioletred", "thistle", "mistyrose"
]


yellow_color = random.choice(yellow_color_list)
blue_color = random.choice(blue_color_list)
red_color = random.choice(red_color_list)
plum_coler = random.choice(plum_coler_list)
black_color = "darkslategray"

def on_click(x_pos, y_pos):
    global is_clicked
    is_clicked = True


onscreenclick(on_click)


def wait_for_click():
    global is_clicked

    update()
    is_clicked = False

    # Keep updating the screen until the user clicks.
    while not is_clicked:
        update()
        time.sleep(0.1)

    is_clicked = False


update()


def move_to(pos):
    pu()
    goto(pos)
    pd()


def write_number(x_pos, y_pos, value):
    move_to(Vec2D(x_pos, y_pos))
    write(value, font=number_style, align="center")




# X position, Y position, and label for each number around the wheel.
number_positions = [
    0, 110, # number 1
    "1",
    87, 70, # number 2
    "2",
    120, -9, # number 3
    "3",
    86, -93, # number 4
    "4",
    0, -130, # number 5
    "5",
    -83, -93, # number 6
    "6",
    -118, -9, # number 7
    "7",
    -85, 70, # number 8
    "8",
]




def draw_ring_effect():
    ring_radius = 100
    pensize(10)
    setheading(0)

    for _ in range(5):
        ring_radius += 20
        draw_circle(Vec2D(0, -ring_radius), random.choice(vintage_colors_list), ring_radius)

        if ring_radius == 200:
            ring_radius = 80

    pensize(2)


def draw_section(start_angle, section_heading):
    pencolor(plum_coler)
    y_pos = sin(radians(start_angle))
    x_pos = cos(radians(start_angle))
    move_to(Vec2D(120 * x_pos, 120 * y_pos))
    setheading(section_heading)
    circle(120, 45)



def draw_circle(pos, color_choice, radius):
    pu()
    color(color_choice)
    goto(pos)
    pd()
    circle(radius)
    pu()


def clear_screen():
    clear()


speed(0)
move_to(Vec2D(-30, 0))

write(welcome_message, font=message_style, align="center")

move_to(Vec2D(-30, -40))
write(start_message, font=message_style, align="center")
hideturtle()
wait_for_click()
clear_screen()
def start():
    yellow_color = random.choice(yellow_color_list)
    blue_color = random.choice(blue_color_list)
    red_color = random.choice(red_color_list)
    plum_coler = random.choice(plum_coler_list)

    pensize(2)
    move_to(Vec2D(0, 0))

    pointer_heading = 0
    
    selected_slot = random.randrange(1, 9, 1)
    total_spin_angle = selected_slot * 45 + 360

    # Spin the pointer with a simple color animation.
    for current_angle in range(6, total_spin_angle, 6):
        pd()
        for pointer_color in [red_color, plum_coler, blue_color,  yellow_color]:
            color(pointer_color)
            pointer_heading += 90
            setheading(pointer_heading)
            forward(75)

        pointer_heading += 6
        setheading(0)

        # Add colorful ring effects after the first full rotation.
        if current_angle > 360:
            draw_ring_effect()
            goto(0, 0)
            setheading(0)

    pensize(5)
    for pointer_color in [red_color, black_color, black_color, yellow_color]:
        pd()
        color(pointer_color)
        pointer_heading += 90
        setheading(pointer_heading)
        forward(75)

    setheading(0)
    move_to(Vec2D(0, 0))
    pensize(15)
    lt(0)

    # Draw the outer wheel circles.
    move_to(Vec2D(0, -120))
    pencolor(red_color)
    circle(120)
    move_to(Vec2D(0, -140))
    pencolor(yellow_color)
    circle(140)
    ht()

    # Draw the four section dividers on the wheel.
    draw_section(67, 157)
    draw_section(157, 247)
    draw_section(247, 337)
    draw_section(337, 67)

    


    color(0, 0, 0)
    for index in range(0, 24, 3):
        write_number(
            number_positions[index],
            number_positions[index + 1],
            number_positions[index + 2],
        )

    move_to(Vec2D(0, -30))

    # Convert the chosen slot to the final number shown in the center.
    if selected_slot < 8:
        selected_slot = 8 - selected_slot

    write(selected_slot, font=result_style, align="center")
    ht()
while True:
    start()
    is_clicked = False
    move_to(Vec2D(0, 240))
    write(restart_message, font=message_style, align="center")
    move_to(Vec2D(-30, 60))
    wait_for_click()
    clear_screen()
    

