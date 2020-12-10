lines = open('day10_input.txt').readlines()

adapters = [int(l.strip()) for l in lines]
adapters.append(0)
adapters.append(max(adapters) + 3)
adapters.sort()

jumps = []
for i in range(1, len(adapters)):
    jumps.append(adapters[i] - adapters[i - 1])

print('Part 1:', jumps.count(1)*jumps.count(3))

pathCounts = [1] * (adapters[-1] + 1)
for d in adapters[1:]:
    count = []
    for n in range(d - 3, d):
        if n in adapters:
            count.append(pathCounts[n])
    pathCounts[d] = sum(count)
    
print('Part 2:', pathCounts[-1])



