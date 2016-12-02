def minimum_perimeter(dims):
	perimeters = [2 * (dims[0] + dims[1]), 2 * (dims[1] + dims[2]), 2 * (dims[0] + dims[2])]
	return min(perimeters)

def volume(dims):
	return dims[0] * dims[1] * dims[2]

def main():
	file_data = ''
	with open('input.txt', 'r') as f:
		file_data = f.read()

	file_lines = file_data.split('\n')
	dimension_strings = [line.strip() for line in file_lines if line]
	dimensions = [[int(x) for x in dimension_string.split('x')] for dimension_string in dimension_strings]
	total_ribbon_length = sum([minimum_perimeter(dims) + volume(dims) for dims in dimensions])
	print(total_ribbon_length)

if __name__ == '__main__':
	main()
