INPUT = ''
WIDTH = 50
HEIGHT = 6

def main():
	file_data = ''
	with open('input.txt', 'r') as f:
		file_data = f.read()

	lines = [line.strip() for line in file_data.split('\n') if line]

	screen = []
	for y in range(0, HEIGHT):
		row = []
		for x in range(0, WIDTH):
			row.append(False)
		screen.append(row)

	for instruction in lines:
		parts = instruction.split(' ')

		if parts[0] == 'rect':
			dims = [int(x) for x in parts[1].split('x')]
			for x in range(0, dims[0]):
				for y in range(0, dims[1]):
					screen[y][x] = True
		elif parts[0] == 'rotate':
			index = int(parts[2].split('=')[1])
			by = int(parts[4])

			if parts[1] == 'row':
				old_row = screen[index][:]
				screen[index] = old_row[-by:] +  old_row[:-by]
			else:
				part1 = []
				for y in range(0, HEIGHT - by):
					part1.append(screen[y][index])
				part2 = []
				for y in range(HEIGHT - by, HEIGHT):
					part2.append(screen[y][index])
				new_col = part2 + part1
				
				for y in range(0, HEIGHT):
					screen[y][index] = new_col[y]

	count = 0
	for y in range(0, HEIGHT):
		for x in range(0, WIDTH):
			if screen[y][x]:
				count += 1
	print(count)

	for y in range(0, HEIGHT):
		for x in range(0, WIDTH):
			print('#' if screen[y][x] else '.', end='')
		print()

if __name__ == '__main__':
	main()
