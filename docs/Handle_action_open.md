# Handle Action "open"

![Handle_action_open](https://www.plantuml.com/plantuml/svg/bPB1IiGm48RlUOhVdjfJxyh27lKkWgSb9DDjC9s4P8A8-EwIT8kBhYlcDl3DzsU6sMVHIShYrKrC-hXeb4nFbCGPxHyc15Qg8Kf5dSI92unxpTOJj6bL5o9nXtS506v2xuGMk8pEXf2w0J8Jet-ZF3HamtmmkWckenjUYKCMBTGQ2ljWNiZ-tbJVRIR1MUVkzDkxo-GwqS5IDid5zhaTkkTG44kUQr2JGRE54-HNnyUC2qRocT1p6FwJyxZfNSPfk6zMjcvIrpEk-rDR7eSrfzPd4L_wd-e_rcCqSv2s2SYi1VqurZCOns7rh-wFUamXgZsnBOl_1000 "Handle_action_open")

<!-- ```plantuml
@startuml
!pragma useVerticalIf on

start

partition Handle action "open" {
    if (item is "door") then (yes)
        if (location is "door") then (yes)
            if (door_state is "unlocked") then (yes)
                :set door_state = "open";
                :set action_description = "You push the door and it swings open";
            else (no)
                :set action_description = "The door is locked";
            endif
        else (no)
            :set action_description = "There is no door here";
        endif
    else (no)
        :set action_description = "You cannot open that (//item//);
    endif
}

stop
@enduml
``` -->
