import re

def main():
	file_data = ''
	with open('input.txt', 'r') as f:
		file_data = f.read()

	numbers = re.findall(r'-?\d+', file_data)
	print(sum([int(x) for x in numbers]))

if __name__ == '__main__':
	main()
