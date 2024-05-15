# Handle action "switch on"

![Handle_action_switch_on](https://www.plantuml.com/plantuml/svg/ZP71IiGm48RlUOhVdDfJxyh27lKkWgSoD5CRI2SXcI2BxBilQTLL536t8TzyyqzoB4fPwnhCJShqiX9guIVEwYSA3pEY6BCXnYJAwjL7mJs92moQjigMLw_JWYWMRmO0_8pEAw_m1JRGccmFNLZGdRZq6_A1xTSDz09XocDhBB_oxTmMLhIUiIWfum0RnTxzPFPme-CoPP-se0VOvrYnnsNNHcmgV3DmA8p_-XuNpjpIIznLhVug4-Tdywdj95xN-KDxYXKJYKHzJmjTID4DGtkTOUYlaVS9Pw3zKqpcoEBg6Yu0 "Handle_action_switch_on")

<!-- 
```plantuml
@startuml
!pragma useVerticalIf on

start

partition Handle action "switch on" {
    if (item is "lamp") then (yes)
        if ("lamp" is in near_items) then (yes)
            :set lamp_state = "on";
            :set action_description = "You switched the lamp on";
        else 
            :set action_description = "There is no lamp here";
        endif
    else (no)
        :set action_description = "you cannot switch that (//item//) on";
    endif
}  

stop
@enduml
```
 -->
