# Lakeisha Larry
# November 21, 2021

# Program 5 uses function to check if player has collected items.

class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_nickname(self):
        return self.nickname

    def get_weapons(self):
        return self.weapons

    def get_weaknesses(self):
        return self.weaknesses

    def profile(self):
        return self.nickname, self.weapons, self.weaknesses

'''
The following functionhas parameters: player(character object), taskL(item list), status(not allowed state)
missed variable is for counting the number the player doesn't have for performing the chosen task.
Whenever the item is not found in the player's weapons list, the missed will be incremented.

'''
def check_equipment(player, taskL, status): 
    print("This functions is to check if items are collected and their condition")
    weaponL = player.get_weapons()
    missed =0
    for item in range(len(taskL)):
        if taskL[item] not in weaponL:
           print('{} is not ready.'.format(taskL[item]))
           missed = missed+1
    '''
    Player has all items to carry out the task if missed is still zero after for loop is fully iterated.
    '''
    if missed == 0:
        print('All items are ready for carrying out the task')
    '''
    If the not_allowed_state is not found in the player's weaknesses list,
    then the player is Ok condition for performing the task.
    '''
    if status in player.get_weaknesses():
        print("Player's {} condition is not allowed.".format(status))
    else:
        print('Player is good condition to carrying out the task.')

        
        
player1 = character('', '', '')
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']
for item in player1.weapons:
    print("Item: ", item)

for debuff in player1.weaknesses:
    print("Debuff: ", debuff)

print("You can choose three tasks.")
print("1. Task 1 - Climb a mountain")
print("2. Task 2 - Cook a meal.")
print("3. Task 3 - Write a book.")
option = input("Please choose option (1-3).")

if option == "1":
    task = ['rope', 'coat', 'first aid kit']
    not_allowed_state = 'slow'

if option == "2":
    task = ['pan', 'groceries']
    not_allowed_state = 'small'

if option == "3":
    task = ['pen', 'paper', 'idea']
    not_allowed_state = 'confusion'

# check with for loop with
# for i in range (len( task )
# if task(i) is not in player weapons
# display the option menu
# input option for task

# call check equipment, you need to pass the following parameters.
check_equipment(player1, task, not_allowed_state)
