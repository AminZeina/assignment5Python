# Created By: Amin Zeina
# Created On: Apr 2018
# Calculator with 1 condition, 1 loop and 1 variable

answer = 0

operation = input('''
Choose your operation:

Type "+" for Addition
Type "*" for Multiplication
''')

if operation != '+' and operation != "*": # Check if operation is valid
	print('Invalid Operation.')

else:
	number_a = int(input('Enter your first number: '))
	number_b = int(input('Enter your second number: '))

	if operation == '+':
		answer = number_a + number_b
	else:
		for timesAdded in range(0,number_b):
			answer = answer + number_a


	print('Your answer is {}' .format(answer))

input('Program End.')