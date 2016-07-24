
class GameState:
    def __init__(self):
        self.inventory = list()
        self.solved = False
        self.bed_state = 0
        self.basin_state = 0
        self.other_prisoners_state = 0
        self.other_basin_state = 0
        self.corner_floor_state = 0
        self.key_state = 0

    def print_inventory(self):
        if len(self.inventory) == 0:
            print "You have no items."
        else:
            print "You have the following items:"
            for item in self.inventory:
                print item
        print "\n"

    def inspect_bed(self):
        if self.bed_state == 0:
            print "\nYou have a bed with some sheets.\n"
            print "What would you like to do?"
            print "1. Take sheets."
            print "2. See inventory."
            print "3. Go back to cell."

            choice = raw_input("> ")
            
            if choice == "1":
                self.inventory.append("sheets")
                self.bed_state = 1
            if choice == "2":
                self.print_inventory()
            elif choice != "3":
                print "Unrecognized choice."
                self.inspect_bed()
        else:
            print "\nYou have an empty bed.\n"

    def inspect_basin(self):
        if self.basin_state == 0:
            print "\nThere is a soap bar in the basin.\n"
            print "\nThere is a water cup in the basin.\n"

            print "What would you like to do?"
            print "1. Take soap bar."
            print "2. Take water cup."
            print "3. See inventory."
            print "4. Go back to cell."

            choice = raw_input("> ")
            
            if choice == "1":
                self.inventory.append("soap bar")
                self.basin_state = 1
            elif choice == "2":
                self.inventory.append("water cup")
                self.basin_state = 2
            elif choice == "3":
                self.print_inventory()
            elif choice != "4":
                print "Unrecognized choice."
                self.inspect_basin()

        elif self.basin_state == 1:
            print "\nThere is a water cup in the basin.\n"

            print "What would you like to do?"
            print "1. Take water cup."
            print "2. See inventory."
            print "3. Go back to cell."

            choice = raw_input("> ")
            
            if choice == "1":
                self.inventory.append("water cup")
                self.basin_state = 3
            elif choice == "2":
                self.print_inventory()
            elif choice != "3":
                print "Unrecognized choice."
                self.inspect_basin()

        elif self.basin_state == 2:

            print "\nThere is a soap bar in the basin.\n"

            print "What would you like to do?"
            print "1. Take soap."
            print "2. Fill water cup with water."
            print "3. See inventory."
            print "4. Go back to cell."

            choice = raw_input("> ")

            if choice == "1":
                self.inventory.append("soap")
                self.basin_state = 3
            elif choice == "2":
                if "filled water cup" in self.inventory:
                    print "Your water cup is already completely full."
                    return None
                else:
                    self.inventory.remove("water cup")
                    self.inventory.append("filled water cup")
                    self.basin_state = 2
            elif choice == "3":
                self.print_inventory()
            elif choice != "4":
                print "Unrecognized choice."
                self.inspect_basin()

        elif self.basin_state == 3:

            print "What would you like to do?"
            print "1. Fill water cup with water."
            print "2. See inventory."
            print "3. Go back to cell."

            choice = raw_input("> ")

            if choice == "1":
                if "filled water cup" in self.inventory:
                    print "Your water cup is already completely full."
                    return None
                else:
                    self.inventory.remove("water cup")
                    self.inventory.append("filled water cup")
                    self.basin_state = 2
            elif choice == "2":
                self.print_inventory()
            elif choice != "3":
                print "Unrecognized choice."
                self.inspect_basin()


    def inspect_toilet(self):
        print "\nThe toilet is dirty.\n"
        print "What would you like to do?"
        
        if "sheets" in self.inventory:
            print "1. Drench sheets in toilet."
            print "2. See inventory."
            print "3. Go back to cell."

            choice = raw_input("> ")
            
            if choice == "1":
                self.inventory.remove("sheets")
                self.inventory.append("dirty sheets")
                print "\nThe sheets are now dirty, and hard to see.\n"
            elif choice == "2":
                self.print_inventory()
            elif choice != "3":
                print "Unrecognized choice."
                self.inspect_toilet()
        else:
            print "1. See inventory."
            print "2. Go back to cell."

            choice = raw_input("> ")
            
            if choice == "1":
                self.print_inventory()
            elif choice != "2":
                print "Unrecognized choice."
                self.inspect_toilet()

    def inspect_other_prisoners(self):
        if self.other_prisoners_state == 0:
            print "\nThere are two prisoners fighting.\n"
            
            if "soap bar" in self.inventory:
                print "What whould you like to do?"
                print "1. Throw soap bar to the adjacent cell."
                print "2. See inventory."
                print "3. Go back to cell."
                
                choice = raw_input("> ")

                if choice == "1":
                    print "\nThe soap bar lands near the fighting prisoners."
                    print "One of the prisoners slips on the soap bar."
                    print "The other prisoner starts to overpower him.\n"
                    self.other_prisoners_state = 1
                elif choice == "2":
                    self.print_inventory()
                elif choice != "3":
                    print "Unrecognized choice."
            
        else:
            print "\nOne of the prisoners choked the other one to death.\n"

    def inspect_other_basin(self):

        if self.other_basin_state == 0:
            print "\nThere is a basin in the other cell with a conspicuous handle.\n"
            if "sheets" in self.inventory or "dirty sheets" in self.inventory:
                print "What do you want to do?"
                print "1. Throw one extreme of the sheets against the basin in the adjacent cell?"
                print "2. See inventory."
                print "3. Go back to cell."
                
                choice = raw_input("> ")
                
                if choice == "1":
                    print "\nThe other side of the sheets becomes locked on the basin."
                    print "As you tigthen the sheets on your side, you form a rope trap at the entrance of the other cell.\n"
                    if "sheets" in self.inventory:
                        self.inventory.remove("sheets")
                        self.other_basin_state = 1
                    else:
                        self.inventory.remove("dirty sheets")
                        self.other_basin_state = 2
                elif choice == "2":
                    self.print_inventory()
                elif choice != "3":
                    print "Unrecognized choice"
                    self.inspect_other_basin()
        elif self.other_basin_state == 1:
            print "\nThere is a tight sheet forming a rope trap at the entrance of the other cell.\n"
        elif self.other_basin_state == 2:
            print "\nThere is a tight dark sheet forming a rope trap at the entrance of the other cell.\n"

    def inspect_key(self):
        if "key" in self.inventory:
            print "\nYou have the key in your pocket.\n"
        elif self.key_state == 0:
            print "\nThe guard outside the cell has the key to your cell.\n"
        else:
            print "The key is in the floor of your cell."
            print "What would you like to do?"
            print "1. Pick up key."
            print "2. See inventory."
            
            choice = raw_input("> ")
            
            if choice == "1":
                self.inventory.append("key")
            elif choice == "2":
                self.print_inventory()
            else:
                print "Unrecognized choice."
                self.inspect_key()

    def scream(self):
        print "\nYou scream 'FIRE!!!' like crazy"
        print "The guard looks around your cell and the adjacent cell.\n"

        if self.other_prisoners_state == 0:

            print "The guard doesn't mind the other prisoners fighting."
            print "The guard tells you to shut up.\n"
        else:
            print "The guard notices one of the prisoners is lying on the floor in the adjacent cell."
            print "The guard approaches the adjacent cell.\n"
