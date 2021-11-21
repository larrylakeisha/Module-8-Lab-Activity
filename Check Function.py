# Lakeisha Larry
# November 21, 2021

# Program 5 uses function to check if player has collected items.

class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_model(self):
        return self.nickname

    def get_year(self):
        return self.weapons

    def get_color(self):
        return self.weaknesses

    def profile(self):
        return self.nickname, self.weapons, self.weaknesses


def check_equipment(Task):
    print("This functions is to check if items are collected and their condition")


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

# call check equipment
check_equipment('task1')
