import hashlib

DOOR_ID = 'ojvtpuvg'

def main():
	password = [' '] * 8
	i = 0

	while len([c for c in password if c != ' ']) != 8:
		value_to_hash = DOOR_ID + str(i)

		m = hashlib.md5()
		m.update(value_to_hash.encode('ascii'))
		hash = m.hexdigest()

		test = [x for x in hash[0:5] if x == '0']

		if len(test) == 5:
			index = hash[5]
			if index not in 'abcdef':
				index = int(index)
				if index < 8 and password[index] == ' ':
					password[index] = hash[6]
					print(''.join(password), flush=True)

		i += 1

if __name__ == '__main__':
	main()
