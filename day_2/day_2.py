with open('input.txt', 'r') as file:
    lines = file.readlines()

lines = [line.strip().split(' ') for line in lines]

#lines = [
#    [48, 46, 47, 49, 51, 54, 56],
#    [1, 1, 2, 3, 4, 5],
#    [1, 2, 3, 4, 5, 5],
#    [5, 1, 2, 3, 4, 5],
#    [1, 4, 3, 2, 1],
#    [1, 6, 7, 8, 9],
#    [1, 2, 3, 4, 3],
#    [9, 8, 7, 6, 7],
#    [7, 10, 8, 10, 11],
#    [29, 28, 27, 25, 26, 25, 22, 20]
#]

def is_safe(line):
    ascending = True
    descending = True
    safe = True
    edits = 0
    editing = False
    for i in range(len(line)-1):
        cur = int(line[i])
        nex = int(line[i+1])

        distance = abs(cur - nex)
        if distance < 1 or distance > 3:
            safe = False
            break

        if cur >= nex:
            ascending = False
        elif cur <= nex:
            descending = False
        if not ascending and not descending:
            ascending = True
            descending = True 
            safe = False
            return safe
    return safe


safe_sum = 0
for line in lines:
    safe = is_safe(line)
    if safe:
        safe_sum += 1
    else:
        for i in range(len(line)):
            safe = is_safe(line[:i] + line[i+1:]) 
            if safe:
                safe_sum += 1
                break

 
print(safe_sum)




