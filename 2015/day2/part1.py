def surface_area(dims):
	face_surface_areas = [dims[0] * dims[1], dims[1] * dims[2], dims[0] * dims[2]]
	return 2 * sum(face_surface_areas) + min(face_surface_areas)

def main():
	file_data = ''
	with open('input.txt', 'r') as f:
		file_data = f.read()

	file_lines = file_data.split('\n')
	dimension_strings = [line.strip() for line in file_lines if line]
	dimensions = [[int(x) for x in dimension_string.split('x')] for dimension_string in dimension_strings]
	total_sa = sum([surface_area(dims) for dims in dimensions])
	print(total_sa)

if __name__ == '__main__':
	main()
