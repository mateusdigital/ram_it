# coding=utf8
##----------------------------------------------------------------------------##
##               █      █                                                     ##
##               ████████                                                     ##
##             ██        ██                                                   ##
##            ███  █  █  ███        sound.py                                  ##
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
## Source Notice:                                                             ##
##                                                                            ##
##  _generateTone function was inspired and hacked from:                      ##
##      pitch perfect by Sean McKean                                          ##
##      https://code.google.com/archive/p/pitch-perfect/                      ##
##                                                                            ##
##  The original copyright notice is represented bellow:                      ##
##                                                                            ##
## generate.py : contains tone-generating function                            ##
##                                                                            ##
## Copyright (C) 2010  Sean McKean                                            ##
##                                                                            ##
## This program is free software: you can redistribute it and/or modify       ##
## it under the terms of the GNU General Public License as published by       ##
## the Free Software Foundation, either version 3 of the License, or          ##
## (at your option) any later version.                                        ##
##                                                                            ##
## This program is distributed in the hope that it will be useful,            ##
## but WITHOUT ANY WARRANTY; without even the implied warranty of             ##
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the              ##
## GNU General Public License for more details.                               ##
##                                                                            ##
## You should have received a copy of the GNU General Public License          ##
## along with this program.  If not, see <http://www.gnu.org/licenses/>.      ##
##                                                                            ##
################################################################################


################################################################################
## Imports                                                                    ##
################################################################################
## Python ##
import sys;
import os;
import random;
## Pygame ##
import pygame;
## NumPy /SciPy ##
import numpy as np;
## Game_RamIt ##
import assets;
from constants import *;


################################################################################
## Constants                                                                  ##
################################################################################
CHANNEL_INDEX_PLAYER = 0;
CHANNEL_INDEX_TICTAC = 1;
CHANNEL_INDEX_SHOT   = 2;
CHANNEL_INDEX_HIT    = 3;
CHANNEL_INDEX_OTHER  = 4;

WAVE_SQUARE = "square";
WAVE_SAW    = "saw";
WAVE_SINE   = "sine";

## Helps the dev - We can set which sound will be allowed to play...
_PLAYER_ENABLED   = True;
_TICTAC_ENABLED   = True;
_SHOT_ENABLED     = True;
_HIT_ENABLED      = True;
_VICTORY_ENABLED  = True;
_DEFEAT_ENABLED   = True;
_GAMEOVER_ENABLED = True;
_ENEMIES_ENABLED  = True;

_VOLUME_HI  = 1.0; ## Used for shot - The perceptive volume is very bellow
                   ## from the other sounds....
_VOLUME_MED = 0.5;
_VOLUME_LOW = 0.2;


PRE_INIT_FREQUENCY = 22050;
PRE_INIT_SIZE      =   -16;
PRE_INIT_CHANNELS  =     1;
PRE_INIT_BUFFER    =   512;


################################################################################
## Private Functions                                                          ##
################################################################################
def _generateTone(freq, wave, play_frames,
                  vol       = 1,
                  add_noise = False):

    (pb_freq, pb_bits, pb_chns) = pygame.mixer.get_init();
    length = GAME_FRAME_SECS * play_frames;

    multiplier = int(freq * length);
    length     = max(1, int(float(pb_freq) / freq * multiplier));
    lin        = np.linspace(0.0, multiplier, length, endpoint=False);

    ## Generate the waves.
    if(wave == WAVE_SINE):
        ary = np.sin(lin * 2.0 * np.pi);

    elif(wave == WAVE_SAW):
        ary = 2.0 * ((lin + 0.5) % 1.0) - 1.0;

    elif(wave == WAVE_SQUARE):
        ary = np.zeros(length);
        ary[lin % 1.0 < 0.5]  = 1.0;
        ary[lin % 1.0 >= 0.5] = -1.0;


    ## Noise
    if(add_noise):
        noise = np.random.normal(0, 1, length);
        ary = ary + noise;

    ## If mixer is in stereo mode, double up the array
    ## information for each channel.
    if pb_chns == 2:
        ary = np.repeat(ary[..., np.newaxis], 2, axis=1)


    buffer = None;
    ## 8 Bits
    if(pb_bits == 8):
        snd_ary = ary * vol * 127.0;
        buffer  = (snd_ary.astype(np.uint8) + 128);
    ## 16 Bits
    elif(pb_bits == -16):
        snd_ary = ary * vol * float((1 << 15) - 1);
        buffer  = (snd_ary.astype(np.int16));

    return buffer;


def _play_buffer(channel, buffer):
    sound_buffer = pygame.sndarray.make_sound(buffer);
    channel      = pygame.mixer.Channel(channel);

    unused_channel = pygame.mixer.find_channel();
    if(unused_channel is not None):
        channel = unused_channel;
    # else:
        #print "- Cannot find a unused channel -"

    if(channel.get_busy()):
        channel.queue(sound_buffer);
    else:
        channel.play(sound_buffer);


def _play_sound(channel, frequency, wave_type,
                frames_count, add_noise, volume):

    tone = _generateTone(freq        = frequency,
                        wave        = wave_type,
                        play_frames = frames_count,
                        vol         = volume,
                        add_noise   = add_noise);

    _play_buffer(channel, tone);


