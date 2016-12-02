SIZE = 0

def get_light_state(lights, point):
	if point in lights.keys():
		return lights[point]
	else:
		return False

def print_lights(lights):
	for y in range(0, 6):
		line = ''
		for x in range(0, 6):
			line += '#' if get_light_state(lights, (x, y)) else '.'
		print(line)

def add_points(p1, p2):
	return (p1[0] + p2[0], p1[1] + p2[1])

def count_on_neighbours(lights, point):
	count = 0
	for yo in [-1, 0, 1]:
		for xo in [-1, 0, 1]:
			neighbour_point = add_points(point, (xo, yo))

			if xo == 0 and yo == 0:
				continue
			elif get_light_state(lights, neighbour_point):
				count += 1
	return count

def step(prev_state):
	new_state = {}
	for y in range(0, SIZE):
		for x in range(0, SIZE):
			point = (x, y)
			on_neighbours = count_on_neighbours(prev_state, point)

			if get_light_state(prev_state, point):
				new_state[point] = on_neighbours in [2, 3]
			else:
				new_state[point] = on_neighbours == 3

	# Part 2
	for y in [0, SIZE - 1]:
		for x in [0, SIZE - 1]:
			new_state[(x, y)] = True

	return new_state

def main():
	global SIZE

	file_data = ''
	with open('input.txt', 'r') as f:
		file_data = f.read()

	lines = [line.strip() for line in file_data.split('\n') if line]
	
	SIZE = len(lines[0])

	lights = {}
	for y, line in enumerate(lines):
		for x, state in enumerate(line):
			if state == '#':
				lights[(x, y)] = True

	for _ in range(0, 100):
		lights = step(lights)

	on_count = 0
	for v in lights.values():
		if v:
			on_count += 1

	print(on_count)

if __name__ == '__main__':
	main()
