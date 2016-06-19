# coding=utf8
##----------------------------------------------------------------------------##
##               █      █                                                     ##
##               ████████                                                     ##
##             ██        ██                                                   ##
##            ███  █  █  ███        enemy_info.py                             ##
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
## Game_RamIt ##
from constants import *;



################################################################################
## Constants                                                                  ##
################################################################################
_MAX_LEVELS       = 30;
_MIN_BASE_TIMER   = 0.16;
_BASE_TIMER_INDEX = 0;
_THRESOLD_INDEX   = 1;
_DECAY_INDEX      = 2;



################################################################################
##  DO NOT TOUCH THIS VALUES WITH OUT CHANGE THE _adjust_difficulty function  ##
##  DO NOT TOUCH THIS VALUES WITH OUT CHANGE THE _adjust_difficulty function  ##
################################################################################
_INFO = [
    [], ## EMPTY

##  Base Timer --- Thresholds       ---  Decay
    [0.45,         [25, 15       ],      0.09       ], ## Level1
    [0.45,         [25, 15,      ],      0.1        ], ## Level2
    [0.45,         [25, 15, 5    ],      0.0666666  ], ## Level3
    [0.43,         [25, 15       ],      0.1        ], ## Level4
    [0.43,         [25, 15, 5    ],      0.0666665  ], ## Level5
    [0.42,         [25, 15       ],      0.105      ], ## Level6
    [0.42,         [25, 15, 5    ],      0.07       ], ## Level7
    [0.41,         [25, 15       ],      0.105      ], ## Level8
    [0.41,         [25, 15, 5    ],      0.07       ], ## Level9
    [0.40,         [25, 15, 10, 5],      0.04998    ], ## Level10
##  Base Timer --- Thresholds       ---  Decay
    [0.40,         [25, 15, 5     ],     0.0566667], ## Level 11
    [0.392,        [25, 15, 10    ],     0.0573333], ## Level 12
    [0.392,        [25, 20, 15, 10],     0.0429999], ## Level 13
    [0.37,         [25, 15, 10    ],     0.0533333], ## Level 14
    [0.37,         [25, 20, 15, 10],     0.040    ], ## Level 15
    [0.35,         [25, 15, 10    ],     0.0499999], ## Level 16
    [0.35,         [25, 20, 15, 10],     0.0374999], ## Level 17
    [0.33,         [25, 15, 10,   ],     0.0466666], ## Level 18
    [0.33,         [25, 20, 15, 10],     0.035    ], ## Level 19
    [0.3,          [25, 20, 15, 10],     0.0285   ], ## Level 20
##  Base Timer --- Thresholds       ---  Decay
    [0.30,         [25, 15, 10    ],     0.0299999 ], ## Level 21
    [0.29,         [25, 15, 10    ],     0.0266666 ], ## Level 22
    [0.29,         [25, 20, 15, 10],     0.0199999 ], ## Level 23
    [0.28,         [25, 15, 10    ],     0.0266666 ], ## Level 24
    [0.28,         [25, 20, 15, 10],     0.0199999 ], ## Level 25
    [0.27,         [25, 15, 10    ],     0.0266666 ], ## Level 26
    [0.27,         [25, 20, 15, 10],     0.0199999 ], ## Level 27
    [0.26,         [25, 15, 10,   ],     0.02333333], ## Level 28
    [0.26,         [25, 20, 15, 10],     0.01749999], ## Level 29
    [0.25,         [25, 15, 10, 5 ],     0.0162499 ], ## Level 30
];



################################################################################
## Helper Functions                                                           ##
################################################################################
def _print_out():
    for i in xrange(1, len(_INFO) ):
        info = _INFO[i];

        final_timer = info[_BASE_TIMER_INDEX] - (len(info[_THRESOLD_INDEX]) * info[_DECAY_INDEX]);
        print "Level: %02d"  %(i),
        print "|   Base timer: %0.2f" %(info[_BASE_TIMER_INDEX]),
        # print "| Thresholds:", info[_THRESOLD_INDEX],
        print "|   Decay: %0.2f" %(info[_DECAY_INDEX]),
        print "|   Final timer: %f"  %(final_timer);

        if(i % 10 == 0):
            print "";


        if(final_timer < _MIN_BASE_TIMER):
            print "PLAY WILL NOT WIN THE GAME:", (i);
            exit(1);


_adjusted = False
def _adjust_difficulty():
    global _INFO;
    global _adjusted;
    if(_adjusted == True):
        return;

    for i in xrange(1, len(_INFO)):
        _INFO[i][_BASE_TIMER_INDEX] -= 0.025;
        for j in xrange(0, len(_INFO[i][_THRESOLD_INDEX])):
            _INFO[i][_THRESOLD_INDEX][j] += 4;

    _adjusted = True;



################################################################################
## Enemy Info Class                                                           ##
################################################################################
class EnemyInfo:
    ############################################################################
    ## Init                                                                   ##
    ############################################################################
    def __init__(self, level):
        if(level >= _MAX_LEVELS):
            level = _MAX_LEVELS;

        _adjust_difficulty();

        _print_out();
        info = _INFO[level];

        self.level           = level;
        self.base_timer      = info[0];
        self.timer_threshold = info[1];
        self.timer_decay     = info[2];


        # print "self.level           :", self.level;
        # print "self.base_timer      :", self.base_timer;
        # print "self.timer_threshold :", self.timer_threshold;
        # print "self.timer_decay     :", self.timer_decay;


################################################################################
## For standalone run                                                         ##
################################################################################
if __name__ == '__main__':
    _print_out();
