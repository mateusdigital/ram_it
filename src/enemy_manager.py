# coding=utf8
##----------------------------------------------------------------------------##
##               █      █                                                     ##
##               ████████                                                     ##
##             ██        ██                                                   ##
##            ███  █  █  ███        enemy_manager.py                          ##
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
## Python ##
import random;
import copy;
## Game_RamIt ##
import sound;
from enemy      import *;
from projectile import *;
from cowclock   import *;
from enemy_info import *;


class EnemyManager:
    ############################################################################
    ## Init                                                                   ##
    ############################################################################
    def __init__(self):
        ## Enemy Objects.
        self.enemies    = [];

        ## Timers.
        self.init_timer               = None;
        self.grow_timer               = None;
        self.timer_speed_up_threshold = [];

        ## HouseKeeping.
        self.level                    = 0;
        self.finished_init            = False;
        self.enemies_alive_count      = 0;
        self.enemy_greater_width      = 0;
        self.enemies_total_width      = 0;
        self.enemy_info               = None;

        ## Init the timers
        self.init_timer = CowClock(0.03, ENEMIES_COUNT,
                                   self._on_init_timer_tick,
                                   self._on_init_timer_done);

        self.grow_timer = CowClock(-1, ## DUMMY VALUE - Set in self.reset.
                                   CowClock.REPEAT_FOREVER,
                                   self._on_grow_timer_tick);


    ############################################################################
    ## Getters                                                                ##
    ############################################################################
    def get_alive_count(self):
        return self.enemies_alive_count;

    def get_enemy_greater_width(self):
        return self.enemy_greater_width;

    def enemy_reached_max_width(self):
        return self.get_enemy_greater_width() >= ENEMY_MAX_WIDTH;

    def did_finished_init(self):
        return self.finished_init;


    ############################################################################
    ## Actions Methods                                                        ##
    ############################################################################
    ## Reset ###################################################################
    def reset(self, level):
        ## Housekeeping....
        self.level         = level;
        self.finished_init = False;

        self.enemies_alive_count = ENEMIES_COUNT;
        self.enemy_greater_width = ENEMY_START_WIDTH;
        self.enemies_total_width = ENEMY_START_WIDTH * ENEMIES_COUNT;

        self.enemy_info = EnemyInfo(level);


        ##Timers
        self.grow_timer.set_time(self.enemy_info.base_timer);
        ## Deep copy because if the player dies we will not speed up again...
        self.timer_speed_up_threshold = copy.deepcopy(self.enemy_info.timer_threshold);

        self.enemies = []; ## Reset all enemies.

        self.grow_timer.stop (); ## Nothing to grow yet..
        self.init_timer.start(); ## Start creating the enemies one by one...



    ## Check Collisions ########################################################
    def check_collision(self, projectile):
        ## Projectile is not active - Nothing to do...
        if(not projectile.is_alive()):
            return False;

        projectile_hit_box = projectile.get_hit_box();

        for enemy in self.enemies:
            ## Enemy is already dead...
            if(not enemy.is_alive()):
                continue;

            ## Projectile collides with enemy.
            ## Shrink the enemy - Kill the projectile.
            if(enemy.check_collision(projectile_hit_box)):
                enemy.shrink(ENEMY_SHRINK_AMMOUNT);
                projectile.kill();

                sound.play_hit_sound(enemy.get_width());
                return True; ## Projectile can hit only one enemy per time.

        return False;


    ############################################################################
    ## Update / Draw                                                          ##
    ############################################################################
    ## Update ##################################################################
    def update(self, dt):
        self.init_timer.update(dt);
        self.grow_timer.update(dt);

        if(not self.finished_init):
            return;

        self.enemy_greater_width = 0;
        self.enemies_alive_count = 0;
        self.enemies_total_width = 0;

        for enemy in self.enemies:
            self.enemies_total_width += enemy.get_width();

            if(enemy.get_width() > self.enemy_greater_width):
                self.enemy_greater_width = enemy.get_width();

            if(enemy.is_alive()):
                self.enemies_alive_count += 1;

        ## Nothing to speed up...
        if(len(self.timer_speed_up_threshold) == 0):
            return;

        if(self.enemies_alive_count == self.timer_speed_up_threshold[0]):
            tick_time = self.grow_timer.get_time() - self.enemy_info.timer_decay;
            self.grow_timer.set_time(tick_time);
            self.timer_speed_up_threshold.pop(0);


    ## Draw ####################################################################
    def draw(self, surface):
        for enemy in self.enemies:
            enemy.draw(surface);


    ############################################################################
    ## Timer Callbacks                                                        ##
    ############################################################################
    ## Enemy Init ##############################################################
    def _on_init_timer_tick(self):
        ## Assume that we creating enemies on left side.
        enemies_count = len(self.enemies);
        enemy_side    = ENEMY_LEFT_SIDE;
        enemy_index   = enemies_count;

        ## Adjust for right side.
        if(enemies_count >= ENEMIES_LEFT_COUNT):
            enemy_side   = ENEMY_RIGHT_SIDE;
            enemy_index -= (ENEMIES_LEFT_COUNT);

        self.enemies.append(Enemy_Factory(enemy_side, enemy_index));
        sound.play_enemy_init_sound(enemies_count);

    def _on_init_timer_done(self):
        self.grow_timer.start();
        self.finished_init = True;


    ## Enemy Grow ##############################################################
    def _on_grow_timer_tick(self):
        if(self.get_alive_count() == 0):
            self.grow_timer.stop();
            return;

        ## The set trick is the grow_timer can be called when
        ## the enemy just died. So, if we keep search for an
        ## alive enemy we will get stuck into an infinite loop.
        ## This way, we ensure that we "touch" all enemies, but
        ## if any of them are alive, we just give up.
        tries_set = set();
        while(True):
            index = random.randint(0, len(self.enemies) -1);
            tries_set.add(index);

            if(self.enemies[index].get_width() > 0):
                ## Make it grow...
                self.enemies[index].grow(ENEMY_GROW_AMMOUNT);
                sound.play_tictac_sound();

                return;



