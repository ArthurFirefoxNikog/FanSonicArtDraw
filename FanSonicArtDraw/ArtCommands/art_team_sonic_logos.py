import turtle
import _tkinter
from ArtCommands.art_base import (Base_Logos, colors_dict)

class Team_Sonic_Logos(Base_Logos):

    def tails(self) -> None:
        """A method for adding two fox tails to a logo."""
        try:
            self.stylus.penup()
            self.stylus.home()
            self.stylus.pendown()

            self.stylus.pensize(1)
            
            # Choosing the right colors
            self.stylus.color(colors_dict['light black'], colors_dict['orange'])
            
            # Drawing the first tail
            self.stylus.begin_fill()
            self.stylus.right(330)

            self.stylus.circle(270, 40)
            self.stylus.right(20)
            self.stylus.circle(-270, 40)

            self.stylus.left(210)
            self.stylus.circle(270, 40)

            self.stylus.right(20)
            self.stylus.circle(-270, 40)
            self.stylus.circle(-80, 40)
            self.stylus.circle(-40, 40)
            self.stylus.circle(-20, 40)
            self.stylus.right(52)
            self.stylus.end_fill()

            # Moving the stylus to draw the second tail
            self.stylus.penup()
            self.stylus.home()
            self.stylus.goto(-20, 5)
            self.stylus.pendown()

            # We draw the second tail
            self.stylus.begin_fill()
            self.stylus.right(310)

            self.stylus.circle(270, 40)
            self.stylus.right(20)
            self.stylus.circle(-270, 40)

            self.stylus.left(210)
            self.stylus.circle(270, 40)

            self.stylus.right(20)
            self.stylus.circle(-270, 40)
            self.stylus.circle(-80, 40)
            self.stylus.circle(-40, 40)
            self.stylus.circle(-20, 40)
            self.stylus.right(52)
            self.stylus.end_fill()

            # Choosing the right colors
            self.stylus.color(colors_dict['light black'], colors_dict['white'])

            # Moving to decorate the ends of the tail to give them a foxy look
            self.stylus.penup()
            self.stylus.home()
            self.stylus.goto(165, 185)
            self.stylus.pendown()
            
            # Algorithm for coloring the end of the first tail
            self.stylus.begin_fill()
            for _ in range(1, 4):
                self.stylus.right(110)
                self.stylus.forward(20)
                self.stylus.left(110)
                self.stylus.forward(20)
            
            self.stylus.left(74)
            self.stylus.circle(-190, 40)

            self.stylus.left(150)
            self.stylus.circle(190, 40)
            self.stylus.end_fill()

            self.stylus.penup()
            self.stylus.home()
            self.stylus.goto(67, 230)
            self.stylus.pendown()

            # The algorithm for coloring the end of the second tail
            self.stylus.begin_fill()
            for _ in range(1, 3):
                self.stylus.right(80)
                self.stylus.forward(20)
                self.stylus.left(80)
                self.stylus.forward(20)
            self.stylus.left(35)
            self.stylus.forward(20)


            self.stylus.left(58)
            self.stylus.circle(-190, 40)

            self.stylus.left(150)
            self.stylus.circle(200, 40)
            self.stylus.end_fill()

            self.stylus.hideturtle()
        except (turtle.Terminator,
                _tkinter.TclError,
                turtle.TurtleGraphicsError):
            print('The Turtle window was closed manually.')

    def logo_version_1(self) -> None:
        """The finished assembly of the Sonic team logo."""
        try:
            for button in self.buttons:
                button.config(state='disabled')
            self.reset_command()
            self.sonic_team_bacground_style(colors_dict['yellow'],
                                            colors_dict['black'],
                                            colors_dict['dark blue'])
            
            self.sonic_team_logo_base_v1(colors_dict['red'],
                                        colors_dict['blue'],
                                        colors_dict['dark orange'],
                                        colors_dict['black'])
            self.tails()
            for button in self.buttons:
                button.config(state='normal')
        except (turtle.Terminator,
                _tkinter.TclError,
                turtle.TurtleGraphicsError):
            print('The Turtle window was closed manually.')

        
    def logo_version_2(self) -> None:
        """The finished assembly of the Sonic team logo."""
        try:
            for button in self.buttons:
                button.config(state='disabled')
            self.reset_command()
            self.sonic_team_bacground_style(colors_dict['yellow'],
                                            colors_dict['black'],
                                            colors_dict['burgundy'])
            
            self.sonic_team_logo_base_v1(colors_dict['red'],
                                        colors_dict['blue'],
                                        colors_dict['dark orange'],
                                        colors_dict['black'])
            self.tails()
            for button in self.buttons:
                button.config(state='normal')
        except (turtle.Terminator,
                _tkinter.TclError,
                turtle.TurtleGraphicsError):
            print('The Turtle window was closed manually.')