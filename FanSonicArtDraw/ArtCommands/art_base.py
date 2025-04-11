import json
import turtle
from turtle import (Screen, Turtle)
import _tkinter
# Open the file.json with the color settings
with open(r'JsonSettings\colors.json') as colors:
    colors_dict = json.load(colors)
    colors_key = tuple(colors_dict)

# Open the file.json with the settings
with open(r'JsonSettings\settings.json') as settings_set:
    settings = json.load(settings_set)

class Base_Logos:
    """A class for drawing logos.
    Parent class for all subsequent classes."""

    def __init__(self,
                 screen: Screen, 
                 stylus: Turtle, 
                 stylus_invisible: Turtle):
        """Three attributes are created to which instances of the class must be passed.
        (screen) -> Accepts a screen from the turtle library for further interaction and drawing.
        (stylus) -> Accepts a turtle for drawing, simply put, it accepts stylus.
        (stylus_invisible) -> Accepts a turtle for drawing, simply put, it accepts stylus. Which becomes invisible."""
        self.screen = screen
        self.stylus = stylus
        self.stylus_invisible = stylus_invisible
        self.buttons = None
        self.stylus_invisible.hideturtle()

    def set_buttons(self, *arg) -> None:
        """Method for adding buttons."""
        self.buttons = arg

    def reset_command(self) -> None:
        """The command for a normal reset."""
        try:
            #self.screen.bgcolor('white')
            self.stylus_invisible.reset()
            self.stylus_invisible.hideturtle()
            self.stylus_invisible.speed(settings['speed_invisible'])
            self.stylus.reset()
            self.stylus.speed(settings['speed'])
        except (turtle.Terminator,
                _tkinter.TclError,
                turtle.TurtleGraphicsError):
            print('The Turtle window was closed manually.')

    def star_for_log(self, size: int) -> None:
        """An algorithm for drawing a star for a logo.
        A five-point star.
        (size) -> Draws with invisible styluses and assumes the size of a star.
        When entering the size, keep in mind that the star increases automatically by about 1.5x."""
        try:
            self.stylus_invisible.begin_fill()
            for _ in range(5):
                self.stylus_invisible.forward(size)
                self.stylus_invisible.left(72)
                self.stylus_invisible.forward(size)
                self.stylus_invisible.right(144)
            self.stylus_invisible.end_fill()
        except (turtle.Terminator,
                _tkinter.TclError,
                turtle.TurtleGraphicsError):
            print('The Turtle window was closed manually.')
        
    def eggman_logo_background_style(self,
                                     color_stylus: str,
                                     color_bg: str) -> None:

        """Designs an fraction eggman-themed logo.
        Accepts two arguments. The color of the stylus and the color of the background.
        (color_stylus) -> color turtle
        (color_bg) -> color screen background"""
        
        try:
            self.stylus_invisible.color(color_stylus) # Changes the color of the invisible stylus
            self.screen.bgcolor(color_bg) # Changes the background color

            # Moving the invisible stylus
            self.stylus_invisible.penup()
            self.stylus_invisible.goto(0, -150)
            self.stylus_invisible.pendown()

            # Drawing and filling the circle
            self.stylus_invisible.begin_fill()
            self.stylus_invisible.circle(200)
            self.stylus_invisible.end_fill()
            self.stylus_invisible.penup()
            self.stylus_invisible.home()
            self.stylus_invisible.pendown()
        except (turtle.Terminator,
                _tkinter.TclError,
                turtle.TurtleGraphicsError):
            print('The Turtle window was closed manually.')

    def eggman_logo_base(self, color: str) -> None:
        """The function draws the eggman logo, his head outline for the logo, mustache and glasses.
        After applying the function manually, return the stylus to the initial position and the initial degree rotation.
        To help the method: .home()"""
        try:
            # Draws a circle for the logo's face.
            # stylus movements
            self.stylus.penup()
            self.stylus.goto(0, -80)
            self.stylus.pendown()

            # Drawing and filling the circle
            self.stylus.begin_fill()
            self.stylus.color(color)
            self.stylus.circle(140)
            self.stylus.end_fill()

            # Draws a mustache
            # Draws a right mustache        
            # stylus movements
            self.stylus.penup()
            self.stylus.goto(120, 100)
            self.stylus.left(25)
            self.stylus.pendown()
            
            self.stylus.begin_fill() # Fixes the fill
            self.stylus.forward(160) # Draws a straight line as the base for a mustache

            # Mustache drawing algorithm
            # Tagging variable for the algorithm
            distantion_forward: int = 60

            # Starting the cycle for moustache drawing
            for i in range(5):
                self.stylus.right(140)
                self.stylus.forward(distantion_forward)
                self.stylus.left(120)
                self.stylus.forward(distantion_forward)
                if i == 1:
                    distantion_forward -= 30
            else:
                self.stylus.right(120)
                self.stylus.forward(160)
            # End of the algorithm
            self.stylus.end_fill() # Fixes the end and fills it
            
            # Draws a left mustache        
            # stylus movements
            self.stylus.penup()
            self.stylus.goto(-120, 100)
            self.stylus.right(10)
            self.stylus.pendown()
            
            self.stylus.begin_fill() # Fixes the fill
            self.stylus.forward(160) # Draws a straight line as the base for a mustache

            # Mustache drawing algorithm
            # Tagging variable for the algorithm
            distantion_forward: int = 60 #  Returns the previous value

            # Starting the cycle for moustache drawing
            for i in range(5):
                self.stylus.left(140)
                self.stylus.forward(distantion_forward)
                self.stylus.right(120)
                self.stylus.forward(distantion_forward)
                if i == 1:
                    distantion_forward -= 30
            else:
                self.stylus.left(120)
                self.stylus.forward(160)
            # End of the algorithm
            self.stylus.end_fill() # Fixes the end and fills it

            # Draws glasses
            # Draws right eyecup
            # stylus movements
            self.stylus.penup()
            self.stylus.goto(80, 170)
            self.stylus.left(27)
            self.stylus.pendown()
            
            self.stylus.begin_fill() # Fixes the fill
            self.stylus.forward(30) # Draws a straight line as the base for a eyecup

            # Mustache glasses algorithm
            # Tagging variable for the algorithm        
            degree_of_line: int = 93

            # Starting the cycle for drawing an eyecup
            for _ in range(2):
                self.stylus.left(degree_of_line)
                self.stylus.forward(45)
                degree_of_line -= 7
            # End of the algorithm
            self.stylus.end_fill() # Fixes the end and fills it
            
            # Draws right eyecup
            # stylus movements
            self.stylus.penup()
            self.stylus.goto(-80, 170)
            self.stylus.right(90)
            self.stylus.pendown()

    
            self.stylus.begin_fill() # Fixes the fill
            self.stylus.forward(30) # Draws a straight line as the base for a eyecup

            # Mustache glasses algorithm
            # Tagging variable for the algorithm
            degree_of_line: int = 93

            # Starting the cycle for drawing an eyecup
            for _ in range(2):
                self.stylus.right(degree_of_line)
                self.stylus.forward(45)
                degree_of_line -= 7
            # End of the algorithm
            self.stylus.end_fill() # Fixes the end and fills it
            
            self.stylus.pensize(5) # Changing the line size
            
            # We draw the edging for glasses
            # stylus movements
            self.stylus.penup()
            self.stylus.goto(-65, 195)
            self.stylus.left(90)
            self.stylus.pendown()

            # Draws a part of a circle, a semi-circle for edging glasses
            self.stylus.circle(-100, 90)

            # Restoring the line size
            self.stylus.pensize(1)
        except (turtle.Terminator,
                _tkinter.TclError,
                turtle.TurtleGraphicsError):
            print('The Turtle window was closed manually.')
    
    def sonic_team_bacground_style(self,
                                   color_fill: str,
                                   color_stylus: str,
                                   color_bg: str) -> None:
        
        """The background background is based on the style of the Sonic team
        (color_fill) -> You pass the fill color, and the star fills in.
        (color_stylus) -> Transmitting the color for the line.
        (color_bg) -> Background color.
        """
        try:
            self.screen.bgcolor(color_bg)
            self.stylus_invisible.color(color_stylus,
                                        color_fill)

            
            # The algorithm for placing stars on the sides. And their size.
            star_size: int = 35

            x: int = 120
            y: int = -200

            for _ in range(3):
                self.stylus_invisible.penup()
                self.stylus_invisible.goto(x, y)
                self.stylus_invisible.pendown()
                self.star_for_log(star_size)
                x += 60
                y += 60

            x: int = -190
            y: int = -200

            for _ in range(3):
                self.stylus_invisible.penup()
                self.stylus_invisible.goto(x, y)
                self.stylus_invisible.pendown()
                self.star_for_log(star_size)
                x -= 60
                y += 60
            
            # We draw a rim for the logo
            self.stylus_invisible.color(color_fill)
            self.stylus_invisible.penup()
            self.stylus_invisible.home()
            self.stylus_invisible.goto(-190, 0)
            self.stylus_invisible.pendown()

            self.stylus_invisible.pensize(20)

            self.stylus_invisible.forward(-300)
            self.stylus_invisible.forward(300)
            self.stylus_invisible.left(270)
            
            self.stylus_invisible.circle(200, 180)

            self.stylus_invisible.setheading(0)
            self.stylus_invisible.forward(300)

            # Returns the cursor to its base position
            self.stylus_invisible.penup()
            self.stylus_invisible.home()
            self.stylus_invisible.pendown()
        except (turtle.Terminator,
                _tkinter.TclError,
                turtle.TurtleGraphicsError):
            print('The Turtle window was closed manually.')

    def sonic_team_logo_base_v1(self,
                                color_line_1: str,
                                color_line_2: str,
                                color_line_3: str,
                                color_fill: str) -> None:
        """Draws a special circle for the logo.
        Attention all transmitted colors are used.
        It's just that some of them are used through strings.
        (color_line_1) -> The last line for drawing.
        (color_line_2) -> The central line.
        (color_line_3) -> The final line.
        (color_fill) -> The color for filling the circle.
        """
        try:
            self.stylus.penup()
            self.stylus.goto(-175, -1)
            self.stylus.left(270)
            self.stylus.pendown()
            
            self.stylus.pensize(10)
            self.stylus.color(color_line_3,
                            color_fill)

            self.stylus.begin_fill()
            self.stylus.circle(185)
            self.stylus.end_fill()
            
            # An algorithm for placing multiple circular lines.
            x: int = -165
            size_cricle: int = 175

            for i in range(2, 0, -1):
                self.stylus.penup()
                self.stylus.goto(x, -1)
                self.stylus.pendown()
                self.stylus.color(eval(f'color_line_{i}'))
                self.stylus.circle(size_cricle)
                x += 10
                size_cricle -= 10
        except (turtle.Terminator,
                _tkinter.TclError,
                turtle.TurtleGraphicsError):
            print('The Turtle window was closed manually.')





        


    
    