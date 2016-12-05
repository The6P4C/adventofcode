import hashlib

DOOR_ID = 'ojvtpuvg'

def main():
	password = ''
	i = 0

	while len(password) != 8:
		value_to_hash = DOOR_ID + str(i)

		m = hashlib.md5()
		m.update(value_to_hash.encode('ascii'))
		hash = m.hexdigest()

		test = [x for x in hash[0:5] if x == '0']

		if len(test) == 5:
			password += hash[5]
			print(password, flush=True)

		i += 1

if __name__ == '__main__':
	main()
