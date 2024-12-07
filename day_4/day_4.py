with open('input.txt', 'r') as file:
    lines = file.readlines()

word_grid = [list(line.strip()) for line in lines]

# pt. 1
search_chars = ["X", "M", "A", "S"]
count = 0
for row in range(len(word_grid)):
    for col in range(len(word_grid[row])):
        if word_grid[row][col] == search_chars[0]:
            for direction in range(1, 9):
                valid_dir = True 
                for i in range(1, len(search_chars)):
                    valid_i = False
                    if direction == 1:
                        if row + i < len(word_grid) and word_grid[row + i][col] == search_chars[i]:
                            valid_i = True 

                    elif direction == 2: 
                        if row - i >= 0 and word_grid[row - i][col] == search_chars[i]:
                            valid_i = True

                    elif direction == 3:
                        if col + i < len(word_grid[row]) and word_grid[row][col + i] == search_chars[i]:
                            valid_i = True
                            
                    elif direction == 4: 
                        if col - i >= 0 and word_grid[row][col - i] == search_chars[i]:
                            valid_i = True

                    elif direction == 5:
                        if row + i < len(word_grid) and col + i < len(word_grid[row]) and word_grid[row + i][col + i] == search_chars[i]:
                            valid_i = True

                    elif direction == 6:
                        if row - i >= 0 and col - i >= 0 and word_grid[row - i][col - i] == search_chars[i]:
                            valid_i = True

                    elif direction == 7:
                        if row + i < len(word_grid) and col - i >= 0 and word_grid[row + i][col - i] == search_chars[i]:
                            valid_i = True

                    elif direction == 8:
                        if row - i >= 0 and col + i < len(word_grid[row]) and word_grid[row - i][col + i] == search_chars[i]:
                            valid_i = True

                    if not valid_i:
                        valid_dir = False
                        break

                if valid_dir:
                    count += 1
                    print("Found at", row, col, "Direction", direction)

print(f"pt 1: {count}")


# pt. 2
count = 0
for row in range(len(word_grid)):
    for col in range(len(word_grid[row])):
        if word_grid[row][col] == 'A' and (len(word_grid)-1 > row > 0) and (len(word_grid[row])-1 > col > 0):
            diag_1 = word_grid[row+1][col+1] + word_grid[row-1][col-1]
            diag_2 = word_grid[row+1][col-1] + word_grid[row-1][col+1]
            if (diag_1 == "MS" or diag_1 == "SM") and (diag_2 == "SM" or diag_2 == "MS"):
                print("Found at", row, col)
                count += 1

print(f"pt 2: {count}")
            
            










































