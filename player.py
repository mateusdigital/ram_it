import pygame;
from constants import *;


################################################################################
##                                                          ##
################################################################################
class Player:
    ## Init ####################################################################
    def __init__(self, min_y, max_y, start_x):
        #Surface
        self.left_surface  = pygame.image.load("cannon.png");
        self.right_surface = pygame.transform.flip(self.left_surface, True, False);
        self.surface       = self.left_surface;

        ## Pos / Size
        self.width  = self.surface.get_width ();
        self.height = self.surface.get_height();

        self.x = start_x - (self.width / 2);
        self.y = 0;

        ## Movement
        self.speed = 0;

        self.min_y = min_y;
        self.max_y = max_y - self.height;

        ## Cannon
        self.cannon_offset    = (self.width / 2, self.height / 2);
        self.cannon_direction = DIRECTION_LEFT;


    ## Update / Draw ###########################################################
    def update(self, dt):
        self.y += (self.speed * dt);

        ## Maintain the player into bounds.
        if  (self.y <= self.min_y): self.y = self.min_y;
        elif(self.y >= self.max_y): self.y = self.max_y;


    def draw(self, surface):
        surface.blit(self.surface, (self.x, self.y));


    ## #########################################################################
    def change_movement_direction(self, direction):
        self.speed = (direction * PLAYER_SPEED);


    ## Cannon Direction ########################################################
    def change_cannon_direction(self, direction):
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

    def get_cannon_direction(self):
        return self.cannon_direction;


    ## Cannon Position #########################################################
    def get_cannon_position(self):
        #COWTODO: Fix this logic...
        if(self.cannon_direction == DIRECTION_LEFT):
            return (self.x - (self.width / 2 + PLAYER_CANNON_X_OFFSET),
                    self.y + 4);
        else:
            return (self.x + (self.width / 2 + (PLAYER_CANNON_X_OFFSET + 10)),
                    self.y + 4);
