#Jeffrey Grimmie 2/17/2019
#dice rolling object that takes to arguments, sides of die 1 and sides of die two, then returns a read out of each di and their combined values.

import random



die1 = []
die2 = []
rturn_lst = [] 
### first I want to generate a list of, posibility for each side of one die
### then repeat this for the second die 
### then using random I want to pick at random a side for each die
### then I want to pring out both die and there their combined values. to the user

def roll_dice(num_dice_side_1, num_dice_side_2):
	var = 1
	for i in range(num_dice_side_1):		
		die1.append(var)
		var += 1
	var = 1
	for i in range(num_dice_side_2):
		die2.append(var)
		var += 1
	die_side_results_1 = random.choice(die1)
	die_side_results_2 = random.choice(die2)
	die_combined_values = int(die_side_results_1) + int(die_side_results_2)
	rturn_lst.append(die_side_results_1)
	rturn_lst.append(die_side_results_2)
	rturn_lst.append(die_combined_values)

	return rturn_lst

#roll_dice(6, 6)



###Need to turn this into iOS app to return a roll of die when gesturing a roll of the dice.