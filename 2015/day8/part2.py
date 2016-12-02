def encode(s):
	escaped = s.translate(str.maketrans({
		'"': '\\"',
		'\\': '\\\\'
	}))
	return '"' + escaped + '"'

def main():
	file_data = ''
	with open("input.txt", 'r') as f:
		file_data = f.read()

	strings = [line.strip() for line in file_data.split('\n') if line]

	code_lengths = sum([len(s) for s in strings])

	encoded_lengths = 0
	for s in strings:
		encoded = encode(s)
		encoded_lengths += len(encoded)

	print(encoded_lengths - code_lengths)

if __name__ == '__main__':
	main()
