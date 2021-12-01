import pandas as pd 


def count_increases(l):
	'''
	Step through the list, incrementing a counter each time a value is preceeded by a lower value
	'''
	increases = 0
	for i in range(1, len(l)):
		if l[i] > l[i-1]:
			increases += 1
	return increases

def sliding_sum(l):
	'''
	Perform a rolling sum over a list with a window size of 3
	'''
	sums = []
	for i in range(2, len(l)):
		sum = l[i] + l[i-1] + l[i-2]
		sums.append(sum)
	return sums



if __name__ == "__main__":
	input = pd.read_csv('input.txt', header = None).values
	sums = sliding_sum(input)
	ups = count_increases(sums)
	print(ups)