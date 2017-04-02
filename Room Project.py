###########################################################################################
# Name: Parker Sikes and Kyle Morales
# Date: 3/24/17
# Description: Room Assignment
###########################################################################################
from Tkinter import *

# the room class
# note that this class is fully implemented with dictionaries as illustrated in the lesson "More on Data Structures"
class Room(object):
    # the constructor
    def __init__(self, name, image):
        # rooms have a name, an image (the name of a file), exits (e.g., south), exit locations
        # (e.g., to the south is room n), items (e.g., table), item descriptions (for each item),
        # and grabbables (things that can be taken into inventory)
        self.name = name
        self.image = image
        self.exits ={}
        self.items = {}
        self.grabbables = []

    # getters and setters for the instance variables
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    # adds an exit to the room
    # the exit is a string (e.g., north)
    # the room is an instance of a room
    def addExit(self, exit, room, locked):
        # append the exit and room to the appropriate dictionary
        self._exits[exit] = [room, locked]

    # adds an item to the room
    # the item is a string (e.g., table)
    # the desc is a string that describes the item (e.g., it is made of wood)
    def addItem(self, item, desc, usage):
        # append the item and description to the appropriate dictionary
        self._items[item] = [desc, usage]

    # adds a grabbable item to the room
    # the item is a string (e.g., key)
    def addGrabbable(self, item):
        # append the item to the list
        self._grabbables.append(item)

    # removes a grabbable item from the room
    # the item is a string (e.g., key)
    def delGrabbable(self, item):
        # remove the item from the list
        self._grabbables.remove(item)

    # returns a string description of the room
    def __str__(self):
        # first, the room name
        s = "You are in {}.\n".format(self.name)

        # next, the items in the room
        s += "You see: "
        for item in self.items.keys():
            s += item + " "
        s += "\n"

        # next, the exits from the room
        s += "Exits: "
        for exit in self.exits.keys():
            s += exit + " "

        return s

