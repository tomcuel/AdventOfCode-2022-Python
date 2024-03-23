# library to use 
from math import lcm
from heapq import heappop, heappush



# opening the file
with open("input24.txt","r") as file :
    grid=file.read().strip().split("\n")

n=len(grid) #number of rows
m=len(grid[0]) #number of columns

# where we start and end
start=(0,1)
end=(n-1,m-2)



# function to print the grid
def print_grid(grid):
    print("\ngrid :")
    print("\n".join(["".join(map(str, row)) for row in grid]),"\n")

# printing the grid to check it 
print_grid(grid)



# blizzard type of position, to calculate blizzard after every point 
arrows=">v<^"

# where we will move through the grid
directions=[[0,1],[1,0],[0,-1],[-1,0]]

# adding a set of points where there is initial blizzard
# we also have the type of direction the blizzard will go to at the next stage 
blizzard=set()
for i in range(n):
    for j in range(m):
        c=grid[i][j]
        if c in arrows:
            blizzard.add((i,j,arrows.index(c)))

# Things are the same after lcm(n, m) steps
period = lcm(n - 2, m - 2)
# we now get the states of the grid after every period
states_blizzard = [None] * period
# the first state of the grid is the initial blizzard from the input 
states_blizzard[0] = blizzard

# going through the period to get the states of the grid after every period
# starting from the second period (t=1) since we already have the first state
for t in range(1, period):
    # making a new set of blizzard for this round 
    new_storms = set()

    # we then go through each point of the blizzard of the previous period
    for storm in blizzard:
        # getting the row, column and direction of the blizzard
        row, col, d = storm
        # getting the direction associated with this type of blizzard
        drow, dcol = directions[d]
        # getting the new row and column of the blizzard, where it needs to be 
        new_row, new_col = row + drow, col + dcol

        # if the new row or column is a border point, we then need to change the position of the new blizzard
        # fully on top of the grid
        if new_row == 0:
            # if the direction is 3 (UP), we then need to change make the point to the other side of the map
            assert d == 3
            new_row = n - 2
        # fully on the bottom of the grid
        elif new_row == n - 1:
            # if the direction is 1 (DOWN), we then need to change make the point to the other side of the map
            assert d == 1
            new_row = 1
        # fully on the left of the grid
        if new_col == 0:
            # if the direction is 2 (LEFT), we then need to change make the point to the other side of the map
            assert d == 2
            new_col = m - 2
        # fully on the right of the grid
        elif new_col == m - 1:
            # if the direction is 0 (RIGHT), we then need to change make the point to the other side of the map
            assert d == 0
            new_col = 1

        # we then add the new position of the blizzard to the new set of blizzard
        new_storms.add((new_row, new_col, d))

    # we then update the states of the grid for this period, to be the corresponding blizzard
    states_blizzard[t] = new_storms
    blizzard = new_storms  # Update of the blizzard used for calculating the next period



# function to get the next state of the grid after every period
def grid_state(blizzard):
    ans = [["."] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            # if the point is a border point, we then marker it with a #
            # but not the entry and exit point
            if (i in [0, n - 1] or j in [0, m - 1]) and not (i, j) in [start, end]:
                ans[i][j] = "#"
                continue

            # this loop if skipped if the point is a border point
            # we then go through the type of blizzard and see if the point is in the blizzard
            # we then can get to type of blizzard and add it to the point, to have the grid state 
            for d in range(4):
                if (i, j, d) in blizzard:
                    # if there is another blizzard already in the point, we then add 1 to the point, so we have one more blizzard
                    if isinstance(ans[i][j], int):
                        ans[i][j] += 1
                    # 
                    elif ans[i][j] != ".":
                        ans[i][j] = 2
                    # if there is no blizzard in the point, we then add the type of blizzard to the point
                    else:
                        ans[i][j] = arrows[d]

    return ans



# function to know if a point (loc) is in the state (st) of the grid
# if this point is already occupied by a blizzard, for this step and so the next one 
def occupied(loc, st):
    for d in range(4):
        if (loc[0], loc[1], d) in st:
            return True
    return False



# doing the BFS algorithm to get the shortest path from the start to the end
# we then start from the start point, using heap to get the shortest path
heap=[(0,start)]
visited=set()

# stopping condition
while len(heap) > 0 : 
    point=heappop(heap)

    # if we've already visited the point, we then skip it
    if point in visited:
        continue
    # otherwise, we then add the point to the visited set
    visited.add(point)

    time, location = point
    row, col = location

    # looking if the point is not in a blizzard state
    assert not occupied(location, states_blizzard[time % period])

    # stopping condition
    if location == end:
        print("\nThe shortest path is time is : ",time,"\n")
        break

    # going through the neighbors of the point
    # we can stay stationary, or move in one of the four directions
    # so we need to add the [[0,0]] to the directions
    for drow, dcol in (directions+[[0,0]]):
        new_row, new_col = row + drow, col + dcol
        new_location = (new_row, new_col)

        # we need to see if the point is still inside the grid 
        # if it's not the start or the end point, or any "#" point (border point)
        if (not new_location in [start, end]) and not (1 <= new_row <= n - 2 and 1 <= new_col <= m - 2):
            continue

        # if the point is in a blizzard state at the next, we then skip it
        if occupied(new_location, states_blizzard[(time + 1) % period]):
            continue

        # udpating the heap with the new point
        new_point= (time + 1, new_location)
        heappush(heap, new_point)

   

# we found 18 as expected with the test.txt file