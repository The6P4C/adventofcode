def main():
	file_data = ''
	with open('input.txt', 'r') as f:
		file_data = f.read()

	level = 0
	for index, c in enumerate(file_data.strip()):
		level += {
			'(': 1,
			')': -1
		}[c]
		
		if level < 0:
			print(index + 1)
			break

if __name__ == '__main__':
	main()
