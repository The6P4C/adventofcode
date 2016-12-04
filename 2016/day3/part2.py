def is_possible(triangle):
	sides = sorted(triangle)
	return sides[0] + sides[1] > sides[2]

def main():
	file_data = ''
	with open('input.txt', 'r') as f:
		file_data = f.read()

	numbers = [int(x) for x in file_data.replace('\n', ' ').split(' ') if x]

	triangles = []
	for i in range(0, len(numbers), 9):
		for j in range(0, 3):
			triangles.append([numbers[i + j], numbers[i + j + 3], numbers[i + j + 6]])

	true_triangles = [triangle for triangle in triangles if is_possible(triangle)]

	print(len(true_triangles))

if __name__ == '__main__':
	main()
