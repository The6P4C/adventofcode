def parse_point(s):
	parts = s.split(',')
	return (int(parts[0]), int(parts[1]))

def apply(lights, p1, p2, func):
	for x in range(p1[0], p2[0] + 1):
		for y in range(p1[1], p2[1] + 1):
			p = (x, y)
			lights[p] = func(lights[p] if p in lights.keys() else 0)

def turn_on(brightness):
	return brightness + 1

def turn_off(brightness):
	return max(0, brightness - 1)

def toggle(brightness):
	return brightness + 2

def main():
	file_data = ''
	with open('input.txt', 'r') as f:
		file_data = f.read()

	instructions = [line.strip() for line in file_data.split('\n') if line]

	lights = {}
	for instruction in instructions:
		parts = instruction.split(' ')
		if parts[1] == 'on' or parts[1] == 'off':
			p1 = parse_point(parts[2])
			p2 = parse_point(parts[4])
			apply(lights, p1, p2, {
				'on': turn_on,
				'off': turn_off
			}[parts[1]])
		else: # toggle
			p1 = parse_point(parts[1])
			p2 = parse_point(parts[3])
			apply(lights, p1, p2, toggle)

	print(sum(lights.values()))

if __name__ == '__main__':
	main()
