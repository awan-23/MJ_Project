


def cost_minimizer(A):
	# greedy approach
	# iterate through A, buy a 1-day ticket for each day i
	# If current_spending > 7, see if A[i-4] > A[i]-6
	# If so, buy a 7-day ticket instead.
	# or, work backwards.

	num_days = len(A)
	last_day = A[-1]
	# normalize input for memoization
	memo = range(last_day + 1)
	# initially, values of memo are 1 for days when traveling, 0 otherwise
	for day in memo:
		if day in A:
			memo[day] = 1  # need to travel
		else:
			memo[day] = 0  # not traveling

	# now, update values of memo to reflect min cost of travel up to day i
	for i in range(last_day + 1):
		# if not traveling, cost is just the same as prev day's cost
		if memo[i] == 0:
			memo[i] = memo[i-1]
		else:  # pick ticket type that minimizes cost up to day i
			before_29 = 0
			before_6 = 0
			if i-29 > 0:
				before_29 = i-29
			if i-6 > 0:
				before_6 = i-6

			memo[i] = min(memo[i-1] + 2,  # 1-day ticket, $2
				memo[before_6] + 6,  # 7-day ticket, $6
				memo[before_29] + 25)  # 30-day ticket, $25

	return memo[last_day-1]



print "tests for min_cost ticket program"
print "[1, 2, 4, 5, 7, 29, 30] should be $11"
print cost_minimizer([1, 2, 4, 5, 7, 29, 30])














def counter(S):
	current_max = 0
	word = False  # has a word been started already?
	count = 0  # how many words in the sentence so far?
	for ch in S:
		if ch in [" ", ".", "!", "?"]:
			if word:
				count += 1
			word = False
			if ch != " ":  # must have been end of sentence
				current_max = max(current_max, count)
				count = 0
		else:  # wasn't punctuation, must be part of a word.
			word = True
	# handle cases where S doesn't end with punctuation
	if word:
		current_max = max(current_max, count + 1)
	return current_max

print ""
print "Tests for counter:"
print counter("Hello a a a a. This is a    test       t t t t t. Heh!")
print counter(". . x . x x x . x x x x   x")



def missing_int(A):
	length = len(A)
	candidates = range(length+1)

	for number in A:
		if number > 0 and number < length+1:
			candidates[number] = length+1

	candidates = candidates[1:]
	return min(candidates)

print ""
print "Tests for missing int:"
print missing_int([1, 2, 3, 5, 6, 7])
print missing_int([0])
print missing_int([1])
print missing_int([-1, -3])
print missing_int([5, 4, 6, 1, 2])
print missing_int([1, 2, 3, 4])







