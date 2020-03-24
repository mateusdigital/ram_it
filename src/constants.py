# coding=utf8
##----------------------------------------------------------------------------##
##               █      █                                                     ##
##               ████████                                                     ##
##             ██        ██                                                   ##
##            ███  █  █  ███        constants.py                              ##
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


START_LEVEL = 1;
START_LIVES = 3;

GAME_STATE_PAUSED        = 0;
GAME_STATE_PLAYING       = 1;
GAME_STATE_VICTORY       = 3;
GAME_STATE_DEFEAT        = 4;
GAME_STATE_GAME_OVER     = 5;

################################################################################
## DIRECTION                                                                  ##
################################################################################
DIRECTION_DOWN  = +1;
DIRECTION_LEFT  = -1;
DIRECTION_NONE  =  0;
DIRECTION_RIGHT = +1;
DIRECTION_UP    = -1;


################################################################################
## GAME                                                                       ##
################################################################################
GAME_FPS = 60;
GAME_FRAME_MS  = (1000.0 / GAME_FPS);
GAME_FRAME_SECS= (1.0    / GAME_FPS);

GAME_WIN_CAPTION       = "Ram It - AmazingCow Labs - v1.2.0";
GAME_WIN_CAPTION_SHORT = "Ram It";
GAME_WIN_WIDTH         = 800;
GAME_WIN_HEIGHT        = 600;
GAME_WIN_SIZE          = (GAME_WIN_WIDTH, GAME_WIN_HEIGHT);


################################################################################
## PLAYFIELD                                                                  ##
################################################################################
PLAYFIELD_LEFT   = 70;
PLAYFIELD_RIGHT  = GAME_WIN_WIDTH  - 70;
PLAYFIELD_CENTER_X = (PLAYFIELD_LEFT + PLAYFIELD_RIGHT) / 2;


################################################################################
## ENEMY                                                                      ##
################################################################################
ENEMIES_LEFT_COUNT  = 15;
ENEMIES_RIGHT_COUNT = 15;
ENEMIES_COUNT       = ENEMIES_LEFT_COUNT + ENEMIES_RIGHT_COUNT;

ENEMIES_LEFT_START_X  = PLAYFIELD_LEFT  + 30;
ENEMIES_RIGHT_START_X = PLAYFIELD_RIGHT - 30;

ENEMY_START_WIDTH = 100;
ENEMY_MAX_WIDTH   = 300;
ENEMY_HEIGHT      =  20;

ENEMY_SPACING = 5;

ENEMY_LEFT_SIDE  = 0;
ENEMY_RIGHT_SIDE = 1;

ENEMY_SHRINK_AMMOUNT = 35;
ENEMY_GROW_AMMOUNT   = 25;

PLAYFIELD_TOP      = 100;
PLAYFIELD_BOTTOM   = PLAYFIELD_TOP + ((ENEMY_HEIGHT * ENEMIES_COUNT / 2) + (ENEMY_SPACING * ENEMIES_COUNT / 2));
PLAYFIELD_CENTER_Y = (PLAYFIELD_TOP + PLAYFIELD_BOTTOM) / 2;


################################################################################
## PLAYER                                                                     ##
################################################################################
PLAYER_CANNON_X_OFFSET  = 8;
PLAYER_SPEED            = 400;
PLAYER_START_X          = (PLAYFIELD_LEFT + PLAYFIELD_RIGHT) / 2;


################################################################################
## PROJECTILE                                                                 ##
################################################################################
PROJECTILE_COLOR = (100, 100, 100);
PROJECTILE_WIDTH  = 15;
PROJECTILE_HEIGHT = 15
PROJECTILE_SIZE   = (PROJECTILE_WIDTH, PROJECTILE_HEIGHT);
PROJECTILE_SPEED  = 1000;


################################################################################
## COLORS                                                                     ##
################################################################################
COLOR_TRANSPARENT = (0, 0, 0, 0);
COLOR_BLACK       = (0, 0, 0);
COLOR_WHITE       = (255, 255, 255);
COLOR_PIPE        = (160, 160, 160);
COLOR_PLAYFIELD   = (162,   98, 33);
import random;
ENEMY_COLOR_INDEX = [];
for i in range(0, 500):
    c = (random.randint(40, 255), random.randint(40, 255), random.randint(40, 255))
    ENEMY_COLOR_INDEX.append(c)


################################################################################
## FONTS                                                                      ##
################################################################################
FONT_NAME = "nokiafc22.ttf";
FONT_SIZE = 17;
