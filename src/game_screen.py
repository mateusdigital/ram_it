##               █      █                                                     ##
##               ████████                                                     ##
##             ██        ██                                                   ##
##            ███  █  █  ███        game_screen.py                            ##
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
from pygame.locals import *;
## Game_RamIt ##
import director;
import sound;
import input;
from constants     import *;
from hud           import *;
from player        import *;
from playfield     import *;
from projectile    import *;
from enemy_manager import *;


class GameScreen():
    ############################################################################
    ## Init                                                                   ##
    ############################################################################
    def __init__(self):
        ## Game Objects
        self.playfield       = None;
        self.enemy_mgr       = None;
        self.player          = None;
        self.projectile      = None;
        self.hud             = None;

        ## Game Status
        self.game_state = None;
        self.level      = START_LEVEL;
        self.lives      = START_LIVES;
        self.score      = 0;

        ## Init the objects...
        self.playfield  = Playfield   ();
        self.enemy_mgr  = EnemyManager();
        self.player     = Player      ();
        self.projectile = Projectile  ();
        self.hud        = Hud         ();

        self.level = START_LEVEL;
        self.lives = START_LIVES;

        self._reset();


    ############################################################################
    ## Update                                                                 ##
    ############################################################################
    def update(self, dt):
        ## Playing
        if(self.game_state == GAME_STATE_PLAYING):
            self._update_playing(dt);
        ## Paused
        elif(self.game_state == GAME_STATE_PAUSED):
            self._update_paused(dt);
        ## Victory
        elif(self.game_state == GAME_STATE_VICTORY):
            self._update_victory(dt);
        ## Defeat
        elif(self.game_state == GAME_STATE_DEFEAT):
            self._update_defeat(dt);
        ## GameOver
        elif(self.game_state == GAME_STATE_GAME_OVER):
            self._update_game_over(dt);


    ## Update Playing ##########################################################
    def _update_playing(self, dt):
        ## Check if player wants to pause.
        if(input.is_click(K_p)):
            self.change_state_playing_to_paused();
            return;

        ## Update the Enemies.
        self.enemy_mgr.update(dt);
        if(not self.enemy_mgr.did_finished_init()):
            return;

        ## Update the Player
        self.player.update(dt);

        ## Update the Projectile
        ## Restart the Projectile if needed.
        if(self.projectile.is_alive() == False and self.player.wants_to_shoot()):
            cannon_pos = self.player.get_cannon_position ();
            cannon_dir = self.player.get_cannon_direction();

            self.projectile.restart(cannon_pos[0], cannon_pos[1], cannon_dir);

        self.projectile.update(dt);

        ## Check collisions
        hit = self.enemy_mgr.check_collision(self.projectile);

        ## If player hit an enemy, increment the score...
        if(hit):
            self.score += 1;
            self.hud.set_score(self.score);

        ## Check Game Status
        self._check_status();



    ## Update Paused ###########################################################
    def _update_paused(self, dt):
        if(input.is_click(K_p)):
            self._change_state_paused_to_playing();


    ## Update Victory ##########################################################
    def _update_victory(self, dt):
        if(input.is_click(K_SPACE)):
            self._change_state_victory_to_playing();


    ## Update Defeat ###########################################################
    def _update_defeat(self, dt):
        if(input.is_click(K_SPACE)):
            self._change_state_defeat_to_playing();


    ## Update GameOver #########################################################
    def _update_game_over(self, dt):
        if(input.is_click(K_SPACE)):
            self._change_state_gameover_to_menu_screen();


    ############################################################################
    ## Draw                                                                   ##
    ############################################################################
    def draw(self, surface):
        ## Draw the game objects.
        self.playfield.draw  (surface);
        self.enemy_mgr.draw  (surface);
        self.player.draw     (surface);
        self.projectile.draw (surface);
        self.hud.draw        (surface);



    ############################################################################
    ## State Management                                                       ##
    ############################################################################
    ## Playing - Paused ########################################################
    def _change_state_playing_to_paused(self):
        ## State
        self.game_state = GAME_STATE_PAUSED;
        ## Hud
        self.hud.set_state(self.game_state);

    def _change_state_paused_to_playing(self):
        ## State
        self.game_state = GAME_STATE_PLAYING;
        ## Hud
        self.hud.set_state(self.game_state);


    ## Playing - Defeat ########################################################
    def _change_state_playing_to_defeat(self):
        ## State
        self.game_state = GAME_STATE_DEFEAT;
        ## Hud
        self.hud.set_state(self.game_state);
        self.hud.set_lives(self.lives     );
        ## Projectile
        self.projectile.kill();
        ## Sounds
        sound.play_defeat_sound();


    def _change_state_defeat_to_playing(self):
        self._reset();


    ## Playing - Victory #######################################################
    def _change_state_playing_to_victory(self):
        ## State
        self.game_state = GAME_STATE_VICTORY;
        ## Hud
        self.hud.set_state(self.game_state);
        ## Projectile
        self.projectile.kill();
        ## Sounds
        sound.play_victory_sound();


    def _change_state_victory_to_playing(self):
        self.level += 1;
        self._reset();


    ## Playing - GameOver ######################################################
    def _change_state_playing_to_gameover(self):
        ## State
        self.game_state = GAME_STATE_GAME_OVER;
        ## Hud
        self.hud.set_state(self.game_state);
        self.hud.set_lives(self.lives     );
        ## Projectile
        self.projectile.kill();
        ## Sounds
        sound.play_gameover_sound();


    ## GameOver - SplashScreen #################################################
    def _change_state_gameover_to_menu_screen(self):
        ## Sounds
        sound.stop_all_sounds();
        director.go_to_menu();


    ############################################################################
    ## Helper Functions                                                       ##
    ############################################################################
    ## Check Status ############################################################
    def _check_status(self):
        enemies_alive     = self.enemy_mgr.get_alive_count        ();
        greater_width     = self.enemy_mgr.get_enemy_greater_width();
        reached_max_width = self.enemy_mgr.enemy_reached_max_width();

        ## Player kill every enemy - Victory.
        if(enemies_alive == 0):
            self._change_state_playing_to_victory();
            return;

        ## Any enemy had reached the max width - Continue
        if(not reached_max_width):
            return;

        ## Descrement the lives...
        self.lives -= 1;

        ## An enemy reached the max width and
        ## player had run out of lives - Game Over
        if(self.lives == 0):
            self._change_state_playing_to_gameover();
            return;

        ## An enemy reached the max width
        ## but player has lives yet - Defeat
        self._change_state_playing_to_defeat();


    ## Reset ###################################################################
    def _reset(self):
        ## Sound
        sound.stop_all_sounds();
        ## State
        self.game_state = GAME_STATE_PLAYING;
        ## Hud
        self.hud.set_level(self.level     );
        self.hud.set_state(self.game_state);
        self.hud.set_lives(self.lives     );
        ## Game Objects
        self.enemy_mgr.reset(self.level);
        self.projectile.kill();
