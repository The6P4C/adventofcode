ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def decrypt(name, key):
	decrypted = ''
	for c in name:
		if c != ' ':
			decrypted += ALPHABET[(ALPHABET.index(c) + key) % len(ALPHABET)]
		else:
			decrypted += ' '
	return decrypted

def checksum(name):
	counts = {}
	for c in name:
		if c in counts.keys():
			counts[c] += 1
		else:
			counts[c] = 1
	
	checksum = ''
	for i in range(max(counts.values()), 0, -1):
		chars = ''
		for c, n in counts.items():
			if n == i:
				chars += c
		checksum += ''.join(sorted(chars))

	return checksum[0:5]

def main():
	file_data = ''
	with open('input.txt', 'r') as f:
		file_data = f.read()

	room_strings = [line.strip() for line in file_data.split('\n') if line]

	for room_string in room_strings:
		name_and_id_split = room_string[:-7].split('-')

		name = ' '.join(name_and_id_split[:-1])
		id = int(name_and_id_split[-1])

		possible_checksum = room_string[-6:-1]

		if possible_checksum == checksum(name.replace(' ', '')) and 'north' in decrypt(name, id):
			print(id)

if __name__ == '__main__':
	main()
