# the blueprint for a room
class Room:
    # the constructor
    def __init__(self, name):
        # rooms have a name, exits (e.g., south), exit locations
        # (e.g., to the south is room n), items (e.g., table), item
        # descriptions (for each item), and grabbables (things that
        # can be taken into inventory)
        # used to check state of rug for game progression
        self.name = name
        self.exits = []
        self.exitLocations = []
        self.items = []
        self.itemDescriptions = []
        self.grabbables = []
        self.rug_cleaned = False
        

    # getters and setters for the instance variables
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def exitLocations(self):
        return self._exitLocations

    @exitLocations.setter
    def exitLocations(self, value):
        self._exitLocations = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def itemDescriptions(self):
        return self._itemDescriptions

    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    # adds an exit to the room
    # the exit is a string (e.g., north)
    # the room is an instance of a room
    def addExit(self, exit, room):
        # append the exit and room to the appropriate lists
        self._exits.append(exit)
        self._exitLocations.append(room)

    # adds an item to the room
    # the item is a string (e.g., table)>back
        
    # the desc is a string that describes the item (e.g., it is made of wood)
    def addItem(self, item, desc):
        # append the item and description to the appropriate lists
        self._items.append(item)
        self._itemDescriptions.append(desc)

    # adds a grabbable item to the room
    # the item is a string (e.g., key)
    def addGrabbable(self, item):
        # appends the grbbable to the appropriate list
        self._grabbables.append(item)
        

    # removes a grabbable item from the room
    # the item is a string (e.g., key)
    def delGrabbable(self, item):
        # remove the item from the list
        self._grabbables.remove(item)

    #changes item description pending player manipulation
    def modifyItemDescription(self, item, new_description):
            # Check if the item exists in the room's items
            if item in self.items:
                # Find the index of the item in the items list
                index_in_room = self.items.index(item)
                
                # Update the item description
                self.itemDescriptions[index_in_room] = new_description

    #removes an item from a player's inventory if it is used
    def removeItem(self, item):
        #removes item from inventory
        inventory.remove(item)

    #function that adds the exit to room 2 if the rug is cleaned.
    def cleanRug(self):
        #changes the state of the rug
        self.rug_cleaned = True
        #checks that room is 2
        if self.name == "Room 2":
            #adds the exit for secret passage
            self.addExit("under", r5)
        return self.rug_cleaned
    
 
    # returns a string description of the room
    def __str__(self):
        # first, the room name
        s = "You are in {}.\n".format(self.name)
        # next, the items in the room
        s += "You see: "
        for item in self.items:
            s += item + " "
        s += "\n"
        # next, the exits from the room
        s += "Exits: "
        for exit in self.exits:
            s += exit + " "
        return s

# creates the rooms
def createRooms():
   # create the rooms and give them meaningful names
    r1 = Room("Room 1")
    r2 = Room("Room 2")
    r3 = Room("Room 3")
    r4 = Room("Room 4")
    r5 = Room("Secret Room")

    # add exits to room 1
    r1.addExit("east", r2)  # -> to the east of room 1 is room 2
    r1.addExit("south", r3)

    # add grabbables to room 1
    r1.addGrabbable("key")

    # add items to room 1
    r1.addItem("chair", "It is made of wicker and no one is sitting on it.")
    r1.addItem("table", "It is made of oak. A golden key rests on it.")
    

    # add exits to room 2
    r2.addExit("west", r1)
    r2.addExit("south", r4)
    

    #adds vacuum to list of grabbables
    r2.addGrabbable("vacuum")

    # add items to room 2
    r2.addItem("rug", "It is nice and Indian. It also needs to be vacuumed.")
    r2.addItem("fireplace", "It is full of ashes.")
    r2.addItem("vacuum", "It's just an ordinary vacuum.")

    # add exits to room 3
    r3.addExit("north", r1)
    r3.addExit("east", r4)

    # add grabbables to room 3
    r3.addGrabbable("book")

    # add items to room 3
    r3.addItem("bookshelves", "They are empty. Go figure.")
    r3.addItem("statue", "There is nothing special about it.")
    r3.addItem("desk", "The statue is resting on it. So is a book.")
    

    # add exits to room 4
    r4.addExit("north", r2)
    r4.addExit("west", r3)
    r4.addExit("south", None)  # DEATH!

    # add grabbables to room 4
    r4.addGrabbable("6-pack")

    # add items to room 4
    r4.addItem("brew_rig", "Gourd is brewing some sort of oatmeal stout on the brew rig. A 6-pack is resting beside it.")
    
    
    #adds exits to room 5
    r5.addExit("up", r2)

    #adds items to room 5
    r5.addItem("mad-man", "'Hello young one, I am in search of my potion book and a 6-pack of secret formula. I would get the items myself but..."
               "\nI had a business deal go wrong and ended up shoved in this room and locked away ever since. I sure could use your help.'")

    # set room 1 as the current room at the beginning of the game
    currentRoom = r1
    return currentRoom, r2, r5

