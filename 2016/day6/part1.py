def main():
	file_data = ''
	with open('input.txt', 'r') as f:
		file_data = f.read()

	lines = [line.strip() for line in file_data.split('\n') if line]

	counts = [{} for i in range(0, len(lines[0]))]

	for line in lines:
		for i, c in enumerate(line):
			if c in counts[i].keys():
				counts[i][c] += 1
			else:
				counts[i][c] = 1

	corrected_string = ''
	for i in range(0, len(lines[0])):
		# Part 1
		# c = max(counts[i].keys(), key=(lambda key: counts[i][key]))

		# Part 2
		c = min(counts[i].keys(), key=(lambda key: counts[i][key]))
		
		corrected_string += c

	print(corrected_string)

if __name__ == '__main__':
	main()
