
from random import randint

def win():# def is pree difine keyword. win is variable name and we pass the prameter inside the parenteses.
    print ('You win!')
    # return ('You win!')# if we are returen the function then i have to print this function when i will pass then argument.

    
def lose():# def is pree difine keyword. lose is variable name and we pass the prameter inside the parenteses.
    print ('You lose!')
    # return ('You lose!')# if we are returen the function then i have to print this function when i will pass then argument.

while True:# our while condition will work infenative.
    player_choice = input('What do you pick? (rock, paper, scissors)')# we will ask to pair to give input among this rock ,paper,scissors.
    player_choice.strip()# it will take take only tring input .
    random_move = randint(0, 2)# random_move is a variable in that (i will assign randint(0,2) it will take randome number 0 to 2 )
    moves = ['rock', 'paper', 'scissors']# moves is list of element's.
    computer_choice =  moves[random_move]#computer choice is equal to moves[random_move] meanse moves index value.
    # print(computer_choice)
    # player_choice = input('What do you pick? (rock, paper, scissors)')
    # player_choice.strip()

    if player_choice == computer_choice:# if player_choice is equal to equal to choice then print Draw!
        print('Draw!')
    elif player_choice == 'rock' and computer_choice == 'scissors': #if , if condition will false then call win function.
        # print(win())
        win() #call win function / pass the argument in win function.
    elif  player_choice == 'paper' and computer_choice == 'scissors':
        # print(lose())
        lose()# call lose function/ pass the argument in lose function.
    elif player_choice  == 'scissors' and computer_choice == 'paper':
        # print(win())
        win()
    elif player_choice  == 'scissors' and computer_choice == 'rock':
        # print(lose())
        lose()
    elif player_choice  == 'paper' and computer_choice == 'rock':
        # print(win())
        win()
    elif player_choice  == 'rock' and computer_choice == 'paper' :
        # print(lose())
        lose()
    aGain = input('Do you want to play again? (y or n)').strip() #if we want to play again then enter y or enter n.
    if aGain == 'n':# if user will write n then it will break.
        break