#code for death display if the player exits the wrong spot in room 4
def death():   
    print(" " * 17 + "u" * 7)
    print(" " * 13 + "u" * 2 + "$" * 11 + "u" * 2)
    print(" " * 10 + "u" * 2 + "$" * 17 + "u" * 2)
    print(" " * 9 + "u" + "$" * 21 + "u")
    print(" " * 8 + "u" + "$" * 23 + "u")
    print(" " * 7 + "u" + "$" * 25 + "u")
    print(" " * 7 + "u" + "$" * 25 + "u")
    print(" " * 7 + "u" + "$" * 6 + "\"" + " " * 3 + "\"" + "$" * 3 +
    "\"" + " " * 3 + "\"" + "$" * 6 + "u")
    print(" " * 7 + "\"" + "$" * 4 + "\"" + " " * 6 + "u$u" + " " * 7
    + "$" * 4 + "\"")
    print(" " * 8 + "$" * 3 + "u" + " " * 7 + "u$u" + " " * 7 + "u" +
    "$" * 3)
    print(" " * 8 + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3 + "u" + "" * 6 + "u" + "$" * 3)
    print(" " * 9 + "\"" + "$" * 4 + "u" * 2 + "$" * 3 + " " * 3 +
    "$" * 3 + "u" * 2 + "$" * 4 + "\"")
    print(" " * 10 + "\"" + "$" * 7 + "\"" + " " * 3 + "\"" + "$" * 7
    + "\"")
    print(" " * 12 + "u" + "$" * 7 + "u" + "$" * 7 + "u")
    print(" " * 13 + "u$\"$\"$\"$\"$\"$\"$u")
    print(" " * 2 + "u" * 3 + " " * 8 + "$" * 2 + "u$ $ $ $ $u" + "$"
    * 2 + " " * 7 + "u" * 3)
    print(" u" + "$" * 4 + " " * 8 + "$" * 5 + "u$u$u" + "$" * 3 + " " * 7 + "u" + "$" * 4)
    print(" " * 2 + "$" * 5 + "u" * 2 + " " * 6 + "\"" + "$" * 9 +
    "\"" + " " * 5 + "u" * 2 + "$" * 6)
    print("u" + "$" * 11 + "u" * 2 + " " * 4 + "\"" * 5 + " " * 4 +
    "u" * 4 + "$" * 10)
    print("$" * 4 + "\"" * 3 + "$" * 10 + "u" * 3 + " " * 3 + "u" * 2
    + "$" * 9 + "\"" * 3 + "$" * 3 + "\"")
    print(" " + "\"" * 3 + " " * 6 + "\"" * 2 + "$" * 11 + "u" * 2 +
    " " + "\"" * 2 + "$" + "\"" * 3)
    print(" " * 11 + "u" * 4 + " \"\"" + "$" * 10 + "u" * 3)
    print(" " * 2 + "u" + "$" * 3 + "u" * 3 + "$" * 9 + "u" * 2 +
    " \"\"" + "$" * 11 + "u" * 3 + "$" * 3)
    print(" " * 2 + "$" * 10 + "\"" * 4 + " " * 11 + "\"\"" + "$" *
    11 + "\"")
    print(" " * 3 + "\"" + "$" * 5 + "\"" + " " * 22 + "\"\"" + "$" *
    4 + "\"\"")
    print(" " * 5 + "$" * 3 + "\"" + " " * 25 + "$" * 4 + "\"")
    19
# Main
inventory = []
currentRoom, room2, r5 = createRooms()
#changes state of a cleaned rug for later use
rugCleaned = False
#game intro/instructions to begin adventure
print("===============================================================================================================================================")
print("Welcome to the mad-man's mansion. You've come here to earn enough money to pay your student debt of $10000."
      "\nYour only instructions are to navigate the mansion and find a way to make the money. Your actions are"
      "\nall based on two-word responses. You can 'go', 'take', and 'look'. The second word of your response will always"
      "\nbe a noun or exit present in the room. Examples of valid actions in room 1 are 'go east' or 'look chair'. In addition,"
      "\nthere are stipulations to the 'take' action. Only grabbable items can be taken. If an item is unable to be taken you will"
      "\nbe given an error message. The same goes for looking and leaving invalid items and locations. Use these actions to help you"
      "\nnavigate the mansion. To leave the game early type: 'quit', 'exit', or 'bye'. Good Luck!")


