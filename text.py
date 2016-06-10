################################################################################
## Imports                                                                    ##
################################################################################
## Pygame ##
import pygame;
## Game_RamIt ##
from constants import *;
from cowclock  import *;


class Text:
    ############################################################################
    ## Init                                                                   ##
    ############################################################################
    def __init__(self,
                 font_name,
                 font_size,
                 x, y,
                 contents = "",
                 color    = COLOR_WHITE):
        ## Font
        self.font = pygame.font.Font(font_name, font_size);

        ## Contents
        self.contents = contents;

        ## Position
        self.x = x;
        self.y = y;

        ## Color
        self.color = color;

        ## Blink timer
        self.visible     = True;
        self.blink_timer = CowClock(0.3, CowClock.REPEAT_FOREVER,
                                    self._on_blink_timer_tick);


    ############################################################################
    ## Public Methods                                                         ##
    ############################################################################
    def set_position(self, x, y):
        self.x = x;
        self.y = y;

    def set_contents(self, contents):
        self.contents = contents;

    def set_blinking(self, blink):
        if(blink): self.blink_timer.start();
        else     : self.blink_timer.stop ();

    def get_size(self, contents = None):
        if(contents == None):
            contents = self.contents;

        return self.font.size(contents);


    ############################################################################
    ## Update / Draw                                                          ##
    ############################################################################
    def update(self, dt):
        self.blink_timer.update(dt);


    def draw(self, surface):
        if(self.visible):
            text_surface = self.font.render(self.contents, False, self.color);
            surface.blit(text_surface, (self.x, self.y));



    ############################################################################
    ## Private Methods                                                        ##
    ############################################################################
    def _on_blink_timer_tick(self):
        self.visible = not self.visible;

