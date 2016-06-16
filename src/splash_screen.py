################################################################################
## Imports                                                                    ##
################################################################################
## Pygame ##
import pygame;
## Game_RamIt ##
from constants import *;
from text      import *;



class SplashScreen:
    ############################################################################
    ## Init                                                                   ##
    ############################################################################
    def __init__(self):
        self._ram_it_logo      = pygame.image.load("RamIt_Logo.png");
        self._ram_it_logo_size = self._ram_it_logo.get_size();
        self._ram_it_logo_pos  = (PLAYFIELD_CENTER_X - (self._ram_it_logo_size[0] / 2),
                                  PLAYFIELD_TOP + 20);

        self._logo      = pygame.image.load("AmazingCow_Logo.png");
        self._logo_size = self._logo.get_size();
        self._logo_pos  = (PLAYFIELD_CENTER_X - (self._logo_size[0] / 2),
                           self._ram_it_logo_pos [1] +
                           self._ram_it_logo_size[1] + 40);


        self._amazingcow_text = Text(FONT_NAME, 20, -1, -1);
        self._amazingcow_text.set_contents("www.AMAZINGCOW.com");
        size = self._amazingcow_text.get_size();
        self._amazingcow_text.set_position(PLAYFIELD_CENTER_X - (size[0] / 2),
                                           self._logo_pos [1] +
                                           self._logo_size[1] + 20);


        self._help_text = Text(FONT_NAME, FONT_SIZE + 5, -1, -1);
        self._help_text.set_contents("Help AACD! [www.aacd.org]");
        size = self._help_text.get_size();
        self._help_text.set_position(PLAYFIELD_CENTER_X - (size[0] / 2),
                                     GAME_WIN_HEIGHT - size[1] - 10);


    ############################################################################
    ## Update / Draw                                                          ##
    ############################################################################
    def update(self, dt):
        pass;

    def draw(self, surface):
        surface.blit(self._logo, self._logo_pos);
        surface.blit(self._ram_it_logo, self._ram_it_logo_pos);

        self._help_text.draw(surface);
        self._amazingcow_text.draw(surface);
