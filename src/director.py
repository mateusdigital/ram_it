# coding=utf8
##----------------------------------------------------------------------------##
##               █      █                                                     ##
##               ████████                                                     ##
##             ██        ██                                                   ##
##            ███  █  █  ███        director.py                               ##
##            █ █        █ █        Game_RamIt                                ##
##             ████████████                                                   ##
##           █              █       Copyright (c) 2016                        ##
##          █     █    █     █      AmazingCow - www.AmazingCow.com           ##
##          █     █    █     █                                                ##
##           █              █       N2OMatt - n2omatt@amazingcow.com          ##
##             ████████████         www.amazingcow.com/n2omatt                ##
##                                                                            ##
##                  This software is licensed as GPLv3                        ##
##                 CHECK THE COPYING FILE TO MORE DETAILS                     ##
##                                                                            ##
##    Permission is granted to anyone to use this software for any purpose,   ##
##   including commercial applications, and to alter it and redistribute it   ##
##               freely, subject to the following restrictions:               ##
##                                                                            ##
##     0. You **CANNOT** change the type of the license.                      ##
##     1. The origin of this software must not be misrepresented;             ##
##        you must not claim that you wrote the original software.            ##
##     2. If you use this software in a product, an acknowledgment in the     ##
##        product IS HIGHLY APPRECIATED, both in source and binary forms.     ##
##        (See opensource.AmazingCow.com/acknowledgment.html for details).    ##
##        If you will not acknowledge, just send us a email. We'll be         ##
##        *VERY* happy to see our work being used by other people. :)         ##
##        The email is: acknowledgment_opensource@AmazingCow.com              ##
##     3. Altered source versions must be plainly marked as such,             ##
##        and must not be misrepresented as being the original software.      ##
##     4. This notice may not be removed or altered from any source           ##
##        distribution.                                                       ##
##     5. Most important, you must have fun. ;)                               ##
##                                                                            ##
##      Visit opensource.amazingcow.com for more open-source projects.        ##
##                                                                            ##
##                                  Enjoy :)                                  ##
##----------------------------------------------------------------------------##

################################################################################
## Imports                                                                    ##
################################################################################
## Pygame ##
import pygame;
from pygame.locals import *;
## Game_RamIt ##
import sound;
import input;
from constants      import *;
from splash_screen  import *;
from menu_screen    import *;
from credits_screen import *;
from game_screen    import *;



################################################################################
## Global vars                                                                ##
################################################################################
class _Globals:
    draw_surface = None;
    running      = False;

    curr_scene = None;
    color      = COLOR_BLACK;


################################################################################
## Public Functions                                                           ##
################################################################################
## Init ########################################################################
def init():
    ## Pre inits
    sound.pre_init ();
    assets.pre_init();

    ## Pygame
    pygame.init();

    ## Setup the icon and caption.
    rawicon = assets.load_image_no_convert("ramit_icon.png");
    pygame.display.set_icon(rawicon);
    pygame.display.set_caption(GAME_WIN_CAPTION, GAME_WIN_CAPTION_SHORT);


    ## Init the Window and Input
    _Globals.draw_surface = pygame.display.set_mode(GAME_WIN_SIZE);
    input.init();


    ## Make the game running.
    _Globals.running = True;

    ## Init the Initial Screen.
    _Globals.curr_scene = SplashScreen();


## Quit ########################################################################
def quit():
    pygame.quit();


## Run #########################################################################
def run():
    clock = pygame.time.Clock()

    while(_Globals.running):
        ## Handle window events...
        for event in pygame.event.get():
            if(event.type == pygame.locals.QUIT):
                _Globals.running = False;

        ## Keep the framerate tidy...
        _update(clock.tick(0) / 1000.0);

        ## Game Draw
        _draw();


## Clear Color #################################################################
def set_clear_color(color):
    _Globals.color = color;


################################################################################
## Scene Management                                                           ##
################################################################################
def go_to_menu():
    _Globals.curr_scene = MenuScreen();

def go_to_game():
    _Globals.curr_scene = GameScreen();

def go_to_credits():
    _Globals.curr_scene = CreditsScreen();


################################################################################
## Update Functions                                                           ##
################################################################################
def _update(dt):
    input.update();
    _Globals.curr_scene.update(dt);


################################################################################
## Draw Functions                                                             ##
################################################################################
def _draw():
    ## Clear
    _Globals.draw_surface.fill(_Globals.color);

    ## Draw
    _Globals.curr_scene.draw(_Globals.draw_surface);

    ## Render
    pygame.display.update();
