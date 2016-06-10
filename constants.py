START_LEVEL = 1;
START_LIVES = 1;

GAME_STATE_PAUSED        = 0;
GAME_STATE_PLAYING       = 1;
GAME_STATE_VICTORY       = 3;
GAME_STATE_DEFEAT        = 4;
GAME_STATE_GAME_OVER     = 5;
GAME_STATE_SPLASH_SCREEN = 6;

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

GAME_WIN_CAPTION = "AmazingCow - RamIt - v0.0.1";
GAME_WIN_WIDTH   = 800;
GAME_WIN_HEIGHT  = 600;
GAME_WIN_SIZE    = (GAME_WIN_WIDTH, GAME_WIN_HEIGHT);


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

ENEMY_SHRINK_AMMOUNT = 30;
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
COLOR_TRANSPARENT = (0,0,0,0);
COLOR_BLACK       = (0, 0, 0);
COLOR_WHITE       = (255, 255, 255);
COLOR_PIPE        = (160, 160, 160);

import random;
c = lambda x: (random.randint(40, 255), random.randint(40, 255), random.randint(40, 255));
ENEMY_COLOR_INDEX = map(c, range(0, 500));


################################################################################
## FONTS                                                                      ##
################################################################################
FONT_NAME = "nokiafc22.ttf";
FONT_SIZE = 17;

################################################################################
## TIMER T                                                         ##
################################################################################
TIMER_ENEMY_BASE_TIME = 0.5;

TIMER_THRESHOLD = [
    #LEVEL 0 - UNUSED.
    [-1000],

    # LEVEL 1
    [15, 10],
    # LEVEL 2
    [20, 15, 10],
    # COWTODO:
    [20, 15, 10],
    # COWTODO:
    [20, 15, 10],
    # COWTODO:
    [20, 15, 10],
    # COWTODO:
    [20, 15, 10],
    # COWTODO:
    [20, 15, 10],
    # COWTODO:
    [20, 15, 10],
    # COWTODO:
    [20, 15, 10],
    # COWTODO:
    [20, 15, 10],
    # COWTODO:
    [20, 15, 10],
    # COWTODO:
    [20, 15, 10],
    # COWTODO:
    [20, 15, 10],
    # COWTODO:
    [20, 15, 10],
    # COWTODO:
    [20, 15, 10],
    # COWTODO:
    [20, 15, 10],
    # COWTODO:
    [20, 15, 10],
    # COWTODO:
    [20, 15, 10],
    # COWTODO:
    [20, 15, 10],
    # COWTODO:
    [20, 15, 10],
    # COWTODO:
    [20, 15, 10],
    # COWTODO:
    [20, 15, 10],
    # COWTODO:
    [20, 15, 10],
]
