# converting the alphabet into the integer value that correponds to each letter 
from string import ascii_lowercase 
# importing the heap
from heapq import heappop, heappush

# reading the file 
with open("input12.txt","r") as file: 
    map = file.read().strip().split("\n")

# to see the input 
print("input:")
for line in map : 
    print(line)
print()

# to simplify the following code 
n=len(map)
m=len(map[0])

# comming from the subject 
height_of_start = 0 
heigth_of_end = 25

# searching the beginning (S) and the end (E) of the maze
for i in range(len(map)) :
    for j in range(len(map[i])) : 
        if map[i][j] == "S" : 
            start = i,j
        if map[i][j] == "E" : 
            end = i,j

print("start:",start)
print("end:",end)

# function to convert the letter into the integer value corresponding to it 
def heigth(s) :
    if s in ascii_lowercase:
        return ascii_lowercase.index(s)
    if s == "S":
        return height_of_start
    if s == "E":
        return heigth_of_end
    
# function that returns the possible neighbors of a point of the map 
def possible_neighbors(i,j) :
    neighbors=[]
    # we're going to check the 4 possible neighbors of the point : right, left, up and down
    for di,dj in [(1,0),(-1,0),(0,1),(0,-1)] : 
        # getting the coordinates of the neighbor
        ii=i+di
        jj=j+dj
        # checking if the neighbor is in the map
        # but mainly if the height bewteen the point and the neighbor is less than 1 for the next step
        if 0<=ii<n and 0<=jj<m and heigth(map[ii][jj]) <= heigth(map[i][j])+1:
            neighbors.append((ii,jj))

    return neighbors
 
# we're now making graphs theorie to find the shortest path 
# we're going to use the djisktra algorithm

# creating the array of the point of the map we visited 
visited = [[False]*m for _ in range(n)]
# creating the heap that will contain the point of the map we're going to visit
heap=[(0,start[0],start[1])]
# while the heap is not empty 
while True : 
    steps, i, j = heappop(heap)

    # if we already visited the point
    if visited[i][j] : 
        continue
    # we're now visiting the point
    visited[i][j] = True

    # if we reach the end of the maze
    if (i,j) == end : 
        print("number of steps:",steps)
        break

    # otherwise, we're now going to visit the neighbors of the point
    for ii,jj in possible_neighbors(i,j) :
        # we're now adding the neighbor to the heap
        heappush(heap,(steps+1,ii,jj))

# the result is 31 for the test.txt file as expected