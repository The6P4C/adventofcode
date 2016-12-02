ANALYSIS = {
	'children': 3,
	'cats': 7,
	'samoyeds': 2,
	'pomeranians': 3,
	'akitas': 0,
	'vizslas': 0,
	'goldfish': 5,
	'trees': 3,
	'cars': 2,
	'perfumes': 1,
}

def main():
	file_data = ''
	with open('input.txt', 'r') as f:
		file_data = f.read()

	sue_text_descriptions = [line.strip() for line in file_data.split('\n') if line]
	sue_data = {}
	for sue_text_description in sue_text_descriptions:
		parts = sue_text_description.split(' ')
		sue_number = int(parts[1][:-1])

		sue_data[sue_number] = {}

		posessions_strings = parts[2:]
		for i in range(0, len(posessions_strings) // 2):
			thing = posessions_strings[i * 2][:-1]
			amount = int(posessions_strings[i * 2 + 1].replace(',', ''))
			
			sue_data[sue_number][thing] = amount

	for sue_number in sue_data:
		sue = sue_data[sue_number]

		all_matched = True
		for thing in sue:
			if thing in ['cats', 'trees']:
				is_match = sue[thing] > ANALYSIS[thing] 
				all_matched = all_matched and is_match
			elif thing in ['pomeranians', 'goldfish']:
				is_match = sue[thing] < ANALYSIS[thing]
				all_matched = all_matched and is_match
			else:
				is_match = sue[thing] == ANALYSIS[thing]
				all_matched = all_matched and is_match

		if all_matched:
			print(sue_number)

if __name__ == '__main__':
	main()
