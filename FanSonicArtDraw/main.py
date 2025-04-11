import turtle
import json
import tkinter as tk
from ArtCommands.art_eggman_logos import Eggman_Logos
from ArtCommands.art_team_sonic_logos import Team_Sonic_Logos

def main():
    # Settings
    with open(r'JsonSettings\settings.json') as settings_set:
        settings = json.load(settings_set)

    # Window name
    name_title = 'F.S.A.D.'

    text_button = ('Draw the eggman logo style 1',
                   'Draw the eggman logo style 2',
                   'Draw the eggman logo style 3',
                   'Draw the eggman logo style 4',
                   'Draw the sonic team logo style 1',
                   'Draw the sonic team logo style 2',
                   'Draw the sonic team logo style 3')

    # Create window and title for window.
    screen = turtle.Screen()
    root = screen._root
    screen.title(name_title)
    # Set window size.
    root.geometry(settings['window'])
    root.resizable(False, False)
    screen.setup(width = settings['screen']['width'],
                 height = settings['screen']['height'])
    
    # Installing the icon
    icon = tk.PhotoImage(file='icon.png')
    root.iconphoto(True, icon)

    # Create turtle.
    # The turtle is a cursor for drawing!
    turtl = turtle.Turtle(shape=settings['shape'])
    turtl.speed(settings['speed'])

    turtl_invisible = turtle.Turtle(shape=settings['shape'])
    turtl_invisible.speed(settings['speed_invisible'])

    # Making an instance of the class for logo
    egg_logos = Eggman_Logos(screen, turtl, turtl_invisible)
    team_sonic_logos = Team_Sonic_Logos(screen, turtl, turtl_invisible)

    button_drawing_logo_egg_v1 = tk.Button(root,
                                           text=text_button[0],
                                           command=egg_logos.logo_version_1)
    button_drawing_logo_egg_v1.pack(anchor='nw')
    button_drawing_logo_egg_v2 = tk.Button(root,
                                           text=text_button[1],
                                           command=egg_logos.logo_version_2)
    button_drawing_logo_egg_v2.pack(anchor='nw')
    button_drawing_logo_egg_v3 = tk.Button(root,
                                           text=text_button[2],
                                           command=egg_logos.logo_version_3)
    button_drawing_logo_egg_v3.pack(anchor='nw')
    button_drawing_logo_egg_v4 = tk.Button(root,
                                           text=text_button[3],
                                           command=egg_logos.logo_version_4)
    button_drawing_logo_egg_v4.pack(anchor='nw')
    button_drawing_logo_sonic_team_v1 = tk.Button(root,
                                                  text=text_button[4],
                                                  command=team_sonic_logos.logo_version_1)
    button_drawing_logo_sonic_team_v1.place(x=200, y=696)
    button_drawing_logo_sonic_team_v2 = tk.Button(root,
                                                  text=text_button[5],
                                                  command=team_sonic_logos.logo_version_2)
    button_drawing_logo_sonic_team_v2.place(x=200, y=722)

    egg_logos.set_buttons(button_drawing_logo_egg_v1,
                          button_drawing_logo_egg_v2,
                          button_drawing_logo_egg_v3,
                          button_drawing_logo_egg_v4,
                          button_drawing_logo_sonic_team_v1,
                          button_drawing_logo_sonic_team_v2)
    team_sonic_logos.set_buttons(button_drawing_logo_egg_v1,
                                 button_drawing_logo_egg_v2,
                                 button_drawing_logo_egg_v3,
                                 button_drawing_logo_egg_v4,
                                 button_drawing_logo_sonic_team_v1,
                                 button_drawing_logo_sonic_team_v2)
    
    #turtle.done()

    # Makes sure that the window does not close.
    screen.mainloop()


if __name__ == '__main__':
    main()
