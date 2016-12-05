def main():
	file_data = ''
	with open('input.txt', 'r') as f:
		file_data = f.read()

	lines = [line.strip() for line in file_data.split('\n') if line]
	instructions = [line.split(' ') for line in lines]

	pc = 0
	registers = {
		# Part 1
		'a': 0,
		# Part 2
		# 'a': 1,
		'b': 0
	}
	
	while pc >= 0 and pc < len(instructions):
		pc_increment = 1

		instruction = instructions[pc]

		op = instruction[0]
		operand1 = instruction[1].replace(',', '')
		operand2 = instruction[2] if len(instruction) == 3 else None

		if op == 'hlf':
			registers[operand1] /= 2
		elif op == 'tpl':
			registers[operand1] *= 3
		elif op == 'inc':
			registers[operand1] += 1
		elif op == 'jmp':
			pc_increment = int(operand1)
		elif op == 'jie':
			if registers[operand1] % 2 == 0:
				pc_increment = int(operand2)
		elif op == 'jio':
			if registers[operand1] == 1:
				pc_increment = int(operand2)

		pc += pc_increment

	print("a = {}, b = {}".format(registers['a'], registers['b']))

if __name__ == '__main__':
	main()
