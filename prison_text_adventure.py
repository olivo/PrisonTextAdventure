
class GameState:
    def __init__(self):
        self.inventory = list()
        self.solved = False
        self.bed_state = 0
        self.basin_state = 0
        self.other_prisoners_state = 0
        self.other_basin_state = 0
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
            print "You have a bed with some sheets."
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
                print "Unreconized choice."
                self.inspect_bed()
        else:
            print "You have an empty bed."

    def inspect_basin(self):
        if self.basin_state == 0:
            print "There is a soap bar in the basin."
            print "What would you like to do?"
            print "1. Take soap bar."
            print "2. See inventory."
            print "3. Go back to cell."

            choice = raw_input("> ")
            
            if choice == "1":
                self.inventory.append("soap bar")
                self.basin_state = 1
            if choice == "2":
                self.print_inventory()
            elif choice != "3":
                print "Unreconized choice."
                self.inspect_basin()
        else:
            print "The basin is empty."

    def inspect_toilet(self):
        print "The toilet is dirty."
        print "What would you like to do?"
        
        if "sheets" in self.inventory:
            print "1. Drench sheets in toilet."
            print "2. See inventory."
            print "3. Go back to cell."

            choice = raw_input("> ")
            
            if choice == "1":
                self.inventory.remove("sheets")
                self.inventory.append("dirty sheets")
                print "The sheets are now dirty, and hard to see."
            if choice == "2":
                self.print_inventory()
            elif choice != "3":
                print "Unreconized choice."
                self.inspect_toilet()
        else:
            print "1. See inventory."
            print "2. Go back to cell."

            choice = raw_input("> ")
            
            if choice == "1":
                self.print_inventory()
            elif choice != "2":
                print "Unreconized choice."
                self.inspect_toilet()

    def inspect_other_prisoners(self):
        if self.other_prisoners_state == 0:
            print "There are two prisoners fighting."
        else:
            print "One of the prisoners choked the other one to death."

    def inspect_other_basin(self):

        if self.other_basin_state == 0:
            print "There is a basin in the other cell with a conspicuous handle."
            if "sheets" in self.inventory or "dirty sheets" in self.inventory:
                print "What do you want to do?"
                print "1. Throw one extreme of the sheets against the basin in the adjacent cell?"
                print "2. See inventory."
                print "3. Go back to cell."
                
                choice = raw_input("> ")
                
                if choice == "1":
                    print "The other side of the sheets becomes locked on the basin."
                    print "As you tigthen the sheets on your side, you form a rope trap at the entrance of the other cell."
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
            print "There is a tight sheet forming a rope trap at the entrance of the other cell."
        elif self.other_basin_state == 2:
            print "There is a tight dark sheet forming a rope trap at the entrance of the other cell."

    def inspect_key(self):
        if "key" in self.inventory:
            print "You have the key in your pocket."
        elif self.key_state == 0:
            print "The guard outside the cell has the key to your cell."
        else:
            print "The key is in the floor of your cell."
            print "What would you like to do?"
            print "1. Pick up key."
            print "2. See inventory."
            
            choice = raw_input("> ")
            
            if choice == "1":
                inventory.append("key")
            elif choice == "2":
                self.print_inventory()
            else:
                print "Unrecognized choice."
                self.inspect_key()

    def scream(self):
        print "You scream 'FIRE!!!' like crazy"
        print "The guard looks around your cell and the adjacent cell."

        if self.other_prisoners_state == 0:

            print "The guard doesn't mind the other prisoners fighting."
            print "The guard tells you to shut up."
        else:
            print "The guard notices one of the prisoners is lying on the floor in the adjacent cell."
            print "The guard approaches the adjacent cell."
# Finish handling of adjacent basin state.
            if self.other_basin_state == 0:
                print "The guard sends one of the prisioners to detainment, and the other to the hospital."
                print "The guard has some other guards bring two new prisioners to the adjacent cell."
            elif self.other_basin_state == 1:
                print "The guard notices something suspicious in the entrance: your rope tra."
                print "Before he gets too close to the gate, you manage to disassembe the trap."
                print "You put the sheets back in the bed."
                self.bed_state = 0
                print "The guard sends one of the prisioners to detainment, and the other to the hospital."
                print "The guard has some other guards bring two new prisioners to the adjacent cell."
            else:
                print "The guard enters the adjacent cell."
                print "The guard trips on the trap, lies unconscious on the floor, and drops a key in your cell."
                self.key_state = 1

    def inspect_gate(self):
        if "key" in self.inventory:
            print "The gate is locked."
            print "What would you like to do?"
            
            print "1. Use key."
            print "2. See inventory."
            print "3. Go back to cell."

            choice = raw_input("> ")

            if choice == "1":
                print "You unlock the cell!"
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

        print "You are in a cell."
        print "What would you like to do?"

        print "1. Inspect bed."
        print "2. Inspect basin."
        print "3. Inspect toilet."
        print "4. Inspect prisoners in adjacent cell"
        print "5. Inspect basin in adjacent cell."
        print "6. Inspect key."
        print "7. Scream 'FIRE!!!'"
        print "8. Inspect cell gate."
        
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
        else:
            print "Unrecognized choice."


print "You are in a prison cell."

game_state = GameState()

while not game_state.solved:
    game_state.select_cell_choice()
    
