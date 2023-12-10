with open("input_1.txt", "r") as f:

	lines = f.readlines()

	nums = {'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r', 'five': 'f5e', 'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'}

	new_lines = list()
	
	num_list = list()

	for line in lines:
		temp_lines = list()
		for i, n in nums.items():
	
			if i in line:
				line = line.replace(i, n)
				temp_lines.append(line)

		if len(temp_lines) != 0:
			new_lines.append(temp_lines[-1])
		else:
			new_lines.append(line)

	print(new_lines)

	for newline in new_lines:

		num = ""
		for char1 in newline:

			if char1.isdigit():
				num = str(char1)
				break

		line_rev = newline[::-1]

		for char2 in line_rev:
			if char2.isdigit():
				num += str(char2)
				break

		num_list.append(int(num))

	print(sum(num_list))

