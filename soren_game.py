# The beginning

print("You wake up in a mysterious place.")

cave_description = "You are in a dim lit room. You see a table, and on the wall a door"

print(cave_description)

prompt = "You can now make action by typing verbs and items. "
verbs = ["go to", "switch on", "enable" ] # more to come
items = ["table", "door", "lamp", "Lock", "key"] # maybee item shall have states as well ...?
lamp_state = "off"

positions = ["floor", "table", "wall"]
current_pos = "floor"

print("Verbs:", verbs)
print("items:", items)
print(prompt)
command = input("> ")

# debug info
print("command:", command)

verb = command[0 : command.rfind(' ')]
item = command[command.rfind(' ')+1 : -1]

print(verb)
print(item)

if verb == "go to":
    pass
    if item == "table":
        current_pos = "table"
        if lamp_state == "off":
            prompt = "You are next to a table. There is a lamp on it. The Lamp as turned off." # but what if the lamp is on?
        elif lamp_state == "on":
            prompt = "You are next to a table. There is a lamp on it. The Lamp as turned on. You also see a key laying on the table."
elif verb == "switch on" or verb == "enable":
    pass 

print(prompt)