# the game class
# inherits from the Frame class of Tkinter
class Game(Frame):
    # the constructor
    def __init__(self, parent):
        # call the constructor in the superclass
        Frame.__init__(self, parent)

    # creates the rooms
    def createRooms(self):
        global currentRoom
        global r8
        global r9

        r1 = Room("Room 1")
        r2 = Room("Room 2")
        r3 = Room("Room 3")
        r4 = Room("Room 4")
        r5 = Room("Room 5")
        r6 = Room("Room 6")
        r7 = Room("Room 7")
        r8 = Room("Room 8")
        r9 = Room("Room 9")
        r10 = Room("Room 10")

        r1.addExit("east", r2, "True")
        r1.addExit("south", r3, "True")
        r1.addGrabbable("key")
        r1.addItem("chair", "It is made of wicker and no one is sitting on it", "I could sit, but I don't think I fit.")
        r1.addItem("table", "It is made of oak, a golden key rests on it", "A sturdy table, perhaps a book might fit on it.")

        r2.addExit("west", r1, "False")
        r2.addExit("south", r4, "False")
        r2.addItem("fireplace", "It is full of ashes", "Why clean out the ashes? It's not your job is it?")

        r3.addExit("north", r1, "False")
        r3.addExit("east", r4, "False")
        r3.addGrabbable("book")
        r3.addItem("desk", "A book rests on the desk", "The History of Pepe, the Nigerian Prince.")

        r4.addExit("north", r2, "False")
        r4.addExit("west", r3, "False")
        r4.addExit("south", None, "True")
        r4.addExit("staircase", r5, "False")
        r4.addGrabbable("6-pack")
        r4.addItem("distillery", "Look's like Gourd's been busy.", "Best to leave this alone.")
        r4.addItem("door", "It's locked, looks like there is a keyhole.", "It's locked, looks like there is a keyhole.")
        r4.addItem("staircase", "It looks like it goes up a floor.", "Leads to the second floor.")

        r5.addExit("staircase", r4, "False")
        r5.addExit("north", r6, "False")
        r5.addGrabbable("cheese_soup")
        r5.addItem("soup_dispenser", "It looks like it produces some sort of soup", "cheese_soup has been made, eat it soon!")

        r6.addExit("south", r5, "False")
        r6.addExit("west", r7, "False")
        r6.addItem("statue", "There is a button that can be pressed.", "As the statue crumbles, the sounds of a ladder appearing seem to come from Room 8.")

        r7.addExit("east", r6, "False")
        r7.addExit("south", r8, "False")
        r7.addItem("sofa", "This sofa looks really worn, there is dust everywhere.", "You could rest here, but you should be more worried about getting out of here.")
        r7.addItem("study", "There's a note on the desk. Perhaps this could come in handy.", "It's hard to read the note from here. You should take it for future reference.")
        r7.addGrabbable("note")

        r8.addExit("north", r7, "False")
        r8.addItem("lamp", "The lamp looks really old.", "Not really anything that this thing contributes to getting the heck out of here.")

        r9.addExit("ladder", r8, "False")
        r9.addExit("north", r10, "False")
        r9.addItem("dusty_trinkets", "Wow, whoever lives in this house must have been rich, there's a lot of antique stuff laying around!", "Nothing of use lies in the pile of goods.")

        r10.addExit("south", r9, "False")
        r10.addItem("dusty_computer", "I wonder who threw this computer away? Wait... as I look closer I see faint letters written on it... oh wait it's actually a Mac. Nevermind.", "Let's be real, there are no uses for a Mac.")
        r10.addGrabbable("second_key")
        r10.addItem("old_desk", "On it rests a dusty_computer and the second_key.", "Perhaps the key that rests here is for the door in Room 4.")

        currentRoom = r1

    def addLadder():                    #This creates the exit in room 8 that allows access to the second_key and the end of the game.

        global r8
        global r9

        r8.addExit("ladder", r9, "False")


    # sets up the GUI
    def setupGUI(self):
        #organize the GUI
        self.pack(fill=BOTH, expand = 1)
        """
        setup the player input at the bottom of the GUI
        sets the background to white and binds the return
        key to the process function in the class
        """
        Game.player_input = Entry(self, bg="white")
        Game.player_input.bind(("<Return>"), self.process)
        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()

        #setup the image to the left of the GUI
        img = None
        Game.image = Label(self, width=WIDTH / 2, image = img)
        Game.image.image = img
        Game.image.pack(side=LEFT, fill = Y)
        game.image.pack_propagate(False)

        #setup the text on the right of the GUI
        text_frame = Frame(self, width=WIDTH / 2)
        Game.text = Text(text_frame, bg="lightgrey", state=DISABLED)
        Game.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)

    # sets the current room image
    def setRoomImage(self):
        if (Game.currentRoom == None):
            Game.img = PhotoImage(file="skull.gif")
        else:
            Game.img = PhotoImage(file=Game.currentRoom.image)

        Game.image.config(image=Game.image)
        Game.image.image = Game.img

    # sets the status displayed on the right of the GUI
    def setStatus(self, status):
        #Enables the text, clears it, sets it, and finally disables it
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)
        if (Game.currentRoom == None):
            Game.text.insert(END, "You are dead. The only thing you can do now is quit.\n")
        else:
            Game.text.insert(END, str(Game.currentRoom) +\
                "\n You are carrying: " + str(Game.inventory) +\
                "\n\n" + status
        Game.text.config(state=DISABLED)

    # plays the game
    def play(self):
        # add the rooms to the game
        self.createRooms()
        # configure the GUI
        self.setupGUI()
        # set the current room
        self.setRoomImage()
        # set the current status
        self.setStatus("")

    # processes the player's input
    def process(self, event):
        action = Game.player_input.get()
        action = action.lower()
        response = "I don't understand. Try (Verb) (Noun). Valid verbs are go, look, use, and take."

    words = action.split()

    #makes sure user can only type 2 words
    if (len(words) == 2):

        verb = words[0]
        noun = words[1]

        #adds functionality to "go" verb
        if (verb == "go"):
            response = "Invalid exit."

			if noun in Game.currentRoom.exits:

                if Game.currentRoom.exits[noun][1] == "True":
                    response = "The door is locked."

                else:

                    Game.currentRoom = Game.currentRoom.exits[noun][0]
                    response = "Room Changed."


    #functionality for "look" verb
        elif (verb == "look"):

            response = "I don't see that item."

			if noun in Game.currentRoom.items:

				response = Game.currentRoom.items[noun][0]

    #functionality for "take" verb
        elif (verb == "take"):

            response = "I don't see that item"
            for i in range(len(Game.currentRoom.grabbables)):

                if (noun == Game.currentRoom.grabbables[i]):

                    inventory.append(noun)
                    currentRoom.delGrabbable(i)
                    response = "Item grabbed."
                    break

    #functionality for "use" verb
        elif (verb == "use"):

            response = ("This item has no uses. Only items in the room or your inventory can be used.")

        	if noun in Game.currentRoom.items
        #these two if statements allow the ladder puzzle on floor 2 to function
                if (noun == "statue"):
                    addLadder()
					response = Game.currentRoom.items[noun][1]
					del Game.currentRoom.items[noun]

        #this is so that the program knows what response to use according to the list of items in current room.
				else:
					response = Game.currentRoom.items[noun][1]

        #adds functionality of using either key in room 1 and room 4
            if (noun == "key") and (Game.currentRoom == "Room 1" or "Room 4"):

				Game.currentRoom.exits["south"][1] = "False"
                Game.currentRoom.exits["east"][1] = "False"
                inventory.remove("key")
                response = "The doors are open"

            if (noun == "second_key") and (Game.currentRoom == "Room 1" or "Room 4"):

                Game.currentRoom.exits["south"][1] = "False"
                inventory.remove("second_key")
                response = "The locked door is open"

        #this is so the note can be used at any time regardless of whatever room the user is in.
            if (noun == "note"):

                response = "It's hard to discern what the note says, but it mentions something about the statue in room 6 and room 8."

    print response


##########################################################
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600

# create the window
window = Tk()
window.title("Room Adventure")

# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()

# wait for the window to close
window.mainloop()
