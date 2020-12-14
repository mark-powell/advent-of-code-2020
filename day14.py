lines = open('day14_input.txt').readlines()

memory = {}
for line in lines:
    if line[:4] == 'mask':
        mask = list(line[7:].strip())
        continue
    memoryAddress = int(line[line.find('[') + 1:line.find(']')])
    value = list(format(int(line[line.find('=') + 2:]), '036b'))
    for i in range(len(mask)):
        if mask[i] == 'X':
            continue
        value[i] = mask[i]
    value = ''.join(value)
    memory[memoryAddress] = int('0b'+value, 2)
    
total = 0
for v in memory:
    total += memory[v]

print('Part 1:', total)

memory = {}
for line in lines:
    if line[:4] == 'mask':
        mask = list(line[7:].strip())
        continue
    memoryAddress = list(format(int(line[line.find('[') + 1:line.find(']')]), '036b'))
    value = int(line[line.find('=') + 2:])
    for i in range(len(mask)):
        if mask[i] == '0':
            continue
        memoryAddress[i] = mask[i]
    floaters = [i for i, x in enumerate(memoryAddress) if x == "X"]
    for i in range(2**len(floaters)):
        config = list(format(i, '0'+str(len(floaters))+'b'))
        for c in range(len(config)):
            memoryAddress[floaters[c]] = config[c]
        newMemoryAddress = ''.join(memoryAddress)
        memory[newMemoryAddress] = value

total = 0
for v in memory:
    total += memory[v]

print('Part 2:', total)

