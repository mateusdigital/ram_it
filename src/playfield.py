##               █      █                                                     ##
##               ████████                                                     ##
##             ██        ██                                                   ##
##            ███  █  █  ███        playfield.py                              ##
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
## Game_RamIt
import assets;
from constants import *;



class Playfield:
    ############################################################################
    ## Init                                                                   ##
    ############################################################################
    def __init__(self):
        pipe_size = (8, PLAYFIELD_BOTTOM - PLAYFIELD_TOP + ENEMY_SPACING);

        ## Surface
        self.top_surface    = assets.load_image("playfield_top.png");
        self.bottom_surface = pygame.transform.flip(self.top_surface, False, True);
        self.pipe_surface   = pygame.Surface(pipe_size);
        self.side_surface   = pygame.Surface((
                                    self.top_surface.get_height(),
                                    (PLAYFIELD_BOTTOM - PLAYFIELD_TOP) + ENEMY_SPACING
                              ));

        ## Position
        wcenter            = GAME_WIN_WIDTH * 0.5;
        top_surface_width  = self.top_surface.get_width();
        top_surface_center = top_surface_width * 0.5;
        top_surface_height = self.top_surface.get_height();

        self.top_pos = (wcenter - top_surface_center,
                        PLAYFIELD_TOP - top_surface_height - ENEMY_SPACING);

        self.bottom_pos = (wcenter - top_surface_center,
                           PLAYFIELD_BOTTOM);

        self.pipe_pos = (wcenter - self.pipe_surface.get_width() / 2 + 3,
                         PLAYFIELD_TOP - ENEMY_SPACING);

        self.lside_pos = (self.top_pos[0],
                          self.top_pos[1] + top_surface_height);
        self.rside_pos = (self.top_pos[0] + top_surface_width - top_surface_height,
                          self.top_pos[1] + top_surface_height);


        ## Colorize the surfaces.
        self.pipe_surface.fill(COLOR_PIPE);
        self.side_surface.fill(COLOR_PLAYFIELD);


    ############################################################################
    ## Draw                                                                   ##
    ############################################################################
    def draw(self, surface, draw_pipe=True, draw_side=False):
        surface.blit(self.top_surface,    self.top_pos   );
        surface.blit(self.bottom_surface, self.bottom_pos);

        if(draw_side):
            surface.blit(self.side_surface, self.lside_pos);
            surface.blit(self.side_surface, self.rside_pos);
        if(draw_pipe):
            surface.blit(self.pipe_surface, self.pipe_pos);
