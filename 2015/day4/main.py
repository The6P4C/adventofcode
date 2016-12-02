import hashlib

SECRET_KEY = 'iwrupvqb'

# Part 1
#NUM_ZEROS = 5

# Part 2
NUM_ZEROS = 6

def main():
	i = 0
	while True:
		value_to_hash = SECRET_KEY + str(i)
		m = hashlib.md5()
		m.update(value_to_hash.encode('ascii'))
		hash = m.hexdigest()

		test = [x for x in hash[0:NUM_ZEROS] if x == '0']

		if len(test) == NUM_ZEROS:
			print(i)
			print(value_to_hash)
			print(hash)
			break
		
		i += 1

if __name__ == '__main__':
	main()
