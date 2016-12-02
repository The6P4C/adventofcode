import re

INPUT = '3113322113'

# Part 1
# NUMBER_OF_TIMES = 40

# Part 2
# NUMBER_OF_TIMES = 50

def look_and_say(s):
	instances = re.findall(r'((.)\2*)', s)
	
	new_string = ''
	for instance in instances:
		new_string += str(len(instance[0]))
		new_string += instance[1]

	return new_string

def main():
	s = INPUT
	for i in range(0, NUMBER_OF_TIMES):
		s = look_and_say(s)

	print(len(s))

if __name__ == '__main__':
	main()
