
import sys
import random
DECK_CARDS =  5 *["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

money = 5000
def main():

    global money
    player_card = []
    dealer_card = []
    answer_yes = ["y", "yes", "YES","Y"]


    deck_card = DECK_CARDS
    random.shuffle(deck_card)

    def append_card(deck_card):
            # append and remove the first card in the deck card list
            card = deck_card[0]
            deck_card.remove(card)

            return card



    def count_player_card(cards):
        # Returns the value of the cards. Face cards are worth 10, aces are 11 or 1
        p_card = []
        for i in cards:
            if i == "Ace":
                p_card.append(11)

            elif i in ["J", "Q", "K"]:
                p_card.append(10)

            else:
                p_card.append(int(i))
        sum_p_card = sum(p_card)
        # in a case that the sum of the card more than 21 ,change the value of the "ace" to 1
        while sum_p_card > 21 and "Ace" in cards:

            if 11 in p_card:
                p_card.remove(11)
                p_card.append(1)
                sum_p_card = sum(p_card)

            else:
                break

        return sum_p_card

    def gemble(player_card):
        # player turn, while sum of player's card less than 21 ,check his move (bet or stay)
        player_hit_option = ["H", "h", "HIT", "hit"]
        player_move = "h"
        sum_cards = count_player_card(player_card)
        while count_player_card(player_card) < 21 and player_move in player_hit_option:
            player_move = input("Would you like to HIT or STAY?")
            # add another card to the player
            if player_move in player_hit_option:
                player_card.append(append_card(deck_card))
                sum_cards = count_player_card(player_card)
                print(f"player_card = {player_card}")

        return sum_cards

    def dealer_turn(dealer_card):
        # add a cards to dealer until the sum of the card will be above than 16
        sum_dealer_card = count_player_card(dealer_card)
        while count_player_card(dealer_card) < 17 :
            dealer_card.append(append_card(deck_card))
            print(f"dealer_card ={dealer_card}")
            sum_dealer_card = count_player_card(dealer_card)

        return sum_dealer_card




    # the player enter his bet
    # check if he's bet is integers
    while True:
        try:
            bet = int(input("Please place your bet:"))
            break
        except ValueError:
            print("Invalid input was provided,  please provide integers only!")


    # check if the bet not exceeding player's balance


    while int(bet) > money :
        print(f"You don't have enough money,you have {money}")
        bet = input("Please place your bet:")

    money = money - int(bet)

    player_card.append(append_card(deck_card))

    dealer_card.append(append_card(deck_card))

    player_card.append(append_card(deck_card))
    print(f"diler card = {dealer_card}")
    print(f"player_card = {player_card}")

    def cont_player(answer_yes,player_balance):
        # Check if the player broke
        if player_balance == 0:
            print("GAME-OVER")
            print("You're broke!")
            sys.exit()
        # Check if the player want to continue game
        else:
            continue_game = input("Would you like continue gamble? y / n")
            if continue_game in answer_yes:
                return True
            else:
                print("Thanks for playing!")
                sys.exit()


    while True:

        count_player_card(player_card)
        if gemble(player_card) > 21 :
            print("you lost")
            if cont_player(answer_yes, money): # check if the player want to continue play
                main()

            else:
                break
        else:
            dealer_turn(dealer_card)
            if count_player_card(dealer_card) > 21 :
                print("you win")
                money += 2 * int(bet)
                print(money)
                if cont_player(answer_yes, money):
                    main()
                else:
                    break
            elif count_player_card(dealer_card) <= 21:
                if count_player_card(dealer_card) > count_player_card(player_card):
                    print("you lost")
                    print(money)
                    if cont_player(answer_yes, money):
                        main()
                    else:
                        break
                elif count_player_card(player_card) == count_player_card(dealer_card):
                    print("tie")

                    money += int(bet)
                    print(money)
                    if cont_player(answer_yes, money):
                        main()
                    else:
                        break
                else:
                    print("you win")
                    money += 2 * int(bet)
                    print(money)
                    if cont_player(answer_yes, money):

                        main()
                    else:
                        break




if __name__ == "__main__":
        main()








