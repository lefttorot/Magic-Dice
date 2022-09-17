import random
import time
# Magic dice - Kakegurui Twin

# rolls dice
def roll_die(color):
    roll = random.choice(color)
    return roll


# Generates a die face in terminal
def generate_dice_face_diagram(dice_value):
    dice_face = [DICE_ART[dice_value]]
    dice_face_rows = get_dice_face(dice_face)

    # Generate header with the word "RESULTS" centered
    width = len(dice_face_rows[0])
    diagram_header = " RESULTS ".center(width, "~")

    dice_faces_diagram = "\n".join([diagram_header] + dice_face_rows)
    return dice_faces_diagram


# creates die face
def get_dice_face(dice_face):
    # Generate a list containing the dice faces rows
    dice_faces_rows = []
    for row_idx in range(DIE_HEIGHT):
        row_components = []
        for die in dice_face:
            row_components.append(die[row_idx])
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)
    return dice_faces_rows


# Prints color that you and dealer chose
def die_color_printer(player, players_num):
    if player == "you":
        if players_num == 1:
            print("You chose Black")
        elif players_num == 2:
            print("You chose White")
        elif players_num == 3:
            print("You chose Red")
    elif player == "pc":
        if players_num == 1:
            print("Dealer chose Black")
        elif players_num == 2:
            print("Dealer chose White")
        elif players_num == 3:
            print("Dealer chose Red")


# Prints menu for user to pick die
def menu_printer():
    print("Black contains 3, 3, 4, 4, 8, 8: Enter 1 ")
    print("White contains 1, 1, 5, 5, 9, 9: Enter 2 ")
    print("  Red contains 2, 2, 6, 6, 7, 7: Enter 3 ")
    while True:
        number = int(input("Choose a die: "))
        if number == "1" or "2" or "3":
            break
        else:
            print("Invalid")
    return number


# function to calculate your dice role result
def generate_my_result():
    number = menu_printer()
    die_color_printer("you", number)
    your_value = roll_die(die_types[number])
    return generate_dice_face_diagram(your_value), your_value


# calculates dealer's dice role result
def generate_dealer_result():
    number = random.randint(1, 3)
    time.sleep(0.5)
    die_color_printer("pc", number)
    pc_value = roll_die(die_types[number])
    time.sleep(2)
    return generate_dice_face_diagram(pc_value), pc_value


# Bet function so player can bet money
def bet(money, string, guest_account, dealer_account):
    if string == "Dealer wins":
        dealer_account.account_balance += money
        guest_account.account_balance -= money
    elif string == "You win":
        guest_account.account_balance += money
        dealer_account.account_balance -= money


# Prints your balance
def bet_printer(guest_account, dealer_account):
    print("Your balance: $" + str(guest_account.account_balance))


# Base account class for player's and dealer's account
class Account:
    def __init__(self):
        self.account_balance = 0.0

    def add(self, money):
        self.account_balance += money

    def deduct(self, money):
        self.account_balance -= money

    def print_balance(self):
        print(self.account_balance)


# Inherited account for player
class GuestAccount(Account):
    def __init__(self, account_balance):
        super().__init__()
        self.account_balance = account_balance


# account for dealer
class DealerAccount(Account):
    def __init__(self):
        super().__init__()
        self.account_balance = 100000


# The three dice that can be chosen
black_die = [3, 3, 4, 4, 8, 8]
white_die = [1, 1, 5, 5, 9, 9]
red_die = [2, 2, 6, 6, 7, 7]

# dictionary so dice can be chosen in menu
die_types = {
    1: black_die,
    2: white_die,
    3: red_die
}

# dictionary containing each die face
DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    7: (
        "┌─────────┐",
        "│ ●     ● │",
        "│ ●  ●  ● │",
        "│ ●     ● │",
        "└─────────┘",
    ),
    8: (
        "┌─────────┐",
        "│ ●  ●  ● │",
        "│ ●     ● │",
        "│ ●  ●  ● │",
        "└─────────┘",
    ),
    9: (
        "┌─────────┐",
        "│ ●  ●  ● │",
        "│ ●  ●  ● │",
        "│ ●  ●  ● │",
        "└─────────┘",
    )
}
# variables that allow dice art to be constructed in terminal
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "

# Main
# how much money the player has
cash = float(input("How much money you bringing?: $"))
# account objects declared
your_acc = GuestAccount(cash)
dealer_acc = DealerAccount()

# for loop that allows 3 rounds of play
for i in range(3):
    if your_acc.account_balance == 0:
        break
    elif dealer_acc.account_balance == 0:
        print("Dealer is broke")
        break

    # player makes a bet
    while True:
        your_bet = float(input("Enter a bet: $"))
        if your_bet > your_acc.account_balance:
            print("Not enough funds")
        else:
            break

    while True:
        # your roll
        my_die_face, my_num = generate_my_result()
        print(my_die_face)

        # dealer's roll
        pc_die_face, pc_num = generate_dealer_result()
        print(pc_die_face)
        
        # Prints who won and what the balance is after betting
        print()
        if pc_num > my_num:
            result = "Dealer wins"
            print(result)
            bet(your_bet, result, your_acc, dealer_acc)
            bet_printer(your_acc, dealer_acc)
            print()
            break
        elif my_num > pc_num:
            result = "You win"
            print(result)
            bet(your_bet, result, your_acc, dealer_acc)
            bet_printer(your_acc, dealer_acc)
            print()
            break
        elif my_num == pc_num:
            print("Tie, roll again")

