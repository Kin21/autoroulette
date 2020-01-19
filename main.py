import parse
import autobetbot
import time

def num_in_color(num):
    if 1 <= num <= 7:
        return 'red'
    elif 8 <= num <= 14:
        return 'black'
    elif num == 0:
        return 'green'


def mybetalg(balance,first_bet,final_sum):
    chosen_color = 'black'
    current_balance = balance
    current_bet = first_bet

    old_result,old_id = parse.get_result()

    while True:
        if current_balance <= 0:
            print("YOU LOSE")
            return
        elif current_balance >= final_sum:
            print("+" + str(current_balance - balance))
            break
        result,id = parse.get_result()
        autobetbot.sell_item()
        autobetbot.make_bet(current_bet,chosen_color)
        while id == old_id:
            time.sleep(4)
            result,id = parse.get_result()
        old_id = id
        color = num_in_color(result)
        print(color)
        if color == 'red' and chosen_color == 'red':
            current_balance += current_bet
            current_bet = first_bet
        elif color == 'red' and chosen_color == 'black':
            current_balance -= current_bet
            current_bet *= 2
            chosen_color = 'red'
        elif color == 'black' and chosen_color == 'black':
            current_balance += current_bet
            current_bet = first_bet
        elif color == 'black' and chosen_color == 'red':
            current_balance -= current_bet
            current_bet *= 2
            chosen_color = 'black'
        elif color == 'green':
            current_balance -= current_bet
            current_bet *= 2



def session():
    balance,first_bet,final_sum = parse.init()
    parse.check_chance(first_bet,balance,final_sum)
    print("Now set coords")
    autobetbot.coords_init()
    ok = 'n'
    while ok != 'y':
        autobetbot.test_coord()
        ok = input("All is OK ?(Y/N)\n")
        ok.lower()
        if ok == 'n':
            autobetbot.coords_init()
    mybetalg(balance,first_bet,final_sum)
session()
# bal,bet,total= parse.init()
# parse.check_chance(bet,bal,total )
