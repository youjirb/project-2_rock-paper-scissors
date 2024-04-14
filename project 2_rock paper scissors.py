import random

chce=['rock','paper','scissors']
win=0
com_win=0
tie=0

while True:
    uc=input('Please pick rock, paper, scissors or type Q to quit: ').lower()
    if uc=='q':
        break
    elif uc not in chce:
        print('Invalid choice. Please enter rock, paper, or scissors.')
        continue
    
    com_choice=random.choice(chce)
    print(f'Computer choose: {com_choice}')

    if uc==com_choice:
        print('its a tie')
        tie +=1

    elif (uc == 'rock' and com_choice == 'scissors') or \
         (uc == 'paper' and com_choice == 'rock') or \
         (uc == 'scissors' and com_choice == 'paper'):
        print('You win')
        win +=1
    else:
        print('Computer wins')
        com_win +=1

print(f'You have played {win+com_win+tie} matches.\nYou won {win} times.\nComputer won {com_win} times.\nYou tied {tie} times')