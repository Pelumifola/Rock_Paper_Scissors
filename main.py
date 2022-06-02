import random

R = "rock"
P = "paper"
S = "scissors"

game_is_on = True
while game_is_on:
    game = [R, P, S]
    player = input("R:rock, P:paper, S:scissors, which option do you want to choose? 'R', 'S' or 'P'\n").lower()
    computer = random.choice(game)

    if player == "r":
        player = "rock"
        print(f'You({player}) : Computer({computer})')
    elif player == "p":
        player = "paper"
        print(f'You({player}) : Computer({computer})')
    elif player == "s":
        player = "scissors"
        print(f'You({player}) : Computer({computer})')
    else:
        print('what you chose is not in the option')

#To win or lose:
#game rule: Rock covers Paper, Scissors cut Paper and Rock crushes Scissors

    if player == "rock" and computer == "paper" \
            or computer == "rock" and player == "scissors"\
            or player == "paper" and computer == "scissors":
        print('Ooops! you lose! Computer won')
        game_is_on = False

    elif computer == "rock" and player == "paper"\
            or player == "rock" and computer == "scissors" \
            or player == "scissors" and computer == "paper":
        print('Hurray! you win!')
        game_is_on = False

    elif computer == player:
        print("it's a tie")
