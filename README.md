# JETPACK JOYRIDE 

## Requirements    
* python3 

        sudo apt install python3
* colorama library 
        
        sudo apt install python-pip
        pip3 install colorama

## Running

    python3 game.py

## Oops concepts implementation

__Inheritance__ :
         
    Player and enemy inherit from the same class 'person'
    Coins, Magnet, beams, powerups inherit from the same class 'objects'
    
__Polymorphism__ :
         
    Dragon shoot overrides person shoot in its parent class 'person'
    Coin generate, coin place replaces generate and place functions of its parent class 'objects'

__Encapsulation__ :
         
    Classes and objects are used for every type of objects

__Abstraction__ :
        
    Intuitive functions like player.move_right(), Manget.place(), boss.shoot() are used  
    


## Movement 
| Key | Function |
| -- | -- |
|a | move left|
|d| move right|
|w | move up|
|b | fire bullets|
|q | exit game|
|[space] | activate shield|
* Player cam move within the window, but can't go ouside the window
* Gravity operates when mandalorian is in air


## Background
* Background keeps moving each second. The Mandalorian cannot go above sky or below ground.
* There are coins which are present and can be collected to increase the score.

## Obstacles
__Fire beams__ :
            
* Fire beams appear in the scenery which may be in horizantal, vertical or tilted shape. 
* Player looses a life when he touches one of these.
    
__Magnet__ : 
            
* A magnet appears randomly which attracts the player towards it along both x-axis and y-axis

## The Boss Enemy

* The boss enemy appears at the end of the game. 
* The boss enemy is viserion(a dragon) which has 50 lives.
* The dragon adjusts it's position according to the player i.e; 
* It follows the player along the y-direction. 
* It looses it's lives when the player shoots bullets at it
* Player scores 20 points for each bullet fired at it. 

## Score and lives

* Score is calculated taking into account of no. of coins collected, no. of fire beams desroyed and no.of bullets fired at the boss enemy.
* Score, Time remaining, Lives of player left, Lives of boss enemy left and The state of shield are displayed at the top of the screen. 
* The score calculation is as follows :

 
| Type | Score |
| -- | -- |
| Coin | 10 |
| Beam | 15 | 
| Bsoss | 20 |

## Power-Ups

__Speed Boost__ : 
* When this power-up is collected, the speed of the gameplay is increased for 10 sec.

__Shield__ : 
* The shield is activated by pressing space bar.
* It remains activated for 10 seconds and becomes available after 30 sec
* The shield is also activated after the player looses a life 
## Bonus 

__Colours__ :
* Different colours are used for different objects.
* Colours are implemented using colorama library

## Additional libraries used
* Colorama