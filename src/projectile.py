# coding=utf8
##----------------------------------------------------------------------------##
##               █      █                                                     ##
##               ████████                                                     ##
##             ██        ██                                                   ##
##            ███  █  █  ███        projectile.py                             ##
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
## Game_RamIt ##
import sound;
from constants import *;



class Projectile:
    ############################################################################
    ## Init                                                                   ##
    ############################################################################
    def __init__(self):
        ## Surface
        self.surface = pygame.Surface(PROJECTILE_SIZE);
        self.surface.fill(PROJECTILE_COLOR);

        ## Position
        self.x = 0;
        self.y = 0;

        ## Movement
        self.speed = 0;

        ## THIS VALUES ARE NOT EXACTLY -
        ## THE PROJECTILE SPEED IS TOO GREAT I.E IT WILL MOVE
        ## TOO MUCH EACH FRAME. SO WE DON'T HAVE PIXEL PERFECT
        ## BOUNDS HERE BUT THAT'S OK!!!!
        self.min_x = PLAYFIELD_LEFT  + PROJECTILE_WIDTH;
        self.max_x = PLAYFIELD_RIGHT - PROJECTILE_WIDTH;

        ## Status
        self.alive = False;


    ############################################################################
    ## Getters                                                                ##
    ############################################################################
    def is_alive(self):
        return self.alive;

    def get_hit_box(self):
        return (self.x, self.y, PROJECTILE_SIZE[0], PROJECTILE_SIZE[1]);


    ############################################################################
    ## Actions                                                                ##
    ############################################################################
    def restart(self, pos_x, pos_y, dir):
        self.alive = True;

        self.y = pos_y;
        self.x = pos_x;

        self.speed =  (PROJECTILE_SPEED * dir);

        sound.play_shot_sound();

    def kill(self):
        self.alive = False;


    ############################################################################
    ## Update / Draw                                                          ##
    ############################################################################
    ## Update ##################################################################
    def update(self, dt):
        if(not self.alive):
            return;

        self.x += (self.speed * dt);

        ## Maintain the projectile on bounds.
        if(self.x < self.min_x or self.x > self.max_x):
            self.kill();


    ## Draw ####################################################################
    def draw(self, surface):
        if(not self.alive):
            return;

        surface.blit(self.surface, (self.x, self.y));


