def main():
	file_data = ''
	with open('input.txt', 'r') as f:
		file_data = f.read()

	print(sum(
		[{
			'(': 1,
			')': -1
		}[c] for c in file_data.strip()]
	))

if __name__ == '__main__':
	main()
