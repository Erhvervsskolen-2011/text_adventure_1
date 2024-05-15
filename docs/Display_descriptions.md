# Display

<!--
```plantuml
@startuml
partition Display descriptions {
        :Show action (if the was one);
        :Show location description;
        :Show items near;
        :Show items taken;
        ://DEBUG// Show posible actions;
        note left
            he user should experiment, 
            to figure out what actions works where?
        end note
    }

@enduml
```
-->

![Display_descriptions](https://www.plantuml.com/plantuml/svg/ROx1JWCn44Fl-nK-WeIqTpXGeI8-0F41OTTBecOpKMQYK5NyEsfKIgdmqVCyzaRD5Qjh7B8h5Yn8mZPeZcwFcJgLa8-UuZ3WfFjNBmrkwknDM62UQ4uXYRSFLrYKoNNmujar4uoh8j6L_o_cThmCZUFs-UdjPHpHeImQtYDFY_GNJ694v69dvoXFL6M1Ugbn1ZypIrYPx0v_E1CiuQCMGggXUMS_3MXITehcMVXupZ3DlR4RNyEmOPhh6hy1 "Display_descriptions")


This section should handle the following tasks:
1. Show action (if the was one);
1. Show location description;
1. Show items near;
1. Show items taken;
1. _DEBUG_ Show posible actions;

## 1. Show action description
If the user made a command with an action, that action shall be described.  
The action could be:
* go to door
* take key

These action should result in `action_description` like
* _You go to the door_
* _You take the key_ or _There is no key, here_

The value of `action_description` is set in the section of th respective action.

The value of `action_description` shall be displayed here.

```python
print(action_description)
```

## 2. Show location description;