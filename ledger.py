"""
Name: awan-23
Desc: This project aims to provide a convenient way to keep track of accounts
		during a casual session of Mahjong.

		Accounts are saved in a dictionary of player:money pairs.
		After each round, the user can type in
			the player who won, the number of points, and the player who lost (or zi-mo).
		The program should then update the accounts in the dictionary.
		At the end, the program should print out the final accounts

"""

# set up scoring/payout system
SCORING = [8, 16, 32, 48, 64, 96, 128, 256]


# get user input on functionality - returns int
def get_option():
	while True:
		# TODO: extra features 
				# add extra players,
				# remove old players,
				# manually change accounts,
				# history of rounds,
				# save in external file
		choice = raw_input("""What would you like to do?
			1) record new round
			2) undo last change
			3) check current scores
			4) end game
			>> """)
		if choice not in "1 2 3 4".split():
			print "That's not a valid choice. Please pick a number."
		else:
			return int(choice)


# get user input, return the name of a valid player
def get_player(winner = None):
	while True:
		if winner == None:
			player = raw_input("Name of the person who won? >> ")
			
		else:
			player = raw_input("Name of the person who lost? (0 for zi-mo) >> ")

		if winner != None and player == "0":
			return player  # zi-mo

		player = player.title()  # capitalize first letter
		if player not in player_list or player == winner:
			print "That's not a valid choice. Please type one of the following:"
			for name in player_list:
				if name != winner:
					print name,
			print ""
		else:
			return player


# get user input, return list of names of losers
def get_losers(winner):
	losers = []
	counter = 0
	while counter < 3:
		player = raw_input("Name of losing player %d? >> " % (counter+1)).title()  # capitalized
		if player not in player_list or player == winner or player in losers:
			print "That's not a valid choice. Please type one of the following:"
			for name in player_list:
				if name != winner and name not in losers:
					print name,
			print ""
		else:
			losers.append(player)
			counter += 1
	return losers

# get user input, return integer in range(3, 11)
def get_score():
	while True:
		score = raw_input("How many points? >> ")
		if score not in "3 4 5 6 7 8 9 10".split():
			print "That's not a valid score. Please type a number between 3 - 10"
		else:
			return int(score)


# initialize dictionary of player:money pairs
ledger = {"Au": 0, "Na": 0, "Nic": 0, "Ra": 0, "Pa": 0}
# TODO: allow user to enter names of players 1 by 1
# num_players = int(raw_input("How many people are playing? >> "))
# for i in range(num_players):
# 	ledger # add players by name, 1 at a time
player_list = ledger.keys()


# copy current ledger in case undo is needed
old_ledger = ledger.copy()

# main loop
while True:
	choice = get_option()  # choice is 1, 2, or 3

	if choice == 1:  # record new round

		old_ledger = ledger.copy()  # copy current ledger in case undo is needed

		winner = get_player()
		score = get_score()
		# TODO: check if score is in range(3, 11)
		money = SCORING[score - 3]
		loser = get_player(winner)
		if loser == "0":
			money *= 2
			if len(ledger) > 4:  # need to ask for losing players
				losers = get_losers(winner)
				for player in losers:
					ledger[player] -= money/3
			else:  # automatically subtract from other players' accounts
				for player in player_list:
					if player != winner:
						ledger[player] -= money/3
		else:
			ledger[loser] -= money
		ledger[winner] += money

		print "*" * 20
		print "Adding %d to %s" %(money, winner)
		if loser != "0":
			print "Subtracting %d from %s" %(money, loser)
		else:
			print "Subtracting %d from the others" %(money/3)
		print "The new ledger is "
		print ledger


	elif choice == 2:  # undo last move
		check = raw_input("Are you sure you want to undo the last move? >> ")
		if "y" in check.lower():
			print "Undoing last move"
			ledger = old_ledger.copy()
			print "The ledger is now"
			print ledger
		else:
			print "Undo cancelled"

	elif choice == 3:  # check current score
		# TODO: better way to do this?
		for player in player_list:
			money = ledger[player]
			if money < 0:
				money *= -1  # make money a positive amount
				print "%s: -$%d." % (player, money)
			else:
				print "%s: $%d." % (player, money)

	else:  # end game
		print ledger
		print "Thanks for playing!"
		exit(0)







