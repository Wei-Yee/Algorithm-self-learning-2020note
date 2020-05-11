import numpy as np

n = int(input())
list1 = []

while True:
    t = input()
    list1.append(tuple(map(int, t.split())))
    if t[0] == '0':
        break

price = [item for t in list1 for item in t]

for i in range(len(price) - 1, -1, -1):
    if i % 2 == 0:
        del price[i]

T = np.zeros((len(price), n + 1))

for i in range(0, len(price)):
    for j in range(0, n + 1):

        # First column => 0 length of rod => 0 profit
        if j == 0:
            continue

            # First row => T[i-1,j] doesn't exist so just pick the second value
        elif i == 0:
            T[i, j] = price[i] + T[i, j - i - 1]

            # where j <= i => T[i, j-i-1] doesn't exist so just pick the first value
        elif (j - i - 1) < 0:
            T[i, j] = T[i - 1, j]

            # using the whole expression
        else:
            T[i, j] = max(T[i - 1, j], (price[i] + T[i, j - i - 1]))

        # Answer in the extreme bottom right cell
x = T[len(price) - 1, n]
Ans = int(x)
print(Ans)