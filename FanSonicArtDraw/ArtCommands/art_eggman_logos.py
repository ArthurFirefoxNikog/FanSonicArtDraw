import turtle
import _tkinter
from ArtCommands.art_base import (Base_Logos, colors_dict)

class Eggman_Logos(Base_Logos):

    """A class for drawing the Eggman Empire logo."""

    def eyes_version_1(self, color_eyes: str) -> None:
        """A method for drawing eyes, the eyes version is sinister."""
        try:
            self.stylus.color(color_eyes) # Changing the color of the turtle to white
            
            # stylus movements
            self.stylus.penup() # Raises the stylus
            self.stylus.goto(-90, 110) # Moves it to the (x, y) coordinates
            self.stylus.left(10) # Turns to the left to align the stylus
            self.stylus.pendown() # He lowers the stylus

            self.stylus.begin_fill() # Fixes the fill
            self.stylus.circle(40, 140) # We draw a 140 degree part of the circle and its size is 40
            self.stylus.left(110) # Turn to the left to align the line to finish drawing the eye
            self.stylus.forward(75) # The line to finish drawing the eye
            self.stylus.end_fill() # Fixes the end and fills it
            
            # stylus movements
            self.stylus.penup()
            self.stylus.goto(90, 122) # Moves it to the (90, 122) coordinates
            self.stylus.left(100)
            self.stylus.pendown()

            self.stylus.begin_fill() # Fixes the fill
            self.stylus.circle(-40, 140) # We draw a 140 degree part of the circle and its size is -40
            self.stylus.right(110) # Turn to the right to align the line to finish drawing the eye
            self.stylus.forward(75) # The line to finish drawing the eye
            self.stylus.end_fill() # Fixes the end and fills it
        except (turtle.Terminator,
                _tkinter.TclError,
                turtle.TurtleGraphicsError):
            print('The Turtle window was closed manually.')

    def eyes_version_2(self, color_eyes: str) -> None:
        """The method for drawing eyes, the standard version of the eyes"""
        try:
            self.stylus.color(color_eyes) # Changing the color of the turtle to white
            
            # stylus movements
            self.stylus.penup()
            self.stylus.goto(-90, 110)
            self.stylus.left(10)
            self.stylus.pendown()
            
            # Draws a circle and fills it in
            self.stylus.begin_fill()
            self.stylus.circle(40)
            self.stylus.end_fill()

            # stylus movements
            self.stylus.penup()
            self.stylus.goto(40, 155)
            self.stylus.left(100)
            self.stylus.pendown()

            # Draws a circle and fills it in
            self.stylus.begin_fill()
            self.stylus.circle(-40)
            self.stylus.end_fill()
        except (turtle.Terminator,
                _tkinter.TclError,
                turtle.TurtleGraphicsError):
            print('The Turtle window was closed manually.')

    def nose(self, color_nose: str) -> None:
        """A method for drawing a nose."""
        try:
            self.stylus.color(color_nose)

            # stylus movements
            self.stylus.penup()
            self.stylus.goto(-30, 40)
            self.stylus.right(110)
            self.stylus.pendown()

            # Draws a circle and fills it in
            self.stylus.begin_fill()
            self.stylus.circle(30)
            self.stylus.end_fill()

            self.stylus.hideturtle() # Making the cursor invisible
        except (turtle.Terminator,
                _tkinter.TclError,
                turtle.TurtleGraphicsError):
            print('The Turtle window was closed manually.')

    def logo_smile(self,
                   color_base: str,
                   color_smile: str) -> None:
        """A method that draws a smile."""
        try:
            # Uses the base
            self.eggman_logo_base(color_base)

            # changes color stylus
            self.stylus.color(color_smile)
            
            # stylus movements
            self.stylus.penup()
            self.stylus.goto(-100, 40)
            self.stylus.right(42)
            self.stylus.pendown()

            # Draws a smile without teeth
            self.stylus.begin_fill()
            self.stylus.circle(100, 180)
            self.stylus.left(90)
            self.stylus.forward(202)
            self.stylus.end_fill()

            self.stylus.color(color_base)
            
            # We increase the size of the line to simulate a mustache
            self.stylus.pensize(15) 

            # stylus movements
            self.stylus.penup()
            self.stylus.goto(-115, 25)
            self.stylus.right(145)
            self.stylus.pendown()
            

            self.stylus.forward(40) # Draw a line to simulate

            # stylus movements
            self.stylus.penup()
            self.stylus.goto(115, 25)
            self.stylus.right(-115)
            self.stylus.pendown()

            self.stylus.forward(40) # Draw a line to simulate

            # We change the size of the line to simulate teeth
            self.stylus.pensize(7)
            self.stylus.left(120) # Align the cursor to the bottom

            # An algorithm for arranging lines and imitating teeth
            position_stylus_x: int = -76 # Markers for the cycle
            distantion_forward: int = 90 # Markers for the cycle

            for _ in range(4):
                self.stylus.penup()
                self.stylus.goto(position_stylus_x, 45)
                self.stylus.pendown()
                self.stylus.forward(distantion_forward)

                position_stylus_x += 30
                distantion_forward += 10
            distantion_forward -= 20
            for _ in range(2):
                self.stylus.penup()
                self.stylus.goto(position_stylus_x, 45)
                self.stylus.pendown()
                self.stylus.forward(distantion_forward)

                position_stylus_x += 30
                distantion_forward -= 30
            # End of the algorithm

            self.stylus.pensize(1) # Returning to the original size
        except (turtle.Terminator,
                _tkinter.TclError,
                turtle.TurtleGraphicsError):
            print('The Turtle window was closed manually.')

    def logo_version_1(self) -> None:
        """A method that completely collects ready-made versions of the logo"""
        try:
            # Blocking buttons while drawing so that they do not lead to errors
            for button in self.buttons:
                button.config(state='disabled')
            self.reset_command()
            # Start of assembly
            self.screen.bgcolor(colors_dict['black'])
            self.logo_smile(colors_dict['burgundy'],
                            colors_dict['white'])
            self.eyes_version_1(colors_dict['white'])
            self.nose(colors_dict['burgundy'])
            # Unlocking buttons
            for button in self.buttons:
                button.config(state='normal')
        except (turtle.Terminator,
                _tkinter.TclError,
                turtle.TurtleGraphicsError):
            print('The Turtle window was closed manually.')

    def logo_version_2(self) -> None:
        """A method that completely collects ready-made versions of the logo"""
        try:
            # Blocking buttons while drawing so that they do not lead to errors
            for button in self.buttons:
                button.config(state='disabled')
            self.reset_command()
            # Start of assembly
            self.eggman_logo_background_style(colors_dict['orange'],
                                            colors_dict['burgundy'])
            self.logo_smile(colors_dict['light black'],
                            colors_dict['white'])
            self.eyes_version_2(colors_dict['white'])
            self.nose(colors_dict['light black'])
            # Unlocking buttons
            for button in self.buttons:
                button.config(state='normal')
        except (turtle.Terminator,
                _tkinter.TclError,
                turtle.TurtleGraphicsError):
            print('The Turtle window was closed manually.')

    def logo_version_3(self) -> None:
        """A method that completely collects ready-made versions of the logo"""
        try:
            # Blocking buttons while drawing so that they do not lead to errors
            for button in self.buttons:
                button.config(state='disabled')
            self.reset_command()
            # Start of assembly
            self.eggman_logo_background_style(colors_dict['orange'],
                                            colors_dict['burgundy'])
            self.logo_smile(colors_dict['light black'],
                            colors_dict['white'])
            self.eyes_version_1(colors_dict['white'])
            self.nose(colors_dict['light black'])
            # Unlocking buttons
            for button in self.buttons:
                button.config(state='normal')
        except (turtle.Terminator,
                _tkinter.TclError,
                turtle.TurtleGraphicsError):
            print('The Turtle window was closed manually.')

    def logo_version_4(self) -> None:
        
        """A method that completely collects ready-made versions of the logo"""
        try:
            # Blocking buttons while drawing so that they do not lead to errors
            for button in self.buttons:
                button.config(state='disabled')
            self.reset_command()
            # Start of assembly
            self.screen.bgcolor(colors_dict['black'])
            self.logo_smile(colors_dict['burgundy'],
                            colors_dict['white'])
            self.eyes_version_2(colors_dict['white'])
            self.nose(colors_dict['burgundy'])
            # Unlocking buttons
            for button in self.buttons:
                button.config(state='normal')
        
        except (turtle.Terminator,
                _tkinter.TclError,
                turtle.TurtleGraphicsError):
            print('The Turtle window was closed manually.')


        
