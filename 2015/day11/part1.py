INPUT = 'hijklmmn'

def increment(s):
	if len(s) == 0:
		return ''
	else:
		c = s[-1]
		if c == 'z':
			return increment(s[0:-1]) + 'a'
		else:
			return s[0:-1] + chr(ord(c) + 1)

def next_password(prev_password):
	password = increment(prev_password)
	while not is_valid(password):
		password = increment(password)
	return password

def is_valid(password):
	increasing_straight_count = 0
	for i, c in enumerate(password[0:-2]):
		substr = password[i:i+3]
		
		if ord(substr[0]) + 1 == ord(substr[1]) and ord(substr[1]) + 1 == ord(substr[2]):
			increasing_straight_count += 1

	if increasing_straight_count == 0:
		return False

	for c in password:
		if c in ['i', 'o', 'l']:
			return False

	pairs = []
	for i, c in enumerate(password[0:-1]):
		substr = password[i:i+2]
		if substr[0] == substr[1] and substr not in pairs:
			pairs.append(substr)

	if len(pairs) < 2:
		return False

	return True

def main():
	print("Part 1:")
	new_password = next_password('hepxcrrq')
	print(new_password)

	print("Part 2:")
	print(next_password(new_password))

if __name__ == '__main__':
	main()
