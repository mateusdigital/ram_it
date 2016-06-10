import pygame;

from constants import *;
from log       import *;

################################################################################
##                                                          ##
################################################################################
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

        ##COWTODO: Tune this values.
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
        # log("self_restart");

        self.alive = True;

        self.y = pos_y;
        self.x = pos_x;

        self.speed =  (PROJECTILE_SPEED * dir);


    def kill(self):
        # log("self_kill");
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


