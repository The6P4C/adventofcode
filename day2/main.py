DIRECTION_OFFSETS = {
	'U': (0, -1),
	'D': (0, 1),
	'L': (-1, 0),
	'R': (1, 0)
}

# Part 1
# keypad = [
# 	['1', '2', '3'],
# 	['4', '5', '6'],
# 	['7', '8', '9']
# ]

# BOUNDS = (2, 2)
# INITIAL = (1, 1)

# Part 2
keypad = [
	[None, None, '1', None, None],
	[None, '2', '3', '4', None],
	['5', '6', '7', '8', '9'],
	[None, 'A', 'B', 'C', None],
	[None, None, 'D', None, None]
]

BOUNDS = (4, 4)
INITIAL = (0, 2)

def add_points(p1, p2):
	return (p1[0] + p2[0], p1[1] + p2[1])

def can_move(position, direction):
	new_position = add_points(position, DIRECTION_OFFSETS[direction])

	if new_position[0] < 0 or new_position[0] > BOUNDS[0] or new_position[1] < 0 or new_position[1] > BOUNDS[1]:
		return False

	return keypad[new_position[1]][new_position[0]] != None

def find_digit(initial_position, instructions):
	position = initial_position
	for direction in instructions:
		if can_move(position, direction):
			position = add_points(position, DIRECTION_OFFSETS[direction])

	return keypad[position[1]][position[0]], position

def main():
	file_data = ''
	with open('input.txt', 'r') as f:
		file_data = f.read()

	# remove empty lines
	digit_instructions = [line for line in file_data.split('\n') if line]
	
	position = INITIAL
	for digit_instruction in digit_instructions:
		digit, position = find_digit(position, digit_instruction)
		print(digit)

if __name__ == '__main__':
	main()
