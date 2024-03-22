from collections import defaultdict 

# opening the files 
with open("input23.txt","r") as file : 
    grid=file.read().strip().split("\n")

n=len(grid) #number of rows
m=len(grid[0]) #number of columns
# print("\ngrid: ")
# for line in grid:
#     print(line)
# print("\n")


# N,S,E,W,NE,NW,SE,SW
directions = [
    [0, 1],
    [-1, 1],
    [-1, 0],
    [-1, -1],
    [0, -1],
    [1, -1],
    [1, 0],
    [1, 1]
]


# finding the elves
elves = set()
for i in range(n):
    for j in range(m):
        if grid[i][j] == '#':
            elves.add((i, j))
# print("elves : \n",elves,"\n")


# function to print the output
def print_grid(grid, elves):
    print("grid at the final state : ")
    for i in range(n):
        for j in range(m):
            if (i, j) in elves:
                print("#", end="")
            else:
                print(grid[i][j], end="")
        print()
    print()


# checks to see if the elves are in the right place or not

# If there is no Elf in the N, NE, or NW adjacent positions, the Elf proposes moving north one step.
# we take the exemple of check[3] : 
# if there is no elf in NE(1), N(0), NW(7) then we can move N(0)
# we look if there is no elf in the first part of checks
# we make the proposal to move in this direction in that case
checks = [
    [[1, 2, 3], 2],
    [[7, 6, 5], 6],
    [[5, 4, 3], 4],
    [[1, 0, 7], 0]
]


# number of rounds to do
nb_rounds = 10
for i in range(nb_rounds) : 
    # Stage 1: make proposals
    propose = {}
    proposed = defaultdict(int)
    for elf in elves:
        row, col = elf

        # Check if elf has neighbors
        has_neighbours = False
        # going through the directions
        for drow, dcol in directions :
            # if the elf has a neighbor, then we need to quit the loop
            if (row + drow, col + dcol) in elves:
                has_neighbours = True
                break
        # If elf has no neighbors, continue
        if not has_neighbours:
            continue

        # going through the directions
        for check_direction, proposed_direction in checks:
            has_neighbours = True
            # going through the directions we need to check now
            for d in check_direction:
                drow, dcol = directions[d]
                if (row + drow, col + dcol) in elves:
                    has_neighbours = False
                    break
            
            # if we can't move in this direction, then we need to continue
            # we skip the rest of the loop
            if not has_neighbours:
                continue

            # if we can move in this direction, then we need to propose it
            drow, dcol = directions[proposed_direction]
            propose[elf] = (row + drow, col + dcol) # what new place this elf "elf" propose 
            # we increment the number of proposals for the new place
            proposed[propose[elf]] += 1
            break


    # Stage 2 : do the proposals
    new_elves = set()
    for elf in elves:
        # if elf is in the propose, then we need to check if we can accept the proposal or not
        if elf in propose:
            # getting the new location, the elf is wanting to go to
            new_loc = propose[elf]
            # if there's no elf in the new location, or if there's more than one elf in the new location
            # then we need to keep the elf in the new_elves at the same place
            if proposed[new_loc] == 0 or proposed[new_loc] > 1 : 
                new_elves.add(elf)
            # otherwise, we need to move the elf to the new location
            else:
                new_elves.add(new_loc)
        # if elv isn"t in the propose, then we need to keep it in the new_elves as it is
        else:
            new_elves.add(elf)

    # Rotate stuff 
    checks = checks[1:] + [checks[0]]
    elves = new_elves

    # printing the grid after the round, to see the changes, and see wether i'm good or not
    #print("after the round",i+1,": ",end="")
    #print_grid(grid, elves)



# to see the final state of the grid
print_grid(grid, elves)



# function to get the index of the elves that are making the edges of the rectangle 
def get_bounds(elves):
    # initial values, so that we don't get wrong results, by intializing them under or above what's needed 
    min_row = 1 << 60
    max_row = -(1 << 60)
    min_col = 1 << 60
    max_col = -(1 << 60)

    for row, col in elves:
        min_row = min(min_row, row)
        max_row = max(max_row, row)

        min_col = min(min_col, col)
        max_col = max(max_col, col)

    return min_row, max_row, min_col, max_col

# getting them
min_row, max_row, min_col, max_col = get_bounds(elves)
print("min_row, max_row :",min_row, max_row)
print("min_col, max_col :",min_col, max_col)


# get the area of the rectangle, but we need to remove the elves from the area to get the free ground 
answer=(max_row-min_row+1)*(max_col-min_col+1)-len(elves)
print("answer : ",answer)


# finding 110 as expected for test.txt