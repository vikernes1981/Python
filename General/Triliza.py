#-*- coding: utf-8 -*-
# Άσκηση 16_1_template
# Κρίση εργασίας: (βαθμολόγηση όπως παρακάτω)
import random
import time

marker = {'Παίκτης 1': 'X', 'Παίκτης 2': 'O', }

def display_board(board): 
    print('+'+'-'*17+'+')
    print('|7    |8    |9    |')
    print('|  '+board[7]+'  |  '+board[8]+'  |  '+board[9]+'  |')
    print('+'+'-'*17+'+')
    print('|4    |5    |6    |')
    print('|  '+board[4]+'  |  '+board[5]+'  |  '+board[6]+'  |')
    print('+'+'-'*17+'+')
    print('|1    |2    |3    |')
    print('|  '+board[1]+'  |  '+board[2]+'  |  '+board[3]+'  |')
    print('+'+'-'*17+'+')

def choose_first():
    paixths = ''
    arithmos = random.randint(1,2)
    if arithmos == 1 :
        paixths = 'Παίκτης 1'
    else:
        paixths = 'Παίκτης 2'
    return paixths

def display_score(score):
    print ("Σκορ : {} ".format(score))

def place_marker(board, marker, position): 
    board[position] = marker
        
def win_check(board,mark): 
    if board[1] == board[2] == board[3] == mark :
        return True
    elif board[4] == board[5] == board[6] == mark :
        return True
    elif board[7] == board[8] == board[9] == mark :
        return True
    elif board[7] == board[5] == board[3] == mark :
        return True
    elif board[9] == board[5] == board[1] == mark :
        return True
    elif board[7] == board[4] == board[1] == mark :
        return True
    elif board[8] == board[5] == board[2] == mark :
        return True
    elif board[9] == board[6] == board[3] == mark :
        return True
    else:
        return False
    
def board_check(board): 
    check = False
    if board[1] == ' ' \
    or board[2] == ' ' \
    or board[3] == ' ' \
    or board[4] == ' ' \
    or board[5] == ' ' \
    or board[6] == ' ' \
    or board[7] == ' ' \
    or board[8] == ' ' \
    or board[9] == ' '  :
        return False
    else :
        return True
     
def player_choice(board, turn): 
    choice1 = ""
    choice1 = input("Ποία είναι η κινησή σου? (1-9) : {} ".format(turn))
    while True :
        if choice1 not in list('123456789') :
            choice1 = input("Ποία είναι η κινησή σου? (1-9) : {} ".format(turn))
            continue
        else :
            if board[int(choice1)] != ' ' :
                print("Πιασμένο Τετράγωνο Ξαναδοκίμασε!")
                choice1 = input("Ποία είναι η κινησή σου? (1-9) : {} ".format(turn))
                continue
            else :
                return int(choice1)

def replay():
    choice1 = " "
    while choice1 != 'N' \
    or choice1 != 'Y' \
    or choice1 != 'Υ' \
    or choice1 != 'Ν' \
    or choice1 != 'ν' \
    or choice1 != 'n' \
    or choice1 != 'y' \
    or choice1 != 'υ':
        choice1 = input("Πάμε άλλη μια φορά; Y/N : ")
        if choice1 == 'y' or choice1 == 'Y':
            return True
            break
        else:
            return False
            break
    

def next_player(turn):
    if turn == 'Παίκτης 1' :
        return 'Παίκτης 2'
    else:
        return 'Παίκτης 1'

def main():
    score = {} # λεξικό με το σκορ των παικτών
    print('Αρχίζουμε!\nΓίνεται κλήρωση ', end = '')
    for t in range(10):
        print(".", flush='True', end=' ')
        time.sleep(0.2)
    print()
    # η μεταβλητή turn αναφέρεται στον παίκτη που παίζει
    turn = choose_first() 
    print("\nΟ " + turn + ' παίζει πρώτος.')
    # η μεταβλητή first αναφέρεται στον παίκτη που έπαιξε πρώτος
    first = turn 
    game_round = 1 # γύρος παιχνιδιού
    while True:
        theBoard = [' '] * 10 
        game_on = True  #ξεκινάει το παιχνίδι
        while game_on:
            display_board(theBoard) #Εμφάνισε την τρίλιζα
            # ο παίκτης turn επιλέγει θέση
            position = player_choice(theBoard, turn) 
            # τοποθετείται η επιλογή του
            place_marker(theBoard, marker[turn], position) 
            if win_check(theBoard, marker[turn]): # έλεγχος αν νίκησε
                display_board(theBoard)
                print('Νίκησε ο '+ turn)
                score[turn] = score.get(turn, 0) + 1
                game_on = False
            # έλεγχος αν γέμισε το ταμπλό χωρίς νικητή
            elif board_check(theBoard): 
                display_board(theBoard)
                print('Ισοπαλία!')
                game_on = False
            else: # αλλιώς συνεχίζουμε με την κίνηση του επόμενου παίκτη
                turn = next_player(turn)
        if not replay():
            ending = ''
            if game_round>1 : ending = 'υς'
            print("Μετά {} γύρο{}".format(game_round, ending))
            display_score(score) # έξοδος ... τελικό σκορ
            break
        else :
            game_round += 1
            # στο επόμενο παιχνίδι ξεκινάει ο άλλος παίκτης
            turn = next_player(first) 
            first = turn
main()
