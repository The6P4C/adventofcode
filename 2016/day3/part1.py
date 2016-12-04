def is_possible(triangle):
	sides = sorted(triangle)
	return sides[0] + sides[1] > sides[2]

def main():
	file_data = ''
	with open('input.txt', 'r') as f:
		file_data = f.read()

	lines = [line.strip() for line in file_data.split('\n') if line]
	triangles = [[int(x) for x in line.split(' ') if x] for line in lines]
	true_triangles = [triangle for triangle in triangles if is_possible(triangle)]

	print(len(true_triangles))

if __name__ == '__main__':
	main()
