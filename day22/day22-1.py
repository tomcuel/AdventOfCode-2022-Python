# opening the file 
with open("input22.txt","r") as file:
    # Assumes input ends with newline character
    parts = file.read()[:-1].split("\n\n")

# Splitting the input into board and commands
# the first part is the board
board=parts[0].split("\n")
# print("Board :")
# for line in board : 
#    print(line)
# the second part is the commands
command_input=parts[1]
# print("\nCommands :",commands,"\n")



# Parse the commands
idx = 0
commands = []
cur_num = ""
for idx in range(len(command_input)):
    # If the character is a digit, add it to the current number, we add it as a string so we can convert it to an integer later
    # it's in the good order here
    if command_input[idx].isdigit():
        cur_num += command_input[idx]

    # If the character is a letter, add the letter to the commands list
    # add the current number to the commands list
    # reset the current number
    else:
        commands.append(int(cur_num))
        cur_num = ""
        commands.append(command_input[idx])

# If last command is a number
if cur_num != "":
    commands.append(int(cur_num))



# Parse the board
# Get the number of rows and columns
nrows = len(board)
ncols = max([len(row) for row in board])

# Initialising the bounds of the board
# bond_row is a list of list, each list contains the min and max column index of the row where we can go
# bound_col is a list of list, each list contains the min and max row index of the column where we can go
bound_row = [[ncols, -1] for _ in range(nrows)]
bound_col = [[nrows, -1] for _ in range(ncols)]

# getting the cells we can go to on the board with a set 
adj = set()
# Loop through the board
for row, line in enumerate(board):
    for col in range(len(line)):
        c = line[col]
        # If the cell is a dot, add it to the set of cells we can go to
        if c == ".":
            adj.add((row, col))

        # If the cell is a dot or a hashtag, update the bounds of the board
        # it means that this row or column is not empty and is part of the map
        # we update the bounds, given what we have seen so far
        if c in [".", "#"]:
            bound_row[row][0] = min(bound_row[row][0], col)
            bound_row[row][1] = max(bound_row[row][1], col)
            bound_col[col][0] = min(bound_col[col][0], row)
            bound_col[col][1] = max(bound_col[col][1], row)



# Possible directions
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# Do the commands
direction = 0
# Start at the top left corner, the first point where it's not empty
row = 0
col = bound_row[0][0]

# going through the commands to move through the board
for cmd in commands : 
    # if it's a str (R or L), we make the rotation of the command
    if isinstance(cmd, str):

        if cmd == "L" : 
            # rotating of 90 degrees anti-clockwise
            direction = (direction - 1) % 4
        else : 
            # rotating of 90 degrees clockwise
            direction = (direction + 1) % 4

        # we're skipping the next part of the loop
        continue

    drow, dcol = directions[direction]

    for _ in range (cmd):
        # if (row, col) isn't on the board or is a rock ("#"), we need to break the loop
        if (row,col) not in adj:
            break

        # otherwise, we move udpating the row and the column
        new_row = row + drow
        new_col = col + dcol

        # if we move to the top or the bottom of the board, we need to update the row by making sure we don't go out of the bounds
        # we then need to reappear on the other side, that's why we use the modulo
        if drow != 0:
            height = bound_col[col][1] - bound_col[col][0] + 1
            new_row = (new_row - bound_col[col][0]) % height + bound_col[col][0]

        # if we move to the left or the right of the board, we need to update the column by making sure we don't go out of the bounds
        # we then need to reappear on the other side, that's why we use the modulo
        if dcol != 0:
            width = bound_row[row][1] - bound_row[row][0] + 1
            new_col = (new_col - bound_row[row][0]) % width + bound_row[row][0]

        # if the new cell is not in the adj set, we break the loop
        if (new_row, new_col) not in adj:
            break

        # otherwise, we update the row and the column, since there are valid
        row, col = new_row, new_col



print("Row :",row+1)
print("Column :",col+1)
print("Direction :",direction)
# there is a +1 difference between the row and the column in reality since we do not strat from 0 in real life
# we need to add it
# for the facing : the last direction taken corresponds to the numbers of the arrow
answer=1000*(row+1)+4*(col+1)+direction
print("Answer :",answer)



# we found 6032 as expected with the test.txt file 