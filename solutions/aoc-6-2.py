#Day 6- The biggest joke in the hitory of AOC?!
import numpy as np

time = 58996469
distance = 478223210191071

ans = list()

counter = 0
for j in range(time):

	if (time - j) * j > distance:
		counter += 1
ans.append(counter)

print(np.prod(ans))