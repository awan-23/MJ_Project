# 
# A zero-indexed array A consisting of N integers is given. An equilibrium index of this array is any integer P such that 0 <= P < N and the sum of elements of lower indices is equal to the sum of elements of higher indices
#

def equilibrium_finder(A, n):
	if n == 0:
		return -1

	results = [[A[0], 0]]  # start of array of n number,prefix doubles. Suffixes to be calculated at the end
	total = A[0]  # used to calculate suffix parts quickly
	
	for i in range(1, n):
		number = A[i]
		prefix = results[i-1][1] + A[i-1]  # prefix is whatever it was before, plus the previous number
		results.append([number, prefix])
		total += number

	print "total: ", total
	for i in range(n):
		prefix = results[i][1]
		print "prefix: ", prefix
		print "suffix: ", total - results[i][0] - prefix
		if prefix == total - results[i][0] - prefix:
			return i

	return -1






