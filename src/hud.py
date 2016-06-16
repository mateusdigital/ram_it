################################################################################
## Imports                                                                    ##
################################################################################
## Pygame ##
import pygame;
## Game_RamIt ##
from constants import *;
from text      import *;

class Hud:
    ############################################################################
    ## Init                                                                   ##
    ############################################################################
    def __init__(self):
        self._level_text = Text(FONT_NAME, FONT_SIZE,
                                PLAYFIELD_LEFT + 30,
                                PLAYFIELD_TOP  - 70);

        ## Dummy values, we need the size
        ## of font to set it's position correctly
        self._score_text  = Text(FONT_NAME, FONT_SIZE, -1, -1);
        self._lives_text  = Text(FONT_NAME, FONT_SIZE, -1, -1);
        self._status_text = Text(FONT_NAME, FONT_SIZE, -1, -1);

        ## Init the contents of the texts...
        self.set_score (0);
        self.set_lives (0);
        self.set_level (0);
        self.set_state(GAME_STATE_PLAYING);

        ## Set their position correctly.
        size = self._score_text.get_size();
        self._score_text.set_position(PLAYFIELD_CENTER_X - size[0] / 2,
                                      PLAYFIELD_TOP  - 70);

        size = self._lives_text.get_size();
        self._lives_text.set_position(PLAYFIELD_RIGHT - 30 - size[0],
                                      PLAYFIELD_TOP  - 70);



    ############################################################################
    ## Public Methods                                                         ##
    ############################################################################
    def set_state(self, state):
        contents = "";

        if  (state == GAME_STATE_GAME_OVER): contents = "- GAME OVER -";
        elif(state == GAME_STATE_PAUSED   ): contents = "-  PAUSED  - ";
        elif(state == GAME_STATE_VICTORY  ): contents = "-  VICTORY  -";
        elif(state == GAME_STATE_DEFEAT   ): contents = "-  DEFEAT  - ";

        self._status_text.set_contents(contents);

        size = self._status_text.get_size();
        self._status_text.set_position(PLAYFIELD_CENTER_X - size[0] / 2,
                                       PLAYFIELD_BOTTOM + 70);

    def set_score(self, score):
        self._score_text.set_contents("Score: %05d" %(score));

    def set_lives(self, lives):
        self._lives_text.set_contents("Lives: %02d" %(lives));

    def set_level(self, level):
        self._level_text.set_contents("Level: %02d" %(level));


    ############################################################################
    ## Update / Draw                                                          ##
    ############################################################################
    def update(self, dt):
        self._level_text.update(dt);

    def draw(self, surface):
        self._level_text.draw (surface);
        self._score_text.draw (surface);
        self._lives_text.draw (surface);
        self._status_text.draw(surface);


    ############################################################################
    ## Private Methods                                                        ##
    ############################################################################
