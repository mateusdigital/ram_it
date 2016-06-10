################################################################################
##                                                          ##
################################################################################
## Pygame ##
import pygame;
## Game_RamIt
from constants import *;
from log       import *;

################################################################################
##                                                          ##
################################################################################
class Playfield:
    ## Init ####################################################################
    def __init__(self):
        pipe_size = (8, PLAYFIELD_BOTTOM - PLAYFIELD_TOP + ENEMY_SPACING);

        ## Surface
        self.top_surface    = pygame.image.load("playfield_top.png");
        self.bottom_surface = pygame.transform.flip(self.top_surface, False, True);
        self.pipe_surface   = pygame.Surface(pipe_size);


        ## Position
        top_surface_width  = self.top_surface.get_width();
        top_surface_height = self.top_surface.get_height();

        self.top_pos = (GAME_WIN_WIDTH / 2 - top_surface_width / 2,
                        PLAYFIELD_TOP - top_surface_height - ENEMY_SPACING);

        self.bottom_pos = (GAME_WIN_WIDTH / 2 - top_surface_width / 2,
                           PLAYFIELD_BOTTOM);

        self.pipe_pos = (GAME_WIN_WIDTH / 2 - self.pipe_surface.get_width() / 2 + 3,
                         PLAYFIELD_TOP - ENEMY_SPACING);

        ## Colorize the pipe surface.
        self.pipe_surface.fill(COLOR_PIPE);

    ## Draw ####################################################################
    def draw(self, surface, draw_pipe=True):
        surface.blit(self.top_surface,    self.top_pos   );
        surface.blit(self.bottom_surface, self.bottom_pos);
        if(draw_pipe):
            surface.blit(self.pipe_surface, self.pipe_pos);
