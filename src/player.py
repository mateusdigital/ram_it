################################################################################
## Imports                                                                    ##
################################################################################
## Pygame ##
import pygame;
from pygame.locals import *;
## Game_RamIt ##
import assets;
from constants import *;
from input     import *;



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
        #COWTODO: Fix this logic...
        if(self.cannon_direction == DIRECTION_LEFT):
            return (self.x - (self.width / 2 + PLAYER_CANNON_X_OFFSET),
                    self.y + 4);
        else:
            return (self.x + (self.width / 2 + (PLAYER_CANNON_X_OFFSET + 10)),
                    self.y + 4);

    def wants_to_shoot(self):
        return self.should_shoot;


    ############################################################################
    ## Update / Draw                                                          ##
    ############################################################################
    ## Update ##################################################################
    def update(self, dt):
        self._get_input();

        self.y += (self.speed * dt);

        ## Maintain the player into bounds.
        if  (self.y <= self.min_y): self.y = self.min_y;
        elif(self.y >= self.max_y): self.y = self.max_y;


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


    ## Input ###################################################################
    def _get_input(self):
        self.speed = 0;

        ## Movement
        if  (Input.is_down(K_UP  )): self.speed = -PLAYER_SPEED;
        elif(Input.is_down(K_DOWN)): self.speed = +PLAYER_SPEED;

        ## Cannon
        if  (Input.is_down(K_LEFT )): self._set_cannon_dir(DIRECTION_LEFT );
        elif(Input.is_down(K_RIGHT)): self._set_cannon_dir(DIRECTION_RIGHT);

        ## Shoot
        self.should_shoot = Input.is_down(K_SPACE);

