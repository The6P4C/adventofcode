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

	positions = [(0, 0), (0, 0)]
	visiteds = [[(0, 0)], [(0, 0)]]
	who = 0
	for instruction in file_data:
		positions[who] = add_points(positions[who], MOVEMENT[instruction])

		if positions[who] not in visiteds[who]:
			visiteds[who].append(positions[who])

		who = (who + 1) % 2

	true_visited = []
	for visited in visiteds:
		for position in visited:
			if position not in true_visited:
				true_visited.append(position)

	print(len(true_visited))

if __name__ == '__main__':
	main()
