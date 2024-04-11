x = []

for i in range(3):
    y = int(input())
    x.append(y)
    if y <= 0:
        x[i] = 1

for i in range(3):
    #print(f"X[{i}] = {x[i]}")
    print("X[%d] ="%i, x[i])
    


