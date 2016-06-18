##               █      █                                                     ##
##               ████████                                                     ##
##             ██        ██                                                   ##
##            ███  █  █  ███        enemy.py                                  ##
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
## Python ##
import random;
## Pygame ##
import pygame;
from pygame.locals import *;
## Game_RamIt
from constants import *;



################################################################################
## Factory                                                                    ##
################################################################################
def Enemy_Factory(side, index):
    ## Assume Left and update otherwise...
    enemy_x = ENEMIES_LEFT_START_X;
    if(side == ENEMY_RIGHT_SIDE):
        enemy_x = ENEMIES_RIGHT_START_X;

    enemy_y = PLAYFIELD_TOP + \
              ((ENEMY_HEIGHT * index) + (ENEMY_SPACING * index));

    return Enemy(x = enemy_x,
                 y = enemy_y,
                 start_width = ENEMY_START_WIDTH,
                 color_index = random.randint(0, len(ENEMY_COLOR_INDEX) -1),
                 enemy_side  = side);


################################################################################
## Enemy                                                                      ##
################################################################################
class Enemy:
    ############################################################################
    ## Init                                                                   ##
    ############################################################################
    def __init__(self, x, y,
                 start_width,
                 color_index,
                 enemy_side):

        ## Surface
        self.surface = pygame.Surface((ENEMY_MAX_WIDTH, ENEMY_HEIGHT),
                                      flags=SRCALPHA);

        ## Position
        self.x = x;
        self.y = y;

        ## Side
        self.width = start_width;

        ## Status
        self.enemy_side  = enemy_side;
        self.color_index = color_index;

        ## Complete the initialization.
        if(enemy_side == ENEMY_RIGHT_SIDE):
            self.x -= ENEMY_MAX_WIDTH;

        self.grow(0);


    ############################################################################
    ## Draw                                                                   ##
    ############################################################################
    def draw(self, surface):
        surface.blit(self.surface, (self.x, self.y));


    ############################################################################
    ## Getters                                                                ##
    ############################################################################
    def is_alive(self):
        return self.width > 0;

    def is_max_width(self):
        return self.width >= ENEMY_MAX_WIDTH;

    def get_width(self):
        return self.width;


    ############################################################################
    ## Actions                                                                ##
    ############################################################################
    def grow(self, ammount):
        if(self.width <= 0 or self.width >= ENEMY_MAX_WIDTH):
            return;

        self.width += ammount;
        self._fill_surface();


    def shrink(self, ammount):
        if(self.width <= 0 or self.width >= ENEMY_MAX_WIDTH):
            return;

        self.width -= ammount;
        if(self.width <= 0):
            self.width = 0;

        self._fill_surface();


    def check_collision(self, rect):
        if(not self.is_alive()):
            return False;

        enemy_rect = (0,0,0,0);
        if(self.enemy_side == ENEMY_LEFT_SIDE):
            enemy_rect = pygame.Rect(self.x, self.y,
                                     self.width, ENEMY_HEIGHT);
        else:
            enemy_rect = pygame.Rect(self.x + (ENEMY_MAX_WIDTH - self.width),
                                     self.y,
                                     self.width, ENEMY_HEIGHT);

        return enemy_rect.colliderect(rect);


    ############################################################################
    ## Private Methods                                                        ##
    ############################################################################
    def _clear_surface(self):
        self.surface.fill(COLOR_TRANSPARENT,
                          (0, 0, ENEMY_MAX_WIDTH, ENEMY_HEIGHT));


    def _fill_surface(self):
        self._clear_surface();

        rect_to_fill = (0, 0, 0, 0);

        if(self.enemy_side == ENEMY_LEFT_SIDE):
            rect_to_fill = (0, 0,
                            self.width, ENEMY_HEIGHT);
        else:
            rect_to_fill = (ENEMY_MAX_WIDTH - self.width, 0,
                            ENEMY_MAX_WIDTH, ENEMY_HEIGHT);


        self.surface.fill(ENEMY_COLOR_INDEX[self.color_index],
                          rect_to_fill);
