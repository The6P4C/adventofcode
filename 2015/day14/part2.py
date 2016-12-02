def main():
	file_data = ''
	with open('input.txt', 'r') as f:
		file_data = f.read()

	descriptions = [line.strip() for line in file_data.split('\n') if line]

	info = {}
	for description in descriptions:
		description_parts = description.split(' ')
		name = description_parts[0]

		info[name] = {
			'speed': int(description_parts[3]),
			'flying_time': int(description_parts[6]),
			'resting_time': int(description_parts[13])
		}

	current = {}
	for name in info.keys():
		current[name] = {
			'state': 'flying',
			'time_spent': 0,
			'distance': 0,
			'points': 0
		}

	for t in range(0, 2503):
		for name in current:
			data = current[name]
			if data['state'] == 'flying':
				data['distance'] += info[name]['speed']
				data['time_spent'] += 1

				if data['time_spent'] == info[name]['flying_time']:
					data['state'] = 'resting'
					data['time_spent'] = 0
			else:
				data['time_spent'] += 1
				if data['time_spent'] == info[name]['resting_time']:
					data['state'] = 'flying'
					data['time_spent'] = 0

		highest_distance = max([data['distance'] for data in current.values()])
		for name in current:
			data = current[name]
			if data['distance'] == highest_distance:
				data['points'] += 1

	print(max([data['points'] for data in current.values()]))

if __name__ == '__main__':
	main()
