# Handle action "take"

![Handle_action_take](https://www.plantuml.com/plantuml/svg/ZP6nQiCm48PtFSLVJVRalQMGiTrB8LEuMET6H3uPwJo4adSlaXsQWY7LTkYxx_wJTbafwJm6ypGb-Xe9S-PFJkfx2ky3eXXJ4MCcIkhLHy4RYGiCwcjbbSviyMq0m0zelF88ds7FVB4jzCI2viAvhSIDghVm0c5AXzAJDzbodicvHGUDAFDawNZvYpaEhBoIGuhZdVmXgdGClCbcrdNPW-FS9p_LnLzXzt6kSKfm5DLl9uVCQ2Is_tLzd3XnUJU9HOLItll4-S5icnyax4aawYqeAPgkAtjsNRiEMEJNyjTnCZiMDu_X1m00 "Handle_action_take")

<!-- 
```plantuml
@startuml
!pragma useVerticalIf on

start

partition Handle action "take" {
    if (item is "key") then (yes)
        if ("key" in near_items) then (yes)
            :add "key" to taken_items;
            :delete "key" from near_items;
            :delete "key" from table_items;
            :set action_description = "You take the key";
        else (no)
            :set action_description = "There is no key here";
        endif
    else (no)
        :set action_description = "You cannot take that (//item//)";
    endif
}

stop
@enduml
```
 -->