# Finish handling of adjacent basin state.
            if self.other_basin_state == 0:
                print "The guard sends one of the prisioners to detainment, and the other to the hospital."
                print "The guard has some other guards bring two new prisioners to the adjacent cell.\n"
            elif self.other_basin_state == 1:
                print "The guard notices something suspicious in the entrance: your rope trap."
                print "Before he gets too close to the gate, you manage to disassembe the trap."
                print "You put the sheets back in the bed.\n"
                self.bed_state = 0
                print "The guard sends one of the prisioners to detainment, and the other to the hospital."
                print "The guard has some other guards bring two new prisioners to the adjacent cell.\n"
            else:
                print "The guard enters the adjacent cell."
                print "The guard trips on the trap, lies unconscious on the floor, and drops a key in your cell.\n"
                self.key_state = 1

    def inspect_gate(self):
        if "key" in self.inventory:
            print "\nThe gate is locked.\n"
            print "What would you like to do?"
            
            print "1. Use key."
            print "2. See inventory."
            print "3. Go back to cell."

            choice = raw_input("> ")

            if choice == "1":
                print "\nYou unlock the cell!\n"
                print "===== YOU HAVE ESCAPED!!! ===="
                self.solved = True
            elif choice == "2":
                self.print_inventory()
            elif choice != "3":
                print "Unrecognized choice."
                self.inspect_gate()
        else:
            print "The gate is locked!"

    def select_cell_choice(self):

        print "\nYou are in a cell.\n"
        print "What would you like to do?"

        print "1. Inspect bed."
        print "2. Inspect basin."
        print "3. Inspect toilet."
        print "4. Inspect prisoners in adjacent cell"
        print "5. Inspect basin in adjacent cell."
        print "6. Inspect key."
        print "7. Scream 'FIRE!!!'"
        print "8. Inspect cell gate."
        print "9. See inventory."
        
        choice = raw_input("> ")

        if choice == "1":
            self.inspect_bed()
        elif choice == "2":
            self.inspect_basin()
        elif choice == "3":
            self.inspect_toilet()
        elif choice == "4":
            self.inspect_other_prisoners()
        elif choice == "5":
            self.inspect_other_basin()
        elif choice == "6":
            self.inspect_key()
        elif choice == "7":
            self.scream()
        elif choice == "8":
            self.inspect_gate()
        elif choice == "9":
            self.print_inventory()
        else:
            print "Unrecognized choice."


cell_game_state = GameState()

while not cell_game_state.solved:
    cell_game_state.select_cell_choice()
    

# Hallway scene.
# Need to get from the hallway to outside.
# You're in prisoners clothing.
# There are armed guards
# There are emergency medical services.
# You should disguise yourself to escape.
# You should knock someone out to make emergency services leave the room.

## You should stall one of the guys before he gets into the room so that
## it allows you enough time to get the coat and escape.

# You should find a way to distract the guards and emergency crew to be allowed
# to escape.

# You should open up the door to the outside. 
