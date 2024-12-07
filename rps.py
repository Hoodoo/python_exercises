import random

up_to = 2

beaten_by = {
    'Paper': 'Rock',
    'Rock': 'Scissors',
    'Scissors': 'Paper'
}

score = {
    'Computer': 0,
    'Player': 0
}

def game_round(player_choice):    
    comp_choice = random.choice(list(beaten_by.keys()))
    print("\n" + "Computer chose " + comp_choice)
    print("Player chose " + player_choice + "\n")
    
    if player_choice == comp_choice:
        print("Draw\n")
        print(score)
        return()  
    if beaten_by[player_choice] == comp_choice:
        print ("player wins this round\n")
        score['Player'] += 1
        print(score)
    else:
        print("computer wins this round\n")
        score['Computer'] += 1
        print(score)

def player_choice():
    if (up_to in score.values()):
        if (score['Computer'] > score['Player']):
            print("Computer wins the game!\n")
            exit()
        else:
            print("Player wins the game\n")
            exit()

    player_choice = input("Choose Rock, Paper or Scissors: ")
    return player_choice

#player_choice()
while True:
    game_round(player_choice())
