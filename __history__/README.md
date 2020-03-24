# Game_RamIt

**Made with <3 by [Amazing Cow](http://www.amazingcow.com).**


<!-- ####################################################################### -->
<!-- ####################################################################### -->

## Description:

```Game_RamIt``` is a small _"quasi"_-remake of the Telesys Ram It.   
You can find more info about the original game in 
[AtariAge](https://atariage.com/software_page.php?SoftwareLabelID=396)

It was developed in python using mainly ```pygame``` and ```numpy```.


<br>
As usual, you are **very welcomed** to **share** and **hack** it.


<!-- ####################################################################### -->
<!-- ####################################################################### -->

## Dedication

This game is dedicated to folks at [APAE](https://www.apaebrasil.org.br) 
that are doing a **great** job helping people that needs.   

Take a 5 min break, take a look their site and find a way to help them :D

Thanks! 


<!-- ####################################################################### -->
<!-- ####################################################################### -->

## Download & Install:

#### Option 1 - Source packages, _almost_ just download and play.

**Check notes bellow about source install.**


#### Option 2 - Clone / Fork the repo and hack it.

Also you can just ```git clone https://github.com/AmazingCow-Game/Game_RamIt``` 
to grab the latest version of sources.    
You should (and probably will) be good to go!

**Check notes bellow about source install.**


#### Notes:

The game depends on ```pygame``` and ```numpy``` to run - So you need to 
have them installed.

Assuming that you have both ```pygame``` and ```numpy```, we made a Makefile 
that installs the game into your system.    

So just type:   
``` bash
make dev-build    ## To generate the build.
sudo make install ## To install the game.
``` 

With the appropriated privileges and start gaming :D

The ```install``` target will create a ```.desktop``` entry in ```games```
sub-menu. So you can play clicking it or typing ```ram-it``` in your 
terminal.


<!-- ####################################################################### -->
<!-- ####################################################################### -->

## Dependencies:

```Game_RamIt``` depends on:

* [pygame](http://www.pygame.org/)
* [numpy](http://www.numpy.org/)

For those that wants to make a executable from the python sources ```Game_RamIt```
will depends on:

* [pyinstaller](http://www.pyinstaller.org/)


<!-- ####################################################################### -->
<!-- ####################################################################### -->

## License:

This software is released under GPLv3.



<!-- ####################################################################### -->
<!-- ####################################################################### -->

## TODO:

Check the TODO file for general things.

This projects uses the COWTODO tags.   
So install [cowtodo](http://www.github.com/AmazingCow-Tools/COWTODO) and run:

``` bash
$ cd path/to/the/project
$ cowtodo 
```

That's gonna give you all things to do :D.



<!-- ####################################################################### -->
<!-- ####################################################################### -->

## Others:

Check our repos and take a look at our 
[open source site](http://opensource.amazingcow.com).
