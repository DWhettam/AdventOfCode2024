import numpy as np

left = []
right = []

with open('input.txt', 'r') as file:  
    for line in file:
        columns = line.split()
        left.append(int(columns[0]))
        right.append(int(columns[1]))

left = np.asarray(sorted(left))
right = np.asarray(sorted(right))

distance = 0
sim_score = 0
for pair in zip(left, right):
    distance += abs(pair[0] - pair[1])
    right_instances = np.where(right == pair[0])[0]
    sim_score += pair[0] * len(right_instances)

print(f"Distance: {distance}")
print(f"Similarity score: {sim_score}")

