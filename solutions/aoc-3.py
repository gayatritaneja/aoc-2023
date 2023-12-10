#an attempt which doesn't work for all cases but works for the sample test case
with open("input_3.txt", "r") as f:


	lines = f.read().split("\n")

	arr_list = list()


	for line in lines:
		line = list(line)
		arr_list.append(line)

	ans = list()

	sp_sym = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "/", "_", "="]

	for i, elem in enumerate(arr_list):

		for ind, subelem in enumerate(arr_list[i]):

			if subelem.isdigit():

				try:
					if arr_list[i][ind + 1].isdigit() and arr_list[i][ind + 2].isdigit():	
						num = int(str(subelem) + str(arr_list[i][ind + 1]) + str(arr_list[i][ind + 2]))

						positions = [(-1, -1), (-1, 0), (-1, 1),(0, -1), (0, 1),(1, -1), (1, 0), (1, 1)]


						surrounding_elements = []
						for j in range(3):

							for pos in positions:

								new_row, new_col = i + pos[0], ind+j + pos[1]
								if 0 <= new_row < len(arr_list) and 0 <= new_col < len(arr_list[new_row]):

									surrounding_elements.append(arr_list[new_row][new_col])

						for sur in surrounding_elements:
							if not sur.isdigit() and not sur.isalpha() and not sur == ".":
								ans.append(num)
								break

				except IndexError:
					print("IndexError in line", i)

				try:

					if arr_list[i][ind + 1].isdigit() and not arr_list[i][ind + 2].isdigit() and not arr_list[i][ind -1].isdigit() and not arr_list[i][ind -2].isdigit():	
						num = int(str(subelem) + str(arr_list[i][ind + 1]))

						positions = [(-1, -1), (-1, 0), (-1, 1),(0, -1), (0, 1),(1, -1), (1, 0), (1, 1)]


						surrounding_elements = []
						for j in range(2):

							for pos in positions:

								new_row, new_col = i + pos[0], ind+j + pos[1]
								if 0 <= new_row < len(arr_list) and 0 <= new_col < len(arr_list[new_row]):

									surrounding_elements.append(arr_list[new_row][new_col])

						for sur in surrounding_elements:
							if not sur.isdigit() and not sur.isalpha() and not sur == ".":
								ans.append(num)
								break
				except IndexError:
					print("IndexError in line", i)


				try:

					if arr_list[i][ind].isdigit() and not arr_list[i][ind + 2].isdigit() and not arr_list[i][ind -1].isdigit() and not arr_list[i][ind -2].isdigit() and not arr_list[i][ind + 1].isdigit():	
						num = int(str(subelem))

						positions = [(-1, -1), (-1, 0), (-1, 1),(0, -1), (0, 1),(1, -1), (1, 0), (1, 1)]


						surrounding_elements = []
						for j in range(2):

							for pos in positions:

								new_row, new_col = i + pos[0], ind+j + pos[1]
								if 0 <= new_row < len(arr_list) and 0 <= new_col < len(arr_list[new_row]):

									surrounding_elements.append(arr_list[new_row][new_col])

						for sur in surrounding_elements:
							if not sur.isdigit() and not sur.isalpha() and not sur == ".":
								ans.append(num)
								break
				except IndexError:
					print("IndexError in line", i)

	print(ans)
