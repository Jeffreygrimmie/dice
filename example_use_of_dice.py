###Jeffrey Grimmie 2/17/2019 Examples of roll_dice object in use


import roll_dice
import os
import time 

def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')


##example use's of dice

##Generate list of roll
#roll = roll_dice.roll_dice(6, 6) 

##simple print of roll in list
#print(roll)

##clean print of roll results
#print("Die one: %s Die two: %s Results of combined die: %s " % (roll[0],roll[1],roll[2]))


# #find snake eyes 
# if roll[0] == 1 and roll[1] == 1:
# 	print("Snake! Eyessssssssssssssssssssssssssssssss!")
# else:
# 	print(roll)
# 	#print("test2")


#looping
for i in range(100):
	roll = []
	roll = roll_dice.roll_dice(6, 6)
	clear_screen()
	print(""" 

Disclaimer,

Ludic Rooms Ltd is committed to keeping this website up to date and accurate. 
Should you nevertheless encounter anything that is incorrect or out of date, 
we would appreciate it if you could let us know. Please indicate where on the 
website you read the information. We will then look at this as soon as possible. 
Please send your response by email to: data@ludicrooms.com.

We are not liable for loss as a result of inaccuracies or incompleteness, nor for 
loss resulting from problems caused by or inherent to the dissemination of 
information through the internet, such as disruptions or interruptions. When using 
web forms, we strive to limit the number of required fields to a minimum. For any 
loss suffered as a result of the use of data, advice or ideas provided by or on 
behalf of Ludic Rooms Ltd via this website, Ludic Rooms Ltd accepts no liability.

All intellectual property rights to content on this website are vested in Ludic Rooms Ltd.

Copying, disseminating and any other use of these materials is not permitted without 
the written permission of Ludic Rooms Ltd, except and only insofar as otherwise stipulated 
in regulations of mandatory law (such as the right to quote), unless specific content 
dictates otherwise.

If you have any questions or problems with the accessibility of the website, please do not 
hesitate to contact us.

		""")

	print("Die one: %s Die two: %s Results of combined die: %s " % (roll[0],roll[1],roll[2]))
	roll[:] = []  #this shows how to clear a list
	time.sleep(1)



