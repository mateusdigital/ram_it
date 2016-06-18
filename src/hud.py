# coding=utf8
##----------------------------------------------------------------------------##
##               █      █                                                     ##
##               ████████                                                     ##
##             ██        ██                                                   ##
##            ███  █  █  ███        hud.py                                    ##
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
