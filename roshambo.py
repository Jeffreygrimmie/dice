###Jeffrey Grimmie 2/17/2019

###To do: fix bug, if more then one player rolls the same number and the rolls are highest in rolls.

### tap roll the dice game rolls dice on each input for player then returns what player wins.
import os
import roll_dice

def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')
def same_number_roll_checker(rolls):
	none = none #place holder for future code
###To do: fix bug, if more then one player rolls the same number and the rolls are highest in rolls.
###here
def roshambo():
	roll = []
	rolls = []
	player_position = 1
	clear_screen()
	print("Welcome to Roshambo play at your own risk!!!")
	print("The player that rolls the highest number first wins!")
	players = int(input('How many players are there: '))
	for i in range(players):
		input('Press any key to roll player %s' % player_position)
		roll = roll_dice.roll_dice(6, 6)
		#print(roll[-1])
		rolls.insert(player_position - 1, roll[-1])
		roll[:] = []
		player_position += 1
	winner = rolls.index(max(rolls)) + 1
	#print(rolls)
	print('Player %s has won the roll!' % winner)

roshambo()