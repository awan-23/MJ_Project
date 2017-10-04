from equilibrium_index import equilibrium_finder

def test_answer():
	A = [-1, 3, -4, 5, 1, -6, 2, 1]
	assert equilibrium_finder(A, len(A)) == 1

def test_two():
	A = [0]
	assert equilibrium_finder(A, len(A)) == 0

def test_two():
	A = []
	assert equilibrium_finder(A, len(A)) == -1