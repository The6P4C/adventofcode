MOVEMENT = {
	'^': (0, 1),
	'v': (0, -1),
	'<': (-1, 0),
	'>': (1, 0)
}

def add_points(p1, p2):
	return (p1[0] + p2[0], p1[1] + p2[1])

def main():
	file_data = ''
	with open('input.txt', 'r') as f:
		file_data = f.read().strip()

	position = (0, 0)
	visited = [(0, 0)]
	for instruction in file_data:
		position = add_points(position, MOVEMENT[instruction])

		if position not in visited:
			visited.append(position)

	print(len(visited))

if __name__ == '__main__':
	main()
