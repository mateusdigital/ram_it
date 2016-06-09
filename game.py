################################################################################
## Imports                                                                    ##
################################################################################
## Python ##
import random;
## Pygame ##
import pygame;
from pygame.locals import *;
## Game_RamIt ##
from constants  import *;
from playfield  import *;
from player     import *;
from projectile import *;
from enemy      import *;
from cowclock   import *;
from text       import *;

################################################################################
## Global vars                                                                ##
################################################################################
class Globals:
    draw_surface = None;
    running      = False;

    ## Game Objects
    playfield  = None;
    enemies    = [];
    player     = None;
    projectile = None;

    ## Timers
    enemy_init_timer = None;
    enemy_grow_timer = None;

    ## Game Status
    game_state        = None;
    total_enemy_width = 0;
    total_enemy_alive = 0;

    ## Texts
    status_text = None;


class Input:
    prev_keys = None;
    curr_keys = None;



################################################################################
## Public Functions                                                           ##
################################################################################
## Init ########################################################################
def game_init():
    pygame.init();

    Globals.draw_surface;
    Globals.draw_surface = pygame.display.set_mode(GAME_WIN_SIZE);
    pygame.display.set_caption(GAME_WIN_CAPTION);

    Globals.running = True;

    ## Init the Game Objects.
    _game_init_playfield  ();
    _game_init_enemies    ();
    _game_init_player     ();
    _game_init_projectile ();

    ## Init the Timers
    _game_init_enemy_init_timer ();
    _game_init_enemy_grow_timer ();

    ## Init the Texts.
    _game_init_status_text();

    ## Start the timers.
    Globals.enemy_init_timer.start();



## Quit ########################################################################
def game_quit():
    pygame.quit();


## Run #########################################################################
def game_run():
    frame_start = pygame.time.get_ticks();
    frame_time  = 0;
    while(Globals.running):
        frame_start = pygame.time.get_ticks();

        _game_handle_events();
        _game_update(GAME_FRAME_SECS);

        frame_time = (pygame.time.get_ticks() - frame_start);
        if(frame_time < GAME_FRAME_MS):
            while(1):
                frame_time = (pygame.time.get_ticks() - frame_start);
                if(frame_time >= GAME_FRAME_MS):
                    break;
        else:
            print "MISS FRAME";

        _game_draw();



################################################################################
## Private Functions                                                          ##
################################################################################
## Update ######################################################################
def _game_update(dt):
    Globals.keys = pygame.key.get_pressed();

    #Stuff that update regardless of the Game State.
    Globals.enemy_init_timer.update(dt);
    Globals.status_text.update     (dt);

    if  (Globals.game_state == GAME_STATE_PLAYING  ) : _game_update_playing  (dt);
    elif(Globals.game_state == GAME_STATE_PAUSED   ) : _game_update_paused   (dt);
    elif(Globals.game_state == GAME_STATE_VICTORY  ) : _game_update_victory  (dt);
    elif(Globals.game_state == GAME_STATE_DEFEAT   ) : _game_update_defeat   (dt);
    elif(Globals.game_state == GAME_STATE_GAME_OVER) : _game_update_game_over(dt);


def _game_update_playing(dt):
    #
    player_dir   = DIRECTION_NONE;
    cannon_dir   = Globals.player.get_cannon_direction();
    should_shoot = False;

    ## Get the input...
    if  (Globals.keys[K_UP  ]): player_dir = DIRECTION_UP;
    elif(Globals.keys[K_DOWN]): player_dir = DIRECTION_DOWN;

    if  (Globals.keys[K_LEFT ]): cannon_dir = DIRECTION_LEFT;
    elif(Globals.keys[K_RIGHT]): cannon_dir = DIRECTION_RIGHT;

    if(Globals.keys[K_SPACE]): should_shoot = True;

    #Update Player movement and cannon direction.
    Globals.player.change_movement_direction(player_dir);
    Globals.player.change_cannon_direction  (cannon_dir);

    #Restart the Projectile if needed.
    if(Globals.projectile.is_alive() == False and should_shoot):
        cannon_pos = Globals.player.get_cannon_position();
        Globals.projectile.restart(cannon_pos[0], cannon_pos[1], cannon_dir);


    #Update the game objects and timers.
    Globals.enemy_grow_timer.update(dt);

    Globals.player.update    (dt);
    Globals.projectile.update(dt);


    #Update the game state.
    _game_check_collisions();
    _game_check_status    ();



def _game_update_paused(dt):
    ##COWTODO: Handle the pause state.
    pass;

def _game_update_victory(dt):
    ##COWTODO: Handle the victory state.
    pass;

def _game_update_defeat(dt):
    ##COWTODO: Handle the defeat state.
    pass;

def _game_update_game_over(dt):
    ##COWTODO: Handle the game over state.
    pass;



