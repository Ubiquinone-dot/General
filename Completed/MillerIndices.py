# Produce all values of HKL for each value of h^2 + k^2 + l^2 = n given a limit n

n = 20+1
limhkl = int(n**0.5+1)

space = [[h for h in range(limhkl)], [h for h in range(limhkl)], [h for h in range(limhkl)]]
print(space)

indices = [[] for _ in range(n)]
print(indices)
for i in range(n):
    for h in space[0]:
        for k in space[1]:
            for l in space[2]:
                if h**2 + k**2 + l**2 == i:
                    indices[i].append((h,k,l))


print(indices)
for n in range(n):
    print(i, 'values:', indices[i])