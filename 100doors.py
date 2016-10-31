doors = [False] * 100

for i in range(100):
   for j in range (i, 100, i+1):
       doors[j] = not doors[j]

print("The following doors are open: ", end=' ')
for index, res in enumerate(doors):
    if res == 1:
       print(index + 1, end=", ")
