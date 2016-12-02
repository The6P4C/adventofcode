import re

# Part 1
# def is_nice(s):
# 	vowel_count = len([c for c in s if c in 'aeiou'])
# 	double_letter_count = len(re.findall(r'(.)\1', s))
# 	bad_count = len(re.findall(r'ab|cd|pq|xy', s))

# 	return vowel_count >= 3 and double_letter_count >= 1 and bad_count == 0

# Part 2
# def is_nice(s):
# 	repeated_pair_count = len(re.findall(r'(..).*\1', s))
# 	letter_repeat_count = len(re.findall(r'(.).\1', s))

# 	return repeated_pair_count >= 1 and letter_repeat_count >= 1

def main():
	file_data = ''
	with open('input.txt', 'r') as f:
		file_data = f.read()

	strings = [s.strip() for s in file_data.split('\n') if s]
	nice_strings = [s for s in strings if is_nice(s)]
	print(len(nice_strings))

if __name__ == '__main__':
	main()
