with open("input_4.txt", "r") as f:

	lines = f.read()
	lines = lines.split("\n")

	ans = dict()
	coll_cards_main = list()
	main_ans = list()


	for line in lines:

		coll_cards = list()
		card = lines.index(line) + 1

		ind = line.index(":") + 2
		line = line[ind:]

		line1, line2 = line.split(" | ")

		line1 = line1.split()
		line2 = line2.split()

		counter = 0

		for elem in line2:
			if elem in line1:
				counter += 1

		for i in range(1, counter+1):
			coll_cards.append(i + card)
			coll_cards_main.append(i+card)

		ans[card] = (coll_cards)

	for i in range(1, len(lines)+1):
		count = coll_cards_main.count(i)
		tba = count*ans[i]
		coll_cards_main.extend(count * ans[i])

	print(len(coll_cards_main) + len(lines))