# opening the file 
with open("input14.txt","r") as file : 
    input=file.read().strip().split("\n")

# Where is the sand_source 
sand_source=500, 0

# we create a set to store the filled coordinates
# we first fill it with the rocks 
# then with the sand blocks 
filled=set()
# set used to be sure that we don't fill the same coordinates twice and don't have to do another function to check if the coordinates are already filled

# getting the input data, as we want it 
for line in input : 
    coords=[]
    # we split the coordinates to get the different points where the rocks changes of directions
    for coord in line.split(" -> ") : 
        x,y=map(int, coord.split(","))
        coords.append((x,y))

    # going trough the different directions of the rocks lines 
    for i in range(1,len(coords)) : 
        # we get the first and the last point of the direction we got in 
        x1,y1=coords[i-1]
        x2,y2=coords[i]
        # we fill the coordinates between the two points

        # if this is an horizontal line
        if x1 != x2 : 
            assert y1==y2
            for x in range(min(x1,x2),max(x1,x2)+1) : 
                filled.add((x,y1))

        # if this is a vertical line
        if y1 != y2 : 
            assert x1==x2
            for y in range(min(y1,y2),max(y1,y2)+1) : 
                filled.add((x1,y))
    

# getting the max height so we know the depth from which we need to stop 
# it's the max y of the filled coordinates + 2 due to the input rules, but +1 in reality since the second one is filled by rocks in theory  
max_y=max(y for x,y in filled)+1

# we create a function to place one block of sand with the rules we have
# he will go to the bottom 
def generate_sand() : 
    global filled
    # we start from the sand_source
    x,y=sand_source

    # if the sand_source is already filled, we return it
    if (x,y) in filled :
        return (x,y)

    # while we can go down starting from the sand_source
    while y<max_y : 
        # check if the block we can go down 
        if (x,y+1) not in filled : 
            y+=1
            continue

        # if we can't go down, we check if we can go down and left 
        if (x-1,y+1) not in filled :
            x-=1
            y+=1
            continue

        # if we can't go down and left, we check if we can go down and right
        if (x+1,y+1) not in filled : 
            x+=1
            y+=1
            continue
            
        # if everything is filled after this step, we stop
        break
    
    return (x,y)

# we fill the sand 
# we stop when we can't fill anymore sand to place

# we count the number of sand blocks we've been able to place
sum=0
while True : 
    # getting the coords of the point we need to place
    (x,y) = generate_sand()
    filled.add((x,y))
    # if we've been able to place it, we add 1 to the sum
    sum+=1

    # stopping condition
    # we are at the sand_source
    if (x,y)==sand_source : 
        break


# we print the sum of the sand blocks we've been able to place
print("\nsum of the sand blocks we've been able to place : ",sum,"\n")

# we find 93 sand blocks as expected with test.txt