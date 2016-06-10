## Python ##
import random;
## Game_RamIt ##
from enemy      import *;
from projectile import *;
from cowclock   import *;

class EnemyManager:
    ############################################################################
    ## Init                                                                   ##
    ############################################################################
    def __init__(self):
        ## Enemy Objects.
        self.enemies    = [];

        ## Timers.
        self.init_timer = None;
        self.grow_timer = None;

        ## HouseKeeping.
        self.level               = 0;
        self.finished_init       = False;
        self.enemies_alive_count = 0;
        self.enemy_greater_width = 0;
        self.enemies_total_width = 0;


        ## Init the timers
        self.init_timer = CowClock(0.03, ENEMIES_COUNT,
                                   self._on_init_timer_tick,
                                   self._on_init_timer_done);

        self.grow_timer = CowClock(0.5, CowClock.REPEAT_FOREVER,
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
        self.level         = level;
        self.finished_init = False;

        self.enemies_alive_count = ENEMIES_COUNT;
        self.enemy_greater_width = ENEMY_START_WIDTH;
        self.enemies_total_width = ENEMY_START_WIDTH * ENEMIES_COUNT;

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


    def _on_init_timer_done(self):
        self.grow_timer.start();
        self.finished_init = True;
        ## COWTODO: inform game that we are done with the initialization.


    ## Enemy Grow ##############################################################
    def _on_grow_timer_tick(self):
        if(self.get_alive_count() == 0):
            self.grow_timer.stop();
            return;

        while(True):
            index = random.randint(0, len(self.enemies) -1);

            if(self.enemies[index].get_width() > 0):
                ## Make it grow...
                self.enemies[index].grow(ENEMY_GROW_AMMOUNT);
                return;
