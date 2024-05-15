# Text Adventure 1

This is a super small and simple adventure game. 
It written in python, doesn't have a game engine or any graphics.
The basic theme would be an escape room, since there is only one róom the game, and the objective is to unlock the door and leave the room.

Even if its a single player game, the is a kind of turn round trip. 
The user types a command, some states change, a new set of informations diplay, and the user is prompted to type another command.

## Flow 

We have made a main loop, that runs until we have `game over`. We introduced the variable `gameover`, to handle this state. To start with we set this to the boolean value `False`.

Inside the main-loop we 
1. Display descriptions based on states
1. Get next command from user
1. Split user command in action and item
1. Take action for each of the possible actions

The loop end if we have `gameover` if True. That only happens when the user exits the door, og pres `q` (or `quit`).

Each action is delegated to sub flowcharts for each action. See below.

We will try to handle each action in the dociments listed below.


<!--
```plantuml
@startuml
'object gameover

!pragma useVerticalIf on


start
partition Init {
    :Handle initialization;
}

while (gameover) is (False)
    partition Display descriptions {
        :Handle display;
    }

    :get user command>
    :split `command` into action and item;

    if (action is "go to") then (yes)
        partition Handle action "go to" {
           :Handle action "go to";
        }
    elseif (action is "switch on" or "enable") then (yes)
        partition Handle action "switch on" {
            :Handle action "switch on" ;
        }  
    elseif (action is "switch off" or "disable") then (yes)
        partition Handle action "switch off" {
            :Handle action "switch off";
        }
    elseif (action is "take") then (yes)
        partition Handle action "take" {
            :Handle action "take";
        }
    elseif (action is "throw") then (yes)
        partition Handle "throw" {
           :Handle action "throw";
        }
    elseif (action is "use") then (yes)
        partition Handle "use" {
            :Hande action "use";
        }
    elseif (action is "open") then (yes)
        partition Handle "open" {
            :Handle action "open";
        }
    endif 

end while (True)

:Show "The game ended in ...";
if (win is True) then (yes)
    :show "Success!";
else (no)
    :show "Failure";
endif
->the.end;
stop

@enduml
```
-->

![README](https://www.plantuml.com/plantuml/svg/fPJ1Rfmm48RlynGJBeL3zm4MASgXYffpefxZu66PreoHFHIbrRvxPKEpR59rYN93zlVF_zb2lebgWewzWq_-wJirYWVJa_z90U1g2ERG6nmZVQEWt1Xtrw8N0CWf64nGLlQ2TyAAlm4HSV_LY7M4BAni7FyoYQZX231rx0ZBlmqLSiJorhX8LOwUvdtXE3ZpZ9PY4tX8Qt6Pl-wmCrRdZIFC_GVIf1omyNrln5xFot5mhFYuB3uYYteqJQupOf6L-deUmIsMomv7B0uUrHSLQaU2vJF5waNaPBmOBR4bir9UMPypzGjop5_a8hqIY1Dhqw6N0dt0WiGyENgdq6h6cTGRgnMuKaEy9DUsivtb-06zD6MRNzjkkJerFzwhaYCN93ApfRuBVjhOly3__sTcPaFp6BUUEwF_Ek-fDH4RElr0ihKqinTkEJDlUiLoYm0a5fS7vI6CL07ixpi_OV7GKNx44aaMMN2tsnKr9Dc9isaElFRSnno_7vk6OhmgQaX7n5BysVwjOJU6T1_P13vVQqSx4bj3L3y0t93OiNT_0000 "README")



## Sub flowcharts

### Init 
About how all variable are initialized to their startup values.  
See [Init.md](docs/Init.md)

### Display_descriptions
### Handle_action_go_to
### Handle_action_open
### Handle_action_switch_off
### Handle_action_switch_on
### Handle_action_take
### Handle_action_throw
### Handle_action_use


docs\Display_descriptions.puml
docs\Handle_action_go_to.puml
docs\Handle_action_open.puml
docs\Handle_action_switch_off.puml
docs\Handle_action_switch_on.puml
docs\Handle_action_take.puml
docs\Handle_action_throw.puml
docs\Handle_action_use.puml
