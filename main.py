from dice import *

# how much money the player has
while True:
    cash = float(input("How much money you bringing?: $"))
    if cash < 0:
        print("Invalid")
    else:
        break

# account objects declared
your_acc = GuestAccount(cash)
dealer_acc = DealerAccount()

# Whether player would like to continue playing
flag = True

while flag:
    if your_acc.account_balance == 0:
        print("You are broke, game over")
        break
    elif dealer_acc.account_balance == 0:
        print("Dealer is broke, game over")
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
        my_die_face, my_num, die_choice = generate_my_result()
        print(my_die_face)

        # dealer's roll
        pc_die_face, pc_num = generate_dealer_result(die_choice)
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

    answer = input("Would you like to continue?[y, n]: ")
    if answer == "y" or "Y":
        continue
    elif answer == "n" or "N":
        flag = False
