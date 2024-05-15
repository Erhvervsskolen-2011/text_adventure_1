# Handle action "use" 

![Handle_action_use](https://www.plantuml.com/plantuml/svg/bPB1IWCn48RlUOhVNDnUkdUbu57l8dWgu-xK3PkTBCb4AEAxosmfIgqMSmdC_FDz3CbTKSfQf-Ykvaol4w4MVkAieQFui4CIjoIScobhq904zoHzPFXQsEFT0K3OeGdA4qA17tdlLz211SsUosf975DB5q6WDB9iRQYS3Hy7OkfeqHgwJodxN-DsRWehBBOjIihOm5U9gHkvzxVdqzGPVzjpwNAO5zS6_ZbL12cSrNGOURzUh_4IoIwhc0HLOkt6SeBcM1YDfDL_X8y3PxOj9PbjI95XfLEsz67d_ZPTMAjFSgqOw8r1flfc-AB_95-WTYIIrFuFT215qxRskcsxEk0Fw0_dYgRPtR7qTOgV "Handle_action_use")

<!-- 
```plantuml
@startuml
!pragma useVerticalIf on
start

partition Handle "use" {
    if (item is "key") then (yes)
        if ("key" in taken_items) then (yes)
            if (location is "door") then (yes)
                :set door_state = "unlocked";
                :set action_description = "You insert the key... bla... the door unlucks";
            else (no)
                :set action_description = "There is no keyhole here";
            endif
        else (no)
            :set action_description = "You don't have a key";
        endif
    else (no)
        :set action_description = "You cannot use that (//item//);
    endif
}

stop
@enduml
``` -->