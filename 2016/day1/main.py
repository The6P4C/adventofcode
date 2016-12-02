DIRECTIONS = [
	(0, 1), # north
	(1, 0), # east
	(0, -1), # south
	(-1, 0) # west
]

def turn_left(direction):
	return DIRECTIONS[DIRECTIONS.index(direction) - 1]

def turn_right(direction):
	return DIRECTIONS[(DIRECTIONS.index(direction) + 1) % len(DIRECTIONS)]

def dist(position):
	return abs(position[0] - 100) + abs(position[1] - 100)

def main():
	raw_input_data = ''
	with open('input.txt', 'r') as f:
		raw_input_data = f.read()

	instructions = [instruction.strip() for instruction in raw_input_data.split(',')]
	
	position = (100, 100)
	direction = DIRECTIONS[0]
	
	previous_positions = []
	for instruction in instructions:
		turn_instruction = instruction[0]
		distance = int(instruction[1:])

		direction = (turn_left if turn_instruction == 'L' else turn_right)(direction)

		for d in range(1, distance + 1):
			position = (position[0] + direction[0], position[1] + direction[1])

			if position in previous_positions:
				print(position)
				print(dist(position))

			previous_positions.append(position)

if __name__ == '__main__':
	main()
