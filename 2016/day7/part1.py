import re

INPUT = ''

def main():
	file_data = ''
	with open('input.txt', 'r') as f:
		file_data = f.read()

	lines = [line.strip() for line in file_data.split('\n') if line]
	count = 0
	for line in lines:
		in_hns = False
		abba_outside = False
		abba_inside = False
		for i, c in enumerate(line):
			if c == '[':
				in_hns = True
			elif c == ']':
				in_hns = False

			if i < len(line) - 3:
				substr = line[i:i+4]
				if substr[0] == substr[3] and substr[1] == substr[2] and substr[0] != substr[1]:
					if in_hns:
						abba_inside = True
					else:
						abba_outside = True
		if abba_outside and not abba_inside:
			count += 1
	print(count)

if __name__ == '__main__':
	main()