################################################################################
## Init                                                                       ##
################################################################################
def pre_init():
    pygame.mixer.pre_init(PRE_INIT_FREQUENCY,
                          PRE_INIT_SIZE,
                          PRE_INIT_CHANNELS,
                          PRE_INIT_BUFFER);



################################################################################
## Stop                                                                       ##
################################################################################
def stop_all_sounds():
    pygame.mixer.Channel(CHANNEL_INDEX_PLAYER).stop();
    pygame.mixer.Channel(CHANNEL_INDEX_TICTAC).stop();
    pygame.mixer.Channel(CHANNEL_INDEX_SHOT  ).stop();
    pygame.mixer.Channel(CHANNEL_INDEX_HIT   ).stop();
    pygame.mixer.Channel(CHANNEL_INDEX_OTHER ).stop();


################################################################################
## Intro                                                                      ##
################################################################################
def play_intro():
    pygame.mixer.Sound(assets.build_path("amazing_intro.wav")).play();


################################################################################
## Player                                                                     ##
################################################################################
def play_player_sound(y_per):
    if(not _PLAYER_ENABLED):
        return;

    y_per     = 1.0 - y_per; ## 0 -> Bottom, 1 -> Top.

    max_freq  = 320;
    min_freq  = 222;
    step_freq = (max_freq - min_freq) / float(ENEMIES_LEFT_COUNT);

    curr_freq_index = int(y_per * ENEMIES_LEFT_COUNT);
    curr_freq       = min_freq + (curr_freq_index * step_freq);

    _play_sound(channel      = CHANNEL_INDEX_PLAYER,
                frequency    = curr_freq,
                wave_type    = WAVE_SQUARE,
                frames_count = 5,
                add_noise    = False,
                volume       = _VOLUME_LOW);


################################################################################
## Tic Tac                                                                    ##
################################################################################
_tictac_index = 0;
def play_tictac_sound():
    if(not _TICTAC_ENABLED):
        return;

    global _tictac_index;
    _tictac_index += 1;

    tic_freq  = 400;
    tac_freq  = 200;
    curr_freq = tac_freq if _tictac_index % 2 == 0 else tic_freq;

    _play_sound(channel      = CHANNEL_INDEX_TICTAC,
                frequency    = curr_freq,
                wave_type    = WAVE_SQUARE,
                frames_count = 5,
                add_noise    = False,
                volume       = _VOLUME_MED);



################################################################################
## Shot                                                                       ##
################################################################################
def play_shot_sound():
    if(not _SHOT_ENABLED):
        return;

    min_freq  = 200;
    max_freq  = 250;
    curr_freq = random.randint(min_freq, max_freq);

    _play_sound(channel      = CHANNEL_INDEX_SHOT,
                frequency    = curr_freq,
                wave_type    = WAVE_SAW,
                frames_count = 3,
                add_noise    = True,
                volume       = _VOLUME_HI);


################################################################################
## Hit                                                                        ##
################################################################################
def play_hit_sound(enemy_width):
    if(not _HIT_ENABLED):
        return;

    max_freq  = 700;
    curr_freq = 700 - enemy_width;

    _play_sound(channel      = CHANNEL_INDEX_HIT,
                frequency    = curr_freq,
                wave_type    = WAVE_SQUARE,
                frames_count = 3,
                add_noise    = (enemy_width == 0),
                volume       = _VOLUME_MED);


################################################################################
## Victory                                                                    ##
################################################################################
def play_victory_sound():
    if(not _VICTORY_ENABLED):
        return;

    min_freq = random.randint(600, 1000);
    grow     = random.randint(200,  250);

    gen    = lambda i: _generateTone(min_freq + (i * grow), WAVE_SQUARE, 10, _VOLUME_MED);
    buffer = np.concatenate(map(gen, range(0, 4)));

    _play_buffer(CHANNEL_INDEX_OTHER, buffer);


################################################################################
## Defeat                                                                     ##
################################################################################
def play_defeat_sound():
    if(not _DEFEAT_ENABLED):
        return;

    max_freq = random.randint(800, 1000);
    decay    = random.randint(200,  250);

    gen    = lambda i: _generateTone(max_freq - (i * decay), WAVE_SQUARE, 10, _VOLUME_MED);
    buffer = np.concatenate(map(gen, range(0, 4)));

    _play_buffer(CHANNEL_INDEX_OTHER, buffer);



################################################################################
## Game Over                                                                  ##
################################################################################
def play_gameover_sound():
    if(not _GAMEOVER_ENABLED):
        return;

    gen    = lambda i: _generateTone(random.randint(200, 800), WAVE_SAW, 10);
    buffer = np.concatenate(map(gen, range(0, 8)));

    _play_buffer(CHANNEL_INDEX_OTHER, buffer);


################################################################################
## Enemy Init                                                                 ##
################################################################################
def play_enemy_init_sound(index):
    if(not _ENEMIES_ENABLED):
        return;

    min_freq  = 200;
    step_freq =  20;

    _play_sound(channel      = CHANNEL_INDEX_OTHER,
                frequency    = min_freq + (step_freq * index),
                wave_type    = WAVE_SQUARE,
                frames_count = 3,
                add_noise    = False,
                volume       = _VOLUME_LOW);
