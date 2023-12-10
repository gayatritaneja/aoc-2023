with open("input_2.txt", "r") as f:

	lines = f.read()
	lines = lines.split("\n")

	ans = list()

	for line in lines:

		line_num = lines.index(line) + 1

		color_count = {"red": [], "green": [], "blue": []}

		ind = line.index(":") + 2
		line = line[ind:]

		line = line.split("; ")


		for entry in line:

			entry = entry.split(", ")

			for elem in entry:

				if "red" in elem:
					color_count["red"].append(int(elem[:-3]))

				elif "green" in elem:
					color_count["green"].append(int(elem[:-5]))

				elif "blue" in elem:
					color_count["blue"].append(int(elem[:-4]))
		


		power = max(color_count["red"]) * max(color_count["green"]) * max(color_count["blue"])
		ans.append(power)

	print(sum(ans))