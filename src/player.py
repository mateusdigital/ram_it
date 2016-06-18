##               █      █                                                     ##
##               ████████                                                     ##
##             ██        ██                                                   ##
##            ███  █  █  ███        player.py                                 ##
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
import assets;
import sound;
import input;
from constants import *;



class Player:
    ############################################################################
    ## Init                                                                   ##
    ############################################################################
    def __init__(self):
        #Surface
        self.left_surface  = assets.load_image("cannon.png");
        self.right_surface = pygame.transform.flip(self.left_surface, True, False);
        self.surface       = self.left_surface;

        ## Pos / Size
        self.width  = self.surface.get_width ();
        self.height = self.surface.get_height();

        self.x = PLAYER_START_X - (self.width / 2);
        self.y = (PLAYFIELD_TOP + (PLAYFIELD_BOTTOM - self.height)) / 2;

        ## Movement
        self.speed = 0;

        self.min_y = PLAYFIELD_TOP;
        self.max_y = PLAYFIELD_BOTTOM - self.height;

        ## Cannon
        self.cannon_offset    = (self.width / 2, self.height / 2);
        self.cannon_direction = DIRECTION_LEFT;

        ## HouseKeeping
        self.should_shoot = False;


    ############################################################################
    ## Getters                                                                ##
    ############################################################################
    def get_cannon_direction(self):
        return self.cannon_direction;

    def get_cannon_position(self):
        ## Cannon is not symmetric, so we need adjust the
        ## projectile position a little bit.
        center   = (self.width * 0.5);
        offset_x = (center + PLAYER_CANNON_X_OFFSET);

        if(self.cannon_direction == DIRECTION_LEFT):
            return (self.x - offset_x, self.y + 4);
        else:
            return ((self.x + offset_x + 10), self.y + 4);

    def wants_to_shoot(self):
        return self.should_shoot;


    ############################################################################
    ## Update / Draw                                                          ##
    ############################################################################
    ## Update ##################################################################
    def update(self, dt):
        self._get_input();

        new_y = self.y + (self.speed * dt);

        ## Maintain the player into bounds.
        if  (new_y <= self.min_y): new_y = self.min_y;
        elif(new_y >= self.max_y): new_y = self.max_y;

        if(new_y != self.y):
            self.y = new_y;
            y_per = float(self.y - self.min_y) / (self.max_y - self.min_y);
            sound.play_player_sound(y_per);


    ## Draw ####################################################################
    def draw(self, surface):
        surface.blit(self.surface, (self.x, self.y));



    ############################################################################
    ## Private Methods                                                        ##
    ############################################################################
    ## Cannon Direction ########################################################
    def _set_cannon_dir(self, direction):
        ## Same direction - Dont need do anything...
        if(self.cannon_direction == direction):
            return;

        ## Change the direction and adjust the offset
        ## of cannon, so it will be centered everytime.
        self.cannon_direction = direction;

        if(direction == DIRECTION_LEFT):
            self.surface = self.left_surface;
            self.x -= PLAYER_CANNON_X_OFFSET;
        else:
            self.surface = self.right_surface;
            self.x += PLAYER_CANNON_X_OFFSET;


    ## input ###################################################################
    def _get_input(self):
        self.speed = 0;

        ## Movement
        if  (input.is_down(K_UP  )): self.speed = -PLAYER_SPEED;
        elif(input.is_down(K_DOWN)): self.speed = +PLAYER_SPEED;

        ## Cannon
        if  (input.is_down(K_LEFT )): self._set_cannon_dir(DIRECTION_LEFT );
        elif(input.is_down(K_RIGHT)): self._set_cannon_dir(DIRECTION_RIGHT);

        ## Shoot
        self.should_shoot = input.is_down(K_SPACE);

