# Python simple menu - text based adventure game
# Michael Zhu
# Sept 21st, 2021
# CS30 
# Ms.Cotcher
""" This is the menu for a game where you are an adventurer trying to escape a 
wasteland, you can commit combat to potential enemies, collect potential materials,
and try to navigate through this endless map"""

# These variables set up the catagories for actions and the coordinate system
x = 0
y = 0
general_action = ["explore", "combat"]
explore = ["forward", "backward", "left", "right", "collect", "stop"]
combat = ["attack", "hide", "defend"]

""" The while loop that makes sure the general menu is running constantly until 
quit is inputted, during this you can either select explore or combat"""
while True:
    print("\nyou can do the following catagory of actions:")
    for i in general_action:
        print (i)
    print("side note: you can type quit to quit anytime\n")
    cata_input = input("which one do you choose?\n")
    
    """ The section is what happens when you select explore, it constantly loops
    and ask for input until you type quit which will return to the general 
    menu"""
    if cata_input.lower() == "explore":
        while True:
            print("\nu can do either")
            for direction in explore:
                print(direction)
            direction_input = input("which one do you choose?\n")
            
            # The coordinate system 
            if direction_input.lower() in explore:
                coord_change = direction_input.lower()
                if coord_change == explore[0]:
                    y += 1
                    print("your y value increased by one, " +
                    "your coord now is " + str(x)+" ," + str(y))
                elif coord_change == explore[1]:
                    y -= 1
                    print("your y value decreased by one, " +
                    "your coord now is " + str(x)+" ," + str(y))
                elif coord_change == explore[2]:
                    x -= 1
                    print("your x value decreased by one, " +
                    "your coord now is " + str(x) + " ," + str(y))
                elif coord_change == explore[3]:
                    x += 1
                    print("your x value increased by one, " +
                    "your coord now is " + str(x) + " ," + str(y))
                elif direction_input.lower() == explore[4]:
                    print(direction_input.lower() + "!")
                elif direction_input.lower() == explore[5]:
                    print("going back to the main menu\n")
                    break
            else:    
                print("invalid action!")
    
    # Happens when you select combat in the general menu
    elif cata_input.lower() == "combat":
        print("\nu can do either")
        for action_type in combat:
            print(action_type)
        combat_input = input("which one do you choose?\n")
        if combat_input.lower() in combat:
            print("\n" + combat_input.lower() + "!")
        else:
            print("invalid action!")
    
    # Breaks the loop when inputted quit and accepts wrong inputs
    elif cata_input.lower() == "quit":
        break
    else:
        print("invalid action!")
