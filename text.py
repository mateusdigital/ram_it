import pygame;

from constants import *;
from cowclock  import *;

class Text:
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


    def set_contents(self, contents):
        self.contents = contents;


    def set_blinking(self, blink):
        if(blink): self.blink_timer.start();
        else     : self.blink_timer.stop ();


    def update(self, dt):
        self.blink_timer.update(dt);


    def draw(self, surface):
        if(not self.visible):
            text_surface = self.font.render(self.contents, False, self.color);
            surface.blit(text_surface, (self.x, self.y));


    def _on_blink_timer_tick(self):
        self.visible = not self.visible;

