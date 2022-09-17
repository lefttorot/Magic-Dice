from dice import *

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