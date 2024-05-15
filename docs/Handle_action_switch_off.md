# Handle action "switch off"

![Handle_action_switch_off](https://www.plantuml.com/plantuml/svg/ZP5DIyGm48Rl-HMlERMdtfM5FUfT14zbQASsa4vACa4MsV--JEl7YYBc5lBEypv9ZaKfQrsYkraplIo4MlY9iuQ1uiE49Cvj4UTMoXeq9C4zoHWPlhm67MQaQV9uSm0G9ZH1UK4ey96MrRVGcGNDYKkxHJvY-x45Wq2OSc-3vTUyhTl22flfYv8o3l1MVFSpH8DPzYEN8OTrCpx0FwUANPX7wzXO-8xWM1Z_1JxEdDdy9Uqisr_3P0oJ-yGsahukz0Vsb2e64adwhWkTIT5qdRrFrxLNpdl5sRuehUx8CjObNW00 "Handle_action_switch_off")
<!-- 
```plantuml
@startuml
!pragma useVerticalIf on

start

partition Handle "switch off" {
    if (item is "lamp") then (yes)
        if ("lamp" is in near_items) then (yes)
            :set lamp_state = "off";
            :set action_description = "You switched the lamp off";
        else 
            :set action_description = "There is no lamp here";
        endif
    else (no)
        :set action_description = "you cannot switch that (//item//) off";
    endif
}

stop
@enduml
```
 -->
