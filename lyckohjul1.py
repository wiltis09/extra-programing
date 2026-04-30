from turtle import *
import random
import subprocess
import time
from math import cos, radians, sin


# Make the turtle window update in visible steps instead of only at the end.
tracer(6,6)

# Messages shown on the welcome screen and after each round.
is_clicked = False
welcome_message = "Welcome to the Lucky Wheel game"
start_message = "Click on the screen to begin"
restart_message = "Click on the screen to restart"


# Font styles used for numbers, menu text, and the big result in the center.
number_style = ("Arial", 14, "bold")
message_style = ("Comic Sans MS", 20, "bold")
result_style = ("Comic Sans MS", 60, "bold")

# Basic screen setup for the game window and turtle drawing.
Screen().bgcolor("steelblue")
speed(0)
hideturtle()
colormode(255)

plum_coler_list = [
    "thistle",
    "plum",
    "lightpink",
    "mistyrose",
    "palevioletred",
    "rosybrown"
]

# Color palettes used to give each round a slightly different look.
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


# Neutral accent and built-in macOS sounds used during the game.
black_color = "darkslategray"
tick_sound_path = "/System/Library/Sounds/Tink.aiff"
win_sound_path = "/System/Library/Sounds/Glass.aiff"


def play_sound(sound_path):
    # Play macOS system sounds in the background so the animation keeps running.
    subprocess.Popen(
        ["afplay", sound_path],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def on_click(x_pos, y_pos):
    # Remember that the user clicked so the game can continue.
    global is_clicked
    is_clicked = True


# Register the mouse-click handler for the whole turtle screen.
onscreenclick(on_click)


def wait_for_click():
    global is_clicked

    # Reset the click flag and wait until the player clicks again.
    update()
    is_clicked = False

    # Keep updating the screen until the user clicks.
    while not is_clicked:
        update()
        time.sleep(0.1)

    is_clicked = False





def move_to(pos):
    # Move without drawing a line to the new position.
    penup()
    goto(pos)
    pendown()


def write_number(x_pos, y_pos, value):
    # Write one number label at the correct wheel position.
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
    # Draw expanding decorative circles after the wheel has spun a while.
    ring_radius = 100
    pensize(10)
    setheading(0)

    for _ in range(5):
        ring_radius += 20
        draw_circle(Vec2D(0, -ring_radius), random.choice(vintage_colors_list), ring_radius)

        if ring_radius == 200:
            ring_radius = 80

    pensize(2)


def draw_section(start_angle, section_heading, section_color):
    # Draw one curved divider that separates two wheel sections.
    pencolor(section_color)
    y_pos = sin(radians(start_angle))
    x_pos = cos(radians(start_angle))
    move_to(Vec2D(120 * x_pos, 120 * y_pos))
    setheading(section_heading)
    circle(120, 45)



def draw_circle(pos, color_choice, radius):
    # Draw a full circle at the given position with the chosen color.
    penup()
    color(color_choice)
    goto(pos)
    pendown()
    circle(radius)
    penup()


def clear_screen():
    # Clear all drawings before showing the next screen.
    clear()


# Show the first start screen before the main game loop begins.
speed(0)
move_to(Vec2D(-30, 0))

write(welcome_message, font=message_style, align="center")

move_to(Vec2D(-30, -40))
write(start_message, font=message_style, align="center")
hideturtle()
wait_for_click()
clear_screen()


def start():
    # Pick fresh colors each time the player spins the wheel.
    yellow_color = random.choice(yellow_color_list)
    blue_color = random.choice(blue_color_list)
    red_color = random.choice(red_color_list)
    plum_coler = random.choice(plum_coler_list)

    # Reset the turtle state for a new round.
    pensize(2)
    move_to(Vec2D(0, 0))

    pointer_heading = 0
    selected_slot = random.randrange(1, 9)
    displayed_number = selected_slot

    # Convert the chosen section into the total amount of spin movement.
    total_spin_angle = selected_slot * 45 + 360
    last_tick_angle = -24

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

        # Play a short tick sound every few steps during the spin.
        if current_angle - last_tick_angle >= 24:
            play_sound(tick_sound_path)
            last_tick_angle = current_angle

    pensize(5)
    for pointer_color in [red_color, black_color, black_color, yellow_color]:
        pd()
        color(pointer_color)
        pointer_heading += 90
        setheading(pointer_heading)
        forward(75)

    # Set up the turtle before drawing the wheel outline and labels.
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
    draw_section(67, 157, plum_coler)
    draw_section(157, 247, plum_coler)
    draw_section(247, 337, plum_coler)
    draw_section(337, 67, plum_coler)

    # Draw the eight number labels around the wheel.
    color(0, 0, 0)
    for index in range(0, 24, 3):
        write_number(
            number_positions[index],
            number_positions[index + 1],
            number_positions[index + 2],
        )

    move_to(Vec2D(0, -30))

    # Convert the chosen slot to the final number shown in the center.
    if displayed_number < 8:
        displayed_number = 8 - displayed_number

    # Show the result in the center and play the win sound.
    write(displayed_number, font=result_style, align="center")
    play_sound(win_sound_path)
    ht()
    return "You won number " + str(displayed_number) + "!"


# Keep the game running so the player can restart after each spin.
while True:
    you_won_message = start()
    is_clicked = False

    # Show the restart instructions and the winning message.
    move_to(Vec2D(0, 240))
    write(restart_message, font=message_style, align="center")
    move_to(Vec2D(0, 270))

    write(you_won_message, font=message_style, align="center")
    move_to(Vec2D(-30, 60))
    wait_for_click()
    clear_screen()
    
