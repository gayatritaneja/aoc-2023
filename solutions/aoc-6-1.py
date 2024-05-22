import numpy as np

time = [58, 99, 64, 69]
distance = [478, 2232, 1019, 1071]

ans = list()

for i in range(len(time)):

	counter = 0
	for j in range(time[i]):

		if (time[i] - j) * j > distance[i]:
			counter += 1
	ans.append(counter)

print(np.prod(ans))
