import numpy as np

# opening the file 
with open("input18.txt","r") as file : 
    lines= file.read().strip().split("\n")


# for line in lines : 
# line=x,y,z to give us the place of the cube on a map 

datas=set()
min_coord=1<<60
max_coord=-(1<<60)
# going through the boxes
for line in lines : 
    x, y, z = map(int, line.split(","))
    datas.add((x, y, z))

    for num in [x,y,z] : 
        max_coord=max(max_coord,num)
        min_coord=min(min_coord,x,y,z)

print("datas : \n",datas,"\n")
print("min_coord : ",min_coord)
print("max_coord : ",max_coord)
print("\n")

# function to see is a block is exposed to the outside of the structure or not 
# doing this with a DFS algorithm 
def exposed(pos) : 
    stack=[pos]
    seen=set()

    # if the box is in the structure, we return False, since we want air and not the box
    if pos in datas : 
        return False
    
    while len(stack) > 0 : 
        pop=stack.pop()

        # if the bow is in the structure, we continue, since we want air and not the box
        if pop in datas :
            continue

        # stopping the DFS if the box is outside the structure
        # we don't have anything to do in that case 
        for coord in range(3) : 
            if not (min_coord <= pop[coord] <= max_coord) : 
                return True 
            
        # checking if we've already seen this box, skipping it if we did
        if pop in seen : 
            continue
        # adding the box to the seen set if we don't skip it
        seen.add(pop)

        # going through the 6 boxes around the current one
        for coord in range(3) : 
            dpos=np.array([0,0,0])
            dpos[coord]=1

            dneg=np.array([0,0,0])
            dneg[coord]=-1

            # adding the boxes to the stack, since it's the neighbors of the current box
            # to go one step deeper in the DFS algorithm
            stack.append(tuple(pop+dpos))
            stack.append(tuple(pop+dneg))

    return False



answer=0
# going through the boxes 
for x,y,z in datas :
    covered=0

    pos=np.array((x,y,z))

    for coord in range(3) : 
        # dpos is the direction of the positive axis 
        # dneg is the direction of the negative axis
        # for each direction : x,y,z 

        dpos=np.array([0,0,0])
        dpos[coord]=1

        dneg=np.array([0,0,0])
        dneg[coord]=-1

        # looking 
        for nbr in [tuple(pos + dpos), tuple(pos + dneg)]:
            # if he can't see outside the box, we add it to the covered boxes
            # exposed(nbr) returns 1 if the box is not in datas, 0 otherwise, since it's a True/False
            answer += exposed(nbr)

print("answer : ",answer)

# I found 58 for the test.txt file as expected