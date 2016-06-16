################################################################################
## Imports                                                                    ##
################################################################################
## Pygame ##
import pygame;


class Input:
    ############################################################################
    ## Class vars                                                             ##
    ############################################################################
    prev_keys = None;
    curr_keys = None;


    ############################################################################
    ## Init                                                                   ##
    ############################################################################
    @staticmethod
    def init():
        Input.prev_keys = pygame.key.get_pressed();
        Input.curr_keys = pygame.key.get_pressed();


    ############################################################################
    ## Update                                                                 ##
    ############################################################################
    @staticmethod
    def update():
        Input.prev_keys = Input.curr_keys;
        Input.curr_keys = pygame.key.get_pressed();


    ############################################################################
    ## Key Methods                                                            ##
    ############################################################################
    @staticmethod
    def is_down(key):
        return Input.curr_keys[key];

    @staticmethod
    def is_up(key):
        return not Input.is_down(key);

    @staticmethod
    def was_down(key):
        return Input.prev_keys[key] and Input.is_up(key);

    @staticmethod
    def was_up(key):
        return (not Input.prev_keys[key] and Input.is_down(key));

    @staticmethod
    def is_click(key):
        return Input.is_down(key) and Input.was_up(key);
