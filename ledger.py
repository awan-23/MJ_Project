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

from copy import deepcopy

# set up scoring/payout system
SCORING = [8, 16, 32, 48, 64, 96, 128, 256]


# get user input on functionality - returns int
def get_option():
	while True:
		# TODO: extra features 
				# manually change accounts,
				# history of rounds,
				# save in external file
		choice = raw_input("""What would you like to do?
			1) record new round
			2) undo last change
			3) check current scores
			4) add new player
			5) remove player
			6) end game
			>> """)  # can't make int in case user entered char
		if choice not in "1 2 3 4 5 6".split():
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
#ledger = {"Au": 0, "Na": 0, "Nic": 0, "Ra": 0, "Pa": 0}
ledger = {}
player_list = []
num_players = int(raw_input("How many people are playing? >> "))
i = 0
while i < num_players:
	name = raw_input("Name of player %d >> " % (i+1))
	if name in player_list:
		print "Sorry, that name is already taken."
	else:
		ledger[name] = 0
		player_list.append(name)
		i += 1


# copy current ledger and player_list in case undo is needed
old_ledger = ledger.copy()
old_player_list = deepcopy(player_list)

# flags used in undo
last_move = 0  # 1: added player, 2: removed player, 0: else
removed_account = ["", 0]

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

		last_move = 0

	elif choice == 2:  # undo last move

		check = raw_input("Are you sure you want to undo the last move? >> ")
		if "y" in check.lower():
			print "Undoing last move"
			ledger = old_ledger.copy()
			print "The ledger is now"
			print ledger

			if last_move == 1:
				name = player_list[-1]
				print "Removing player %s." % name  # undo adding of player
				# ledger updated already, no need to del account again
				player_list = player_list[:-1]  # remove last entry
			elif last_move == 2:
				name = removed_account[0]
				money = removed_account[1]
				print "Restoring player %s." % name
				player_list.append(name)
				ledger[name] = money  # TODO: does this affect recording on external file?

			last_move = 0
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

		# doesn't change last_move flag

	elif choice == 4:  # add new player
		added = False
		while not added:
			new_player = raw_input("Name of new player? (0 to cancel) >> ").title()  # capitalize first letter
			# TODO: any other criteria for name?
			if new_player == "0":
				print "Cancelled."
				added = True
			elif new_player in player_list:
				print "Sorry, that name is already taken."
			else:
				old_ledger = ledger.copy()  # copy current ledger in case undo is needed
				old_player_list = deepcopy(player_list)  # deep copy of player_list in case undo
				print "Adding %s to the ledger." % new_player
				player_list.append(new_player)
				print player_list
				ledger[new_player] = 0  # creates new account, starting bal $0
				added = True
				last_move = 1

	elif choice == 5:  # removed player
		removed = False
		while not removed:
			old_player = raw_input("Name of player to remove? (0 to cancel) >> ").title()  # capitalize first letter
			if old_player == "0":
				print "Cancelled."
				removed = True
			elif old_player not in player_list:
				print "Sorry, could not find that player.\nChoose one of the following:"
				for name in player_list:
					print name,
				print ""
			else:
				old_ledger = ledger.copy()  # copy current ledger in case undo is needed
				old_player_list = deepcopy(player_list)  # deep copy of player_list in case undo
				removed_account = [old_player, ledger[old_player]]  # save account in case undo
				print "Removing %s from the ledger." % old_player
				player_list.remove(old_player)  # TODO: will this affect recording on external file?
				del ledger[old_player]
				removed = True
				last_move = 2

	else:  # end game
		check = raw_input("Are you sure you want to end the game? >> ")
		if "y" in check.lower():
			print ledger
			print "Thanks for playing!"
			exit(0)
		else:
			print "Cancelled."






