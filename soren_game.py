# The beginning

print("You wake up in a mysterious place.")

cave_description = "You are in a dim lit room. You see a table, and on the wall a door"
scene_description = cave_description
action_description = ""
# print(cave_description)


prompt = "You can now make action by typing verbs and items"
actions = ["go to", "switch on", "enable" ] # more to come
items   = ["table", "door", "lamp", "Lock", "key"] # maybee item shall have states as well ...?

holding_items = []
near_items = []
table_items = ['lamp', 'key']
door_items = []

lamp_state = "off"

positions = ["floor", "table", "wall"]
current_pos = "floor"

game_over = False

# For the rest of eternaty (or the end of this game).
# TODO Consider what will cause gameover?
while not game_over:
    
    ### Display 
 
    #### possitional scene description

    if current_pos == "table"
        if lamp_state == "on":
            scene_description += "The Lamp as turned on, and on the table you can see a key."
        else:
            scene_description += "The Lamp as turned off." # but what if the lamp is on?
    elif current_pos == "door":
        scene_description = "In the wall there is a door. There is a huge lock on the door. The door won't open!"    

     # for debugging:
    print('Debug info:########################################################################')
    # print("Verbs:", actions)
    # print("items:", items)
    print('table_items:', table_items)
    print('door_items:', door_items)
    print('near_items:', near_items)
    print("holding items:", holding_items)
    print('###################################################################################')    

    print(action_description)
    print(scene_description)
    command = input( f"{prompt}> ")

    # debug info
    print("command:", command)
    
    action = ""
    item = ""
    words = command.split()
    if len(words) > 1:
        action = " ".join(words[:-1])
        item   = words[-1]
    elif len(words) == 1:
        action = words[0]

    print('Debug info:########################################################################')
    print(action)
    print(item)
    print('###################################################################################')
    

    if action == "go to":
        pass
        if item == "table":
            current_pos = "table"
            scene_description = "You are next to a table. There is a lamp on it. "
            
            near_items = table_items
        elif item == "door":
            near_items = door_items
            current_pos = "door"
        else:
            action_description = f"Invalid command.\nYou cannot go to {item}"
    elif action == "switch on" or action == "enable":
        if item == "lamp":
            if current_pos == "table":
                lamp_state = "on"
                action_description = "You switched the lamp on..."
            else:
                action_description = "There is no lamp here"
        else: 
            pass 
    elif action == "take":
        # [FIXME] kan man tage nøglen hvis lampen ikke er tændt, og det er mørkt
        # [BUG] man skal KUN kunne tage nøglen, hvis man er ved bordet
        # [TODO] "key" skal tilføjes til listen holding items  
        if item not in near_items:
            action_description = f"{item} is not here, so you cannot take it."
        else:
            if item == "key":
                action_description = "You took the key"
                holding_items.append('key')
                near_items.remove('key')
            else:
                action_description = f"You cannot take {item}"
    elif action == "quit" or action == "q":
        break
    else:
        action_description = f'Invalid command. There is no action called "{action}"'
# End of loop
