# Initilazation

Initialization of variables to initial values.
At last we print to screen, som introductional info and the initail descriptions.
<!-- 
```plantuml
@startuml
partition Init {
    :set initial state values;
    ' note left
    '     Several states to be detailed later
    '     * gameover
    '     * location
    '     * items near
    '     * items state
    '     * items taken
    ' end note
}
@enduml
``` -->


![Init](https://www.plantuml.com/plantuml/svg/ROun3i8m54FtdC8R4aU0fIip9_WGWo9-4fIuNH1tHwse18Y_-Tdozz1bJMFsSBUcf5GB3YK9Zm00kquXbQHaZYuJCPcFxFl5tg1K4SwBtdg-8oUsDT-XYXCHAKlE23UnVQItk5fcdNwWrxFDQxvW4dD7eRK_U7dtXyjkN6jOuZ8vFCF04iViBm00 "Init")

## Variables and values

name                    | value     | .
:-                      | :-        |:-
`gameover`              | `false`   | When the game is over, it should be `True`
`location`              | `"floor"` | Can also be `"table"` or `"door"`
`near_items`            | `[]`      | Empty list. key, lamp and door can be added
`taken_items`           | `[]`      | Empty list. key can be added
`table_item`            | `["lamp", "key"]` | A list of what's on the table. The key can be removed (if taken)
`door_item`            | `[]`       | A list of what's at the door. The key can be left here (if thrown)

### Descriptive texts

name                    | value     | .
:-                      | :-        |:-
`welcome_description`   | `"You are en a dark cave... bla bla"              | Displayed at the start, and maybe at every turn?
`table_description` lamp off | `"A solid table, with a lamp it. The lamp is switched off"` | Has an alternative text when lamp is on
`table_description` lamp on  | `"A solid table, with a lamp it. The lamp is switched on. On the table you see a key!"`                 | Has an alternative text when lamp is off
`action_description`    | `""`      | Initally an empty string.

### Item states

name        | initial state     | possible states
:-          | :-                | :-
`lamp_state`      | `"switched off"`  | `"switched off"` or `"switched on"`
`door_state`        | `"locked"`        | `"locked"`, `"unlocked"` or `"open"`.          


