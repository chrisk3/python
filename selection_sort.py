# Implement a selection sort algorithm to sort a list of varying length

import random

input_list = []

# generating a random list of numbers
for i in range(10000):
	input_list.append(random.randrange(0, 10000))

# accepts a list of integers and sorts the list
def selection_sort(input_list):

	for n in range(0, len(input_list)):
		# initializing the variable lowest and setting it to the first index of the input_list
		lowest = n

		# for each item in the list starting at n
		for j in range(n, len(input_list)):
			# checks each index for the lowest value
			if input_list[j] < input_list[lowest]:
				lowest = j
		# 'swaps' the current lowest value. n becomes the current lowest and the original n value gets moved further into the list.
		input_list[n], input_list[lowest] = input_list[lowest], input_list[n]
	return input_list

print selection_sort(input_list)