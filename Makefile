##----------------------------------------------------------------------------##
##               █      █                                                     ##
##               ████████                                                     ##
##             ██        ██                                                   ##
##            ███  █  █  ███        Makefile                                  ##
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
## Vars                                                                       ##
################################################################################
HOST="linux_x64"


################################################################################
## NOT INTENDED TO BE MODIFIED - But if so change the assets.py too           ##
################################################################################
_COW_BIN="/usr/local/bin"
_COW_SHARE="/usr/local/share/amazingcow_game_ramit"
_GIT_TAG=`git describe --tags --abbrev=0 | tr . _`


################################################################################
## End user                                                                   ##
################################################################################
install:
	@ echo "---> Installing...".

	@ ## Deleting old stuff...
	@ rm -rf $(_COW_SHARE)
	@ rm -rf $(_COW_BIN)/ram-it

	@ ## Install new stuff...
	@ cp -rf ./src/    $(_COW_SHARE)        ## Source
	@ ln -s $(_COW_SHARE)/main.py $(_COW_BIN)/ram-it
	@ chmod 755 $(_COW_BIN)/ram-it

	@ cp -rf ./assets/ $(_COW_SHARE)/assets ## Assets

	@ echo "---> Done... We **really** hope that you have fun :D"



################################################################################
## Release                                                                    ##
################################################################################
gen-binary:
	rm -rf build     \
	       dist      \
	       bin       \
	       ram_it.spec

	pyinstaller -F --windowed                                       \
	            --name="ram_it"                                     \
	            --osx-bundle-identifier="com.amazingcow.game_ramit" \
	            ./src/main.py

	mkdir -p ./bin/game_ramit
	cp -r ./assets/      ./bin/game_ramit/assets
	cp    ./dist/ram_it  ./bin/game_ramit/ram_it
	cp AUTHORS.txt   \
	   CHANGELOG.txt \
	   COPYING.txt   \
	   README.md     \
	   TODO.txt      \
	   ./bin/game_ramit

	cd ./bin && zip -r ./$(HOST)_$(_GIT_TAG).zip ./game_ramit
	rm -rf ./bin/game_ramit


gen-archive:
	mkdir -p ./archives

	git archive --output ./archives/source_game_ramit_$(_GIT_TAG).zip    master
	git archive --output ./archives/source_game_ramit_$(_GIT_TAG).tar.gz master


################################################################################
## Dev                                                                        ##
################################################################################
dev-build:
	python ./src/main.py ./assets
	rm ./src/*.pyc


dev-info:
	python ./src/enemy_info.py
