ROW = 2981
COLUMN = 3075

def position_to_index(row, column):
	return sum(range(1, column + 1)) + sum(range(column, column + row - 1))

def get_code(index):
	code = 20151125
	for i in range(1, index):
		code *= 252533
		code %= 33554393
	return code

def main():
	index = position_to_index(ROW, COLUMN)
	print("Index: %d" % index)

	code = get_code(index)
	print("Code: %d" % code)

if __name__ == '__main__':
	main()
