with open("input_4.txt", "r") as f:

	lines = f.read()
	lines = lines.split("\n")

	ans = list()

	for line in lines:

		line_num = lines.index(line) + 1

		ind = line.index(":") + 2
		line = line[ind:]

		line1, line2 = line.split(" | ")

		line1 = line1.split()
		line2 = line2.split()

		counter = 0

		for elem in line2:
			if elem in line1:
				counter += 1

		if counter > 0:
			gp_term = 1 * (2 ** (counter - 1))
		else:
			gp_term = 0

		ans.append(gp_term)
	print(sum(ans))

