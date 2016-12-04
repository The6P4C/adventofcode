def get_transformations(initial_molecule, rule):
	rule_from = rule[0]
	rule_to = rule[1]

	transformations = []
	for i in range(0, len(initial_molecule) - len(rule_from) + 1):
		possible_from = initial_molecule[i:i + len(rule_from)]
		
		if possible_from == rule_from:
			transformed = initial_molecule[:i] + rule_to + initial_molecule[i + len(rule_from):]
			transformations.append(transformed)

	return transformations

def main():
	file_data = ''
	with open('input.txt', 'r') as f:
		file_data = f.read()

	lines = [line.strip() for line in file_data.split('\n') if line]

	rule_strings = lines[:-1]
	rules = []
	for rule_string in rule_strings:
		parts = rule_string.split('=>')
		rules.append((parts[0].strip(), parts[1].strip()))

	initial_molecule = lines[-1]

	transformations = []
	for rule in rules:
		rule_transformations = get_transformations(initial_molecule, rule)
		for transformation in rule_transformations:
			if transformation not in transformations:
				transformations.append(transformation)

	print(len(transformations))

if __name__ == '__main__':
	main()
