import math

def increment(arr):
	if len(arr) == 1:
		if arr[0] == 100:
			return [-1]
		else:
			return [arr[0] + 1]

	if arr[-1] == 100:
		return increment(arr[0:-1]) + [0]
	else:
		arr[-1] += 1
		return arr

def totals(n):
	value = [0] * n
	while True:
		if sum(value) == 100:
			yield value

		value = increment(value)
		if value[0] == -1:
			break

def cook(totals, ingredient_data):
	final_product = {
		'capacity': 0,
		'durability': 0,
		'flavor': 0,
		'texture': 0,
		'calories': 0
	}

	for i in range(0, len(totals)):
		total = totals[i]
		current_ingredient_data = ingredient_data[i]
		
		for prop in final_product:
			final_product[prop] += current_ingredient_data[prop] * total

	if final_product['calories'] != 500:
		return -1

	final_product['calories'] = 1

	acc = 1
	for v in final_product.values():
		acc *= max(0, v)

	return acc

def main():
	file_data = ''
	with open('input.txt', 'r') as f:
		file_data = f.read()

	ingredient_data_strings = [line.strip() for line in file_data.split('\n') if line]

	ingredient_data = []
	for ingredient_data_string in ingredient_data_strings:
		parts = ingredient_data_string.split(' ')
		ingredient_data.append({
			'capacity': int(parts[2][0:-1]),
			'durability': int(parts[4][0:-1]),
			'flavor': int(parts[6][0:-1]),
			'texture': int(parts[8][0:-1]),
			'calories': int(parts[10])
		})

	scores = []
	for total in totals(len(ingredient_data)):
		scores.append(cook(total, ingredient_data))
	print(max(scores))

if __name__ == '__main__':
	main()
