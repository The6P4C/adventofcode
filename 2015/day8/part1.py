def main():
	file_data = ''
	with open("input.txt", 'r') as f:
		file_data = f.read()

	strings = [line.strip() for line in file_data.split('\n') if line]

	code_lengths = sum([len(s) for s in strings])

	memory_lengths = 0
	for s in strings:
		memory_lengths += len(eval(s))

	print(code_lengths - memory_lengths)

if __name__ == '__main__':
	main()