# play forever (well, at least until the player dies or asks to quit)
while True:
    # set the status so the player has situational awareness
    # the status has room and inventory information
    status = "{}\nYou are carrying: {}\n".format(currentRoom, inventory)

    # if the current room is None, then the player is dead
    # this only happens if the player goes south when in room 4
    if currentRoom is None:
        status = "You are dead."


    # display the status
    print("===============================================================================================================================================")
    print(status)

    # if the current room is None (and the player is dead), exit the game
    if currentRoom is None:
        death()
        break
    #displays victory message if the player successfully completes the game
    if "$10000" in inventory:
        print("You've beat the game. Thanks for playing.\nGAME OVER")
        break

    # prompt for player input
    # the game supports a simple language of <verb> <noun>
    # valid verbs are go, look, and take
    action = input("What to do? ")
    # set the user's input to lowercase to make it easier to compare
    # the verb and noun to known values
    action = action.lower()

    # exit the game if the player wants to leave (supports quit, exit, and bye)
    if action == "quit" or action == "exit" or action == "bye":
        print("Leaving so soon? Better luck next time.")
        break


    # set a default response
    response = "I don't understand. Try verb noun. Valid verbs are go, look, and take"

    # split the user input into words (words are separated by spaces)
    words = action.split()

    # the game only understands two-word inputs
    if len(words) == 2:
        # isolate the verb and noun
        verb = words[0]
        noun = words[1]

        # the verb is: go
        if verb == "go":
            # set a default response
            response = "Invalid exit."

            # check for valid exits in the current room
            for i in range(len(currentRoom.exits)):
                # a valid exit is found
                if noun == currentRoom.exits[i]:
                    # change the current room to the one that is
                    # associated with the specified exit
                    currentRoom = currentRoom.exitLocations[i]
                    # set the response (success)
                    response = "Room changed."
                    # no need to check any more exits
                    break
            else:
                response = "Invalid exit. Try a different direction."

        # the verb is: look
        elif verb == "look":
            # set a default response
            response = "I don't see that item."


            #code that opens the passage for the player if the key is in their possesion
            if noun == "passage" and "key" in inventory:
                currentRoom.modifyItemDescription("passage", "The key fits the lock and opens a new exit underground.")
                currentRoom.cleanRug()
            #set of rules that determine the mad-man's response based on what the player has to offer him -also gives the required items to the man in exchange for money
            if noun == "mad-man" and "book" in inventory and "6-pack" in inventory:
                currentRoom.modifyItemDescription("mad-man", "'Wow young one! You possess both of the items I've been looking for. I am so grateful. I planned on using this money for a business deal but I have no use for it now. \nI hope you'll accept this reward'.\n{*he hands you a wad of cash}")
                inventory.remove("book")
                inventory.remove("6-pack")
                inventory.append("$10000")
            if noun == "mad-man" and "book" in inventory and "6-pack" not in inventory:
                currentRoom.modifyItemDescription("mad-man", "'Thanks young one. You don't know how much I needed this. All I need now is the 6-pack of formula.'")
            if noun == "mad-man" and "6-pack" in inventory and "book" not in inventory:
                currentRoom.modifyItemDescription("mad-man", "'Thanks young one. You don't know how much I nedded this. All I need now is the book.'")
            # check for valid items in the current room
            for i in range(len(currentRoom.items)):
                # a valid item is found
                if noun == currentRoom.items[i]:
                    # set the response to the item's description
                    response = currentRoom.itemDescriptions[i]
                    # no need to check any more items
                    break

        # the verb is: take
        elif verb == "take":
            # set a default response if the player cannot take an item.
            response = f"You can't take {noun}."

            #informs player that they've already grabbed their intended item
            if noun in inventory:
                response = f"You've already grabbed {noun}."
            if noun == "vacuum" and rugCleaned:
                response = f"You've already used the vacuum to clean the rug."

            # check for valid grabbable items in the current room
            for grabbable in currentRoom.grabbables:
                # a valid grabbable item is found
                if noun == grabbable:
                    # add the grabbable item to the player's inventory
                    inventory.append(grabbable)
                    # remove the grabbable item from the room
                    currentRoom.delGrabbable(grabbable)

                    # set the response (success)
                    response = "Item Grabbed"

                    #checks if item is removed from room and placed in inventory
                    if "key" in inventory:
                        #updates the room to match the removal of grabbable items
                        currentRoom.modifyItemDescription("table", "It is made of oak. It used to have a golden key on it.")
                    if "book" in inventory:
                        currentRoom.modifyItemDescription("desk", "The statue is resting on it. You took the book.")
                    if "6-pack" in inventory:
                        currentRoom.modifyItemDescription("brew_rig", "Gourd is still there, but the 6-pack is now in your possession.")
                    #allows the player the ability to clean the rug and reveal a new room
                    if "vacuum" in inventory:
                        rugCleaned = True
                        print("\nYou use the vacuum to clean the rug and notice an odd square impression under the rug. You move the rug and reveal"
                              " a locked underground passage.")
                        currentRoom.modifyItemDescription("rug", "The rug is cleaned and out of the way. In its place rests an interesting passage.")
                        currentRoom.removeItem("vacuum")
                        #automatically unlocks passage if key is in possession
                        if "key" in inventory and rugCleaned:
                            currentRoom.cleanRug()
                            print("The key fits perfectly and unlocks the underground passage.")
                        #gives guidance/hint to player so they can enter the passage
                        if "key" not in inventory and rugCleaned:
                            print("Something tells you there's a key that unlocks this passage somewhere in this mansion.")
                            currentRoom.addItem("passage", "Requires key to access.")
                        
                
                    
                    
                    
                        

                    # no need to check any more grabbable items
                    break



        # display the response
        print("\n{}".format(response))








