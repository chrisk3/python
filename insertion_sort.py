# Implement an insertion sort algorithm to sort a list of varying length

import random

input_list = []

# generating a random list of numbers
for i in range(10000):
	input_list.append(random.randrange(0, 10000))

# sorts a list of integers using the insertion sort algorithm. accepts a list of integers and returns the same list sorted lowest to highest
def insertion_sort(input_list):
	for index in range(1, len(input_list)):
		value = input_list[index]
		left = index - 1

		# traverse the list backwards until we get to the first index
		while left >= 0:
			# if the current index in the outer for loop is greater than our next value on the left
			if value < input_list[left]:
				# we swap the two values until we've traversed the array backwards
				input_list[left + 1], input_list[left] = input_list[left], value
			else:
				pass
			left -= 1

	return input_list

print "Unsorted: ", input_list
print "----------------"
print "Sorted: ", insertion_sort(input_list)