def _game_change_status_text():
    if(Globals.game_state == GAME_STATE_VICTORY):
        Globals.status_text.set_contents("- VICTORY -");
        Globals.status_text.set_blinking(True);

    elif(Globals.game_state == GAME_STATE_DEFEAT):
        Globals.status_text.set_contents("- DEFEAT -");
        Globals.status_text.set_blinking(True);

    else:
        Globals.status_text.set_contents("Score: 23");
        Globals.status_text.set_blinking(False);


## Draw ########################################################################
def _game_draw():
    ## Clear
    Globals.draw_surface.fill((0, 0, 0));

    ## Draw the game objects.
    Globals.playfield.draw(Globals.draw_surface);

    for enemy in Globals.enemies:
        enemy.draw(Globals.draw_surface);

    Globals.player.draw    (Globals.draw_surface);
    Globals.projectile.draw(Globals.draw_surface);

    Globals.status_text.draw(Globals.draw_surface);

    ## Render
    pygame.display.update();


## Handle Events ###############################################################
def _game_handle_events():
    for event in pygame.event.get():
        if(event.type == pygame.locals.QUIT):
            Globals.running = False;


## Check Collisons #############################################################
def _game_check_collisions():
    ## Projectile is not active - Nothing to do...
    if(not Globals.projectile.is_alive()):
        return;

    projectile_hit_box = Globals.projectile.get_hit_box();

    for enemy in Globals.enemies:
        ## Enemy is already dead...
        if(not enemy.is_alive()):
            continue;

        if(enemy.check_collision(projectile_hit_box)):
            enemy.shrink(ENEMY_SHRINK_AMMOUNT);
            Globals.projectile.kill();

            return;


## Check Status ################################################################
def _game_check_status():
    Globals.total_enemy_alive = ENEMIES_COUNT;
    Globals.total_enemy_width = 0;

    for enemy in Globals.enemies:
        if(not enemy.is_alive()):
            Globals.total_enemy_alive -= 1;
            continue;

        if(enemy.is_max_width()):
            Globals.game_state = GAME_STATE_DEFEAT;
            break;

        Globals.total_enemy_width += enemy.get_width();

    if(Globals.total_enemy_alive == 0):
        Globals.game_state = GAME_STATE_VICTORY;

    _game_change_status_text();


################################################################################
## Inits                                                                      ##
################################################################################
## Playfield ###################################################################
def _game_init_playfield():
    Globals.playfield = Playfield();


## Enemy #######################################################################
def _game_init_enemies():
    Globals.enemies = [];

    Globals.total_enemy_alive = ENEMIES_COUNT;
    Globals.game_state        = GAME_STATE_INITING_ENEMIES;



## Player ######################################################################
def _game_init_player():
    Globals.player = Player(min_y   = PLAYFIELD_TOP,
                            max_y   = PLAYFIELD_BOTTOM,
                            start_x = PLAYER_START_X);


## Projectile ##################################################################
def _game_init_projectile():
    Globals.projectile = Projectile(min_x = PLAYFIELD_LEFT,
                                    max_x = PLAYFIELD_RIGHT);


## Enemy Init Timer ############################################################
def _game_init_enemy_init_timer():
    Globals.enemy_init_timer = CowClock(0.03, ENEMIES_COUNT,
                                        _game_on_enemy_init_timer_tick,
                                        _game_on_enemy_init_timer_done);


## Enemy Grow Timer ############################################################
def _game_init_enemy_grow_timer():
    Globals.enemy_grow_timer = CowClock(0.1,
                                        CowClock.REPEAT_FOREVER,
                                        _game_on_enemy_grow_timer_tick,
                                        None);


## Status Text #################################################################
def _game_init_status_text():
    Globals.status_text = Text("nokiafc22.ttf", 22,
                                100,
                                100,
                                "- PAUSED -");






################################################################################
## Timer Callbacks                                                            ##
################################################################################
## Enemy Init ##################################################################
def _game_on_enemy_init_timer_tick():
    if(Globals.game_state != GAME_STATE_INITING_ENEMIES):
        return;

    enemies_count = len(Globals.enemies);
    enemy_side    = ENEMY_LEFT_SIDE;
    enemy_index   = enemies_count;

    if(enemies_count >= ENEMIES_LEFT_COUNT):
        enemy_side   = ENEMY_RIGHT_SIDE;
        enemy_index -= (ENEMIES_LEFT_COUNT);

    Globals.enemies.append(Enemy_Factory(enemy_side, enemy_index));


def _game_on_enemy_init_timer_done():
    Globals.game_state = GAME_STATE_PLAYING;
    Globals.enemy_grow_timer.start();


## Enemy Grow ##################################################################
def _game_on_enemy_grow_timer_tick():
    if(Globals.game_state != GAME_STATE_PLAYING):
        return;

    while(True):
        index = random.randint(0, len(Globals.enemies) -1);
        if(Globals.enemies[index].get_width() > 0):
            Globals.enemies[index].grow(ENEMY_GROW_AMMOUNT);
            return;
