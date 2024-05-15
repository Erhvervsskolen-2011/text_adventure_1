# Handle action "throw" 

![Handle_action_throw](https://www.plantuml.com/plantuml/svg/hPEnJiCm48PtFyMHAHrGzbP87M57I4pLDRuqLfsxoBw08iIx8pj5D6qfGf39aJ__t-zJiewAGOVEcvi-uAv3628zKL1NetzeGDYOZ1ZJOr2dJXZkaQqdABGDybh0cm40QBoWEju1Yn9uQdG90zygxccL0TT0wPGwS16AFOt50hGbXdAakCZ49vLtmJ4mOTYaC_4Ycvwb9KzAKoAeG1BoT6Wr9z7Q0zO4wOx2vvnhIYyrvfkcgefRJyMt1KwYSuEjfql96OsaW7LAtrYATN1zDjr1yIm3v94c5Unf1E6yd1hCiyX7IhEQLRKYuJTD4_ylHRTZNcR_UKyeMHP_4xXf4Y_YxAc0hMlCTTqLrMDBWTBmMB8elHuPljBFat-uG8tCelbx16rHeQogDEkgMXm4K_Xx-iEaDsjYEtJ-0m00 "Handle_action_throw")

<!-- 
```plantuml
@startuml
!pragma useVerticalIf on

start

partition Handle "throw" {
    floating note left: un-take;
    if (item is "key") then (yes)
        if ("key" in near_items) then (yes)
            :delete "key" to taken_items;
            :add "key" from near_items;
            if(location is "table") then (yes)
                :add "key" to table_items;
                :set action_description = "You throw the key on the table";
            elseif (location is "door") then (yes)
                :add "key" to door_items;
                :set action_description = "You throw the key by the door";
            else (no)
                :set action_description = "You throw the key in the void";
            endif
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
