# Handle Action "go to"

![Handle_action_go_to](https://www.plantuml.com/plantuml/svg/dP712i8m38RlVOhVdVGL5657VG71ayGrqqBNZ3OzYFZkqeuT1Zk88PV0zoSVf4rAKVFWpMQCz1W8EV65exgE_Bc716CgOin8KPqw2JXHi9v1NPsQXq2bmTi0WEknTSe3N4AZTFVSxA1F3jY-EEqgKsgVME6bexhZEBE79J2Tk5bENNJZZ5ubenwj_MIiPWDJl1MLLB62JEF4iK-yaBKYyKVNYlwdkXPTcXPY8Hgiwysd_456qtAmUV1V "Handle_action_go_to")

<!--
```plantuml
@startuml
!pragma useVerticalIf on

start

partition Handle action "go to" {
    if (item is "table") then (yes)
        :set location = "table";
        :set action_description = "You go to to the table";
        :set near_items to table_items;
    elseif (item is "door") then (yes)
        :set location = "door";
        :set action_description = "You go to to the door";
        :set near_items to door_items;
    endif
}

stop
@enduml
```
-->