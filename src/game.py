################################################################################
## Imports                                                                    ##
################################################################################
## Pygame ##
import pygame;
from pygame.locals import *;
## Game_RamIt ##
from constants     import *;
from hud           import *;
from input         import *;
from player        import *;
from playfield     import *;
from projectile    import *;
from enemy_manager import *;
from splash_screen import *;



################################################################################
## Global vars                                                                ##
################################################################################
class Globals:
    draw_surface = None;
    running      = False;

    ## Game Objects
    splash_screen = None;
    playfield       = None;
    enemy_mgr       = None;
    player          = None;
    projectile      = None;
    hud             = None;

    ## Game Status
    game_state = None;
    level      = START_LEVEL;
    lives      = START_LIVES;
    score      = 0;



################################################################################
## Public Functions                                                           ##
################################################################################
## Init ########################################################################
def game_init():
    pygame.init();

    # Init the Window.
    Globals.draw_surface;
    Globals.draw_surface = pygame.display.set_mode(GAME_WIN_SIZE);
    pygame.display.set_caption(GAME_WIN_CAPTION);

    ## Init the Input.
    Input.init();

    ## Make the game running.
    Globals.running = True;
    Globals.game_state = GAME_STATE_SPLASH_SCREEN;

    ## Init the game objects
    Globals.splash_screen = SplashScreen ();
    Globals.playfield     = Playfield    ();
    Globals.enemy_mgr     = EnemyManager ();
    Globals.player        = Player       ();
    Globals.projectile    = Projectile   ();
    Globals.hud           = Hud          ();


## Quit ########################################################################
def game_quit():
    pygame.quit();


## Run #########################################################################
def game_run():
    frame_start = pygame.time.get_ticks();
    frame_time  = 0;
    while(Globals.running):
        frame_start = pygame.time.get_ticks();

        ## Handle window events...
        for event in pygame.event.get():
            if(event.type == pygame.locals.QUIT):
                Globals.running = False;

        ## Game Update
        _game_update(GAME_FRAME_SECS);

        ## Keep the framerate tidy...
        frame_time = (pygame.time.get_ticks() - frame_start);
        if(frame_time < GAME_FRAME_MS):
            while(1):
                frame_time = (pygame.time.get_ticks() - frame_start);
                if(frame_time >= GAME_FRAME_MS):
                    break;
        else:
            print "MISS FRAME";

        ## Game Draw
        _game_draw();



################################################################################
## Update Functions                                                           ##
################################################################################
## Update ######################################################################
def _game_update(dt):
    Input.update();

    ## Playing
    if(Globals.game_state == GAME_STATE_PLAYING):
        _game_update_playing(dt);
    ## Paused
    elif(Globals.game_state == GAME_STATE_PAUSED):
        _game_update_paused(dt);
    ## Victory
    elif(Globals.game_state == GAME_STATE_VICTORY):
        _game_update_victory(dt);
    ## Defeat
    elif(Globals.game_state == GAME_STATE_DEFEAT):
        _game_update_defeat(dt);
    ## GameOver
    elif(Globals.game_state == GAME_STATE_GAME_OVER):
        _game_update_game_over(dt);
    ## SplashScreen
    elif(Globals.game_state == GAME_STATE_SPLASH_SCREEN):
        _game_update_splash_screen(dt);


#  Update Playing ##############################################################
def _game_update_playing(dt):
    ## Check if player wants to pause.
    if(Input.is_click(K_p)):
        _game_change_state_playing_to_paused();
        return;

    Globals.enemy_mgr.update(dt);
    if(not Globals.enemy_mgr.did_finished_init()):
        return;

    Globals.player.update(dt);

    ## Restart the Projectile if needed.
    if(Globals.projectile.is_alive() == False and Globals.player.wants_to_shoot()):
        cannon_pos = Globals.player.get_cannon_position ();
        cannon_dir = Globals.player.get_cannon_direction();

        Globals.projectile.restart(cannon_pos[0], cannon_pos[1], cannon_dir);

    Globals.projectile.update(dt);
    hit = Globals.enemy_mgr.check_collision(Globals.projectile);

    ## If player hit an enemy, increment the score...
    if(hit):
        Globals.score += 1;
        Globals.hud.set_score(Globals.score);

    _game_check_status();



## Update Paused ###############################################################
def _game_update_paused(dt):
    if(Input.is_click(K_p)):
        _game_change_state_paused_to_playing();


## Update Victory ##############################################################
def _game_update_victory(dt):
    if(Input.is_click(K_SPACE)):
        _game_change_state_victory_to_playing();


## Update Defeat ###############################################################
def _game_update_defeat(dt):
    if(Input.is_click(K_SPACE)):
        _game_change_state_defeat_to_playing();


## Update GameOver #############################################################
def _game_update_game_over(dt):
    if(Input.is_click(K_SPACE)):
        _game_change_state_gameover_to_splash_screen();


## Update SplashScreen #######################################################
def _game_update_splash_screen(dt):
    if(Input.is_click(K_SPACE)):
        _game_change_state_splash_screen_to_playing();


################################################################################
## Draw Functions                                                             ##
################################################################################
## Draw ########################################################################
def _game_draw():
    ## Clear
    Globals.draw_surface.fill(COLOR_BLACK);

    if(Globals.game_state == GAME_STATE_SPLASH_SCREEN):
        _game_draw_splash_screen();
    else:
        _game_draw_game();

    ## Render
    pygame.display.update();


## Draw Game Over ##############################################################
def _game_draw_splash_screen():
    Globals.playfield.draw(Globals.draw_surface, draw_pipe=False);
    Globals.splash_screen.draw(Globals.draw_surface);


## Draw Game ###################################################################
def _game_draw_game():
    ## Draw the game objects.
    Globals.playfield.draw  (Globals.draw_surface);
    Globals.enemy_mgr.draw  (Globals.draw_surface);
    Globals.player.draw     (Globals.draw_surface);
    Globals.projectile.draw (Globals.draw_surface);
    Globals.hud.draw        (Globals.draw_surface);


################################################################################
## State Management                                                           ##
################################################################################
## Playing - Paused ############################################################
def _game_change_state_playing_to_paused():
    log("GameStateChange: Playing -> Paused");

    Globals.game_state = GAME_STATE_PAUSED;
    Globals.hud.set_state(Globals.game_state);

def _game_change_state_paused_to_playing():
    log("GameStateChange: Paused -> Playing");

    Globals.game_state = GAME_STATE_PLAYING;
    Globals.hud.set_state(Globals.game_state);


## Playing - Defeat ############################################################
def _game_change_state_playing_to_defeat():
    log("GameStateChange: Playing -> Defeat");

    Globals.game_state = GAME_STATE_DEFEAT;
    Globals.hud.set_state(Globals.game_state);
    Globals.hud.set_lives(Globals.lives     );
    Globals.projectile.kill();


def _game_change_state_defeat_to_playing():
    log("GameStateChange: Defeat -> Playing");

    _game_reset();


## Playing - Victory ###########################################################
def _game_change_state_playing_to_victory():
    log("GameStateChange: Playing -> Victory");

    Globals.game_state = GAME_STATE_VICTORY;
    Globals.hud.set_state(Globals.game_state);
    Globals.projectile.kill();


def _game_change_state_victory_to_playing():
    log("GameStateChange: Victory -> Playing");

    Globals.level += 1;
    _game_reset();


## Playing - GameOver ##########################################################
def _game_change_state_playing_to_gameover():
    log("GameStateChange: Playing -> Game Over");

    Globals.game_state = GAME_STATE_GAME_OVER;
    Globals.hud.set_state(Globals.game_state);
    Globals.hud.set_lives(Globals.lives     );
    Globals.projectile.kill();


## GameOver - SplashScreen #####################################################
def _game_change_state_gameover_to_splash_screen():
    log("GameStateChange : GameOver -> SplashScreen");
    Globals.game_state = GAME_STATE_SPLASH_SCREEN;


## SplashScreen - Playing ######################################################
def _game_change_state_splash_screen_to_playing():
    log("GameStateChange : SplashScreen -> Playing");

    Globals.level = START_LEVEL;
    Globals.lives = START_LIVES;

    _game_reset();


################################################################################
## Game Helper Functions                                                      ##
################################################################################
## Check Status ################################################################
def _game_check_status():
    enemies_alive     = Globals.enemy_mgr.get_alive_count        ();
    greater_width     = Globals.enemy_mgr.get_enemy_greater_width();
    reached_max_width = Globals.enemy_mgr.enemy_reached_max_width();

    ## Player kill every enemy - Victory.
    if(enemies_alive == 0):
        _game_change_state_playing_to_victory();
        return;

    ## Any enemy had reached the max width - Continue
    if(not reached_max_width):
        return;

    ## Descrement the lives...
    Globals.lives -= 1;

    ## An enemy reached the max width and
    ## player had run out of lives - Game Over
    if(Globals.lives == 0):
        _game_change_state_playing_to_gameover();
        return;

    ## An enemy reached the max width
    ##  but player has lives yet - Defeat
    _game_change_state_playing_to_defeat();


## Reset #######################################################################
def _game_reset():
    Globals.game_state = GAME_STATE_PLAYING;

    Globals.hud.set_level(Globals.level     );
    Globals.hud.set_state(Globals.game_state);
    Globals.hud.set_lives(Globals.lives     );

    Globals.enemy_mgr.reset(Globals.level);
    Globals.projectile.kill();
