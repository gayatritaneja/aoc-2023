with open("input_1.txt", "r") as f:

	lines = f.readlines()

	num_list = list()


	for line in lines:

		num = ""
		for char1 in line:

			if char1.isdigit():
				num = str(char1)
				break

		line_rev = line[::-1]

		for char2 in line_rev:
			if char2.isdigit():
				num += str(char2)
				break

		num_list.append(int(num))

	print(sum(num_list))
