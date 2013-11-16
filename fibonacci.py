# Create a script that calculates the fibonacci sequence to the N indices, where N is a user inputted integer.

# get input from user
end = raw_input("How long do we continue the sequence? (Note: max 100) >> ")

# cap it at 100 to keep it from getting ridiculous and confirm number isn't negative
if int(end) > 100:
	while int(end) > 100:
		end = raw_input("How long do we continue the sequence? (Note: max 100) >> ")
if int(end) < 0:
	while int(end) < 0:
		end = raw_input("How long do we continue the sequence? (Note: max 100) >> ")

# calculates the fibonacci sequence. accepts an integer as a parameter and returns a list containing the sequence.
def calculate(end):
	first = 0
	second = 1
	fib = [0, 1]

	for i in range(end - 2):
		fib.append(fib[-1] + fib[-2])

	return fib

print calculate(int(end))