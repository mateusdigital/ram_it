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
