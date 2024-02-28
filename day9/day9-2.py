from math import *

# opening the file 
with open("input9.txt","r") as file :
    lines=file.read().strip().split("\n")

# splitting the lines into a list of lists to get the things separated
# we will have the directory and then the distance we will travel in that direction
n=len(lines)
for i in range(n) :
    lines[i]=lines[i].split(" ")

# printing the lines to check if the file is read correctly
print(lines)

# function that checks if the head and tail are touching
def touching (head, tail) : 
    return (abs(head[0]-tail[0])<=1 and abs(head[1]-tail[1])<=1)

knots=[[0,0] for i in range(10)]

def move (dx, dy) : 
    global knots
    knots[0][0]+=dx
    knots[0][1]+=dy
    # we need to do the thing we've done before for all the knots
    for i in range(1, 10) :
        # function that moves the head and make the tail move that is following the head
        # the same as the previous code in part1 for two nots 
        head_x, head_y=knots[i-1][0], knots[i-1][1]
        tail_x, tail_y=knots[i][0], knots[i][1]
        # if the head and tail are touching, we don't have to move the tail 
        if not touching([head_x, head_y], [tail_x, tail_y]) : 
 
            # no need to move the tail on abscissa if the head and tail have the same abscissa
            if head_x==tail_x :
                sign_x=0
            # if the head is on the right of the tail, we move the tail to the right
            # if the head is on the left of the tail, we move the tail to the left
            # we use the sign of the difference between the head and the tail to know the direction
            else :
                sign_x=(head_x-tail_x)//abs(head_x-tail_x)
            
            # no need to move the tail on ordinate if the head and tail have the same ordinate
            if head_y==tail_y : 
                sign_y=0
            # if the head is on the top of the tail, we move the tail to the top
            # if the head is on the bottom of the tail, we move the tail to the bottom
            # we use the sign of the difference between the head and the tail to know the direction
            else :
                sign_y=(head_y-tail_y)//abs(head_y-tail_y)

            # moving the tail
            tail_x+=sign_x
            tail_y+=sign_y
        
        knots[i]=[tail_x, tail_y]
    

# making the directions dictionary
directions={"U":[0,1], "D":[0,-1], "R":[1,0], "L":[-1,0]}

# moving the head and tail according to the directions given in the file
# we must make a list of the points that the tail visited to calculate the result

# list of the points that the tail visited
visited=[]
# we're looking at what the file says us to do 
for instruction in lines : 
    # takin the infos 
    dx,dy=directions[instruction[0]]
    distance=int(instruction[1])
    for i in range(distance) :
        # making moves 
        move(dx, dy)
        # checking if the tail is in the list of the visited points
        if knots[9] not in visited :
            # if not, we add it to the list
            visited.append(knots[9])

# printing the result
print("The result is ", len(visited),"\n")

# the result is 1 as expected with test.txt
# the result is 36 as expected with test2.txt