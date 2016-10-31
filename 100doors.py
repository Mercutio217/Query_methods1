doors = [False] * 100

for i in range(100):
   for j in range (i, 100, i+1):
       doors[j] = not doors[j]

print("Opened doors:", end=' ')
for x in range(len(doors)):
    if doors[x] == 1:
        x = x+1
        print(x, end=",")
