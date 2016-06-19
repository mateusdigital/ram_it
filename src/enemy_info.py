
import numpy as np;
from constants import *;

MAX_LEVELS     = 30;
MIN_BASE_TIMER = 0.16;


_INFO = [
    [], ## EMPTY

##  Base Timer         Thresholds                    Decay
    [0.45,              [25, 15      ],              0.09     ], ## Level1

    [0.45,              [25, 15,     ],              0.1      ], ## Level2
    [0.45,              [25, 15, 5   ],              0.0666666], ## Level3

    [0.43,              [25, 15      ],              0.1      ], ## Level4
    [0.43,              [25, 15, 5   ],              0.0666665], ## Level5

    [0.42,              [25, 15      ],              0.105    ], ## Level6
    [0.42,              [25, 15, 5   ],              0.07     ], ## Level7

    [0.41,              [25, 15      ],              0.105    ], ## Level8
    [0.41,              [25, 15, 5   ],              0.07     ], ## Level9

    [0.4,               [25, 15, 10, 5],             0.04998    ], ## Level10

    ##  Base Timer       Thresholds                    Decay
    [0.40,               [25, 15, 5     ],              0.0566667], ## Level 11

    [0.392,              [25, 15, 10    ],              0.0573333], ## Level 12
    [0.392,              [25, 20, 15, 10],              0.0429999], ## Level 13

    [0.37,               [25, 15, 10    ],              0.0533333], ## Level 14
    [0.37,               [25, 20, 15, 10],              0.040], ## Level 15

    [0.35,               [25, 15, 10     ],              0.0499999], ## Level 16
    [0.35,               [25, 20, 15, 10 ],              0.0374999], ## Level 17

    [0.33,               [25, 15, 10,   ],              0.0466666], ## Level 18
    [0.33,               [25, 20, 15, 10 ],             0.035],     ## Level 19

    [0.3,                [25, 20, 15, 10],               0.0285], ## Level 20


##  Base Timer           Thresholds                    Decay
    [0.30,               [25, 15, 10     ],             0.0299999], ## Level 21

    [0.29,               [25, 15, 10    ],              0.0266666], ## Level 22
    [0.29,               [25, 20, 15, 10],              0.0199999], ## Level 23

    [0.28,               [25, 15, 10    ],              0.0266666], ## Level 24
    [0.28,               [25, 20, 15, 10],              0.0199999], ## Level 25

    [0.27,               [25, 15, 10     ],              0.0266666], ## Level 26
    [0.27,               [25, 20, 15, 10 ],              0.0199999], ## Level 27

    [0.26,               [25, 15, 10,   ],              0.02333333], ## Level 28
    [0.26,               [25, 20, 15, 10 ],             0.01749999],     ## Level 29

    [0.25,               [25, 15, 10, 5],               0.0162499], ## Level 30
];

_BASE_TIMER_INDEX = 0;
_THRESOLD_INDEX   = 1;
_DECAY_INDEX      = 2;

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

        if(final_timer < MIN_BASE_TIMER):
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

class EnemyInfo:
    ############################################################################
    ## Init                                                                   ##
    ############################################################################
    def __init__(self, level):
        if(level >= MAX_LEVELS):
            level = MAX_LEVELS;

        _adjust_difficulty();

        _print_out();
        info = _INFO[level];

        self.level           = level;
        self.base_timer      = info[0];
        self.timer_threshold = info[1];
        self.timer_decay     = info[2];


        print "self.level           :", self.level;
        print "self.base_timer      :", self.base_timer;
        print "self.timer_threshold :", self.timer_threshold;
        print "self.timer_decay     :", self.timer_decay;

        # exit(0);


if __name__ == '__main__':
    _print_out();
