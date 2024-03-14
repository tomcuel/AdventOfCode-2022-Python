# kind of tetris with some strange rules 

#opening the file 
with open("test.txt","r") as file :
    line=file.read().strip()

# printing the line
print("\nline input :",line)
print("len(line) :",len(line),"\n")


# just to print the map when we need it 
# function to print the map, it's a void one 
def print_map(map):
    mapped=[[0]*7 for i in range(len(map))]
    for i in range(len(map)):
        for j in range(7):
            if map[i][j] == 1 :
                mapped[i][j]="#"
            elif map[i][j] == 0 :
                mapped[i][j]="."
            elif map[i][j] == 2 :
                mapped[i][j]="@"

    for line in mapped : 
        result = "|" + "".join(str(num) for num in line) + "|"
        print(result)  # Output: |001234|
    print("÷-------÷")
    print("\n")


# function that is placing the rock on top of the map entry 
# a case taken by a rock entry is a 2
# does a new map with the rock placed a the beginning of the map + 3 empty lines
def place_the_entry(map, rocks_type: str) :
    # maps need to be 10 lines at the moment 

    # for each rock : 
    # place the rock
    # get the height of the rock to know the height of the new_map
    # created a new map 
    # make the 3 steps bewteen the lower of this rock and the higher of the previous rock placement 
    # copie the 10 last lines of the map in the new map on its 10 last lines


    if rocks_type == "-":
        height_of_the_rock=1
        map_changed=[[0]*7 for i in range(height_of_the_rock+3)]
        map_changed[0][2]=2
        map_changed[0][3]=2
        map_changed[0][4]=2
        map_changed[0][5]=2

    elif rocks_type == "+":
        height_of_the_rock=3
        map_changed=[[0]*7 for i in range(height_of_the_rock+3)]
        map_changed[0][3]=2
        map_changed[1][2]=2
        map_changed[1][3]=2
        map_changed[1][4]=2
        map_changed[2][3]=2
    
    elif rocks_type == "j":
        height_of_the_rock=3
        map_changed=[[0]*7 for i in range(height_of_the_rock+3)]
        map_changed[0][4]=2
        map_changed[1][4]=2
        map_changed[2][4]=2
        map_changed[2][3]=2
        map_changed[2][2]=2
    
    elif rocks_type == "|":
        height_of_the_rock=4
        map_changed=[[0]*7 for i in range(height_of_the_rock+3)]
        map_changed[0][2]=2
        map_changed[1][2]=2
        map_changed[2][2]=2
        map_changed[3][2]=2

    elif rocks_type == "@":
        height_of_the_rock=2
        map_changed=[[0]*7 for i in range(height_of_the_rock+3)]
        map_changed[0][2]=2
        map_changed[0][3]=2
        map_changed[1][2]=2
        map_changed[1][3]=2
        

    return map_changed

# round == 39 for test.txt
# round == 10091 for input17.txt
# function to get the next instruction from the command line
# return a number that is linked to the next instruction and the next round also 
def get_next_instruction(line, round):
    # if we've gone trough the line, we need to run it again from the beginning
    if round == len(line) :
        round = 0
    return line[round]


# function to get the position of the different points of the rock
# gets it line by line 
# so we can deduct the type of rock we are dealing with by looking at the position of the points
# return the position of the points of the rock in a list of points
def get_position_of_the_rock(map,rock_type : str) :
    positions=[]
    for i in range(len(map)):
        for j in range(7):
            if map[i][j] == 2 :
                positions.append([i,j])
    return positions


# function to say if we can move the rock to the right
# function to say if we can move the rock to the left
def can_move_right(map, direction : str, current_figure : str) :
    can_move=True 
    # to get the position of the rock, where are the points of the rock
    positions=get_position_of_the_rock(map,current_figure)

    if current_figure == "-" : 
        # if the one on the left is blocked by a 1 
        if map[positions[3][0]][positions[3][1]+1] == 1 :
            can_move=False

    if current_figure == "+" :
        # if the top one is blocked 
        if map[positions[0][0]][positions[0][1]+1] == 1 :
            can_move=False
        # if the left  one is blocked 
        if map[positions[3][0]][positions[3][1]+1] == 1 :
            can_move=False
        # if the bottom one is blocked
        if map[positions[4][0]][positions[4][1]+1] == 1 :
            can_move=False

    if current_figure == "j" :
        # if the two top one is blocked 
        if map[positions[0][0]][positions[0][1]+1] == 1 or map[positions[1][0]][positions[1][1]+1] == 1:
            can_move=False
        # if the bottom one, on the left is blocked
        if map[positions[4][0]][positions[4][1]+1] == 1 :
            can_move=False

    if current_figure == "|" :
        for point in positions:
            if map[point[0]][point[1]+1] == 1 :
                can_move=False

    if current_figure == "@" :
        # searching the two point of the left of the cube
        if map[positions[1][0]][positions[1][1]+1] == 1 or map[positions[3][0]][positions[3][1]+1] == 1 :
            can_move=False


    return can_move


# function to say if we can move the rock to the left
def can_move_left(map, direction : str, current_figure : str) :
    can_move=True 
    # to get the position of the rock, where are the points of the rock
    positions=get_position_of_the_rock(map,current_figure)

    if current_figure == "-" : 
        # if the one on the left is blocked by a 1 
        if map[positions[0][0]][positions[0][1]-1] == 1 :
            can_move=False

    if current_figure == "+" :
        # if the top one is blocked 
        if map[positions[0][0]][positions[0][1]-1] == 1 :
            can_move=False
        # if the left  one is blocked 
        if map[positions[1][0]][positions[1][1]-1] == 1 :
            can_move=False
        # if the bottom one is blocked
        if map[positions[4][0]][positions[4][1]-1] == 1 :
            can_move=False

    if current_figure == "j" :
        # if the two top one is blocked 
        if map[positions[0][0]][positions[0][1]-1] == 1 or map[positions[1][0]][positions[1][1]-1] == 1:
            can_move=False
        # if the bottom one, on the left is blocked
        if map[positions[2][0]][positions[2][1]-1] == 1 :
            can_move=False

    if current_figure == "|" :
        for point in positions:
            if map[point[0]][point[1]-1] == 1 :
                can_move=False

    if current_figure == "@" :
        # searching the two point of the left of the cube
        if map[positions[0][0]][positions[0][1]-1] == 1 or map[positions[2][0]][positions[2][1]-1] == 1 :
            can_move=False


    return can_move


# function to move the rock to the left or to the right one tile and not if it's not possible
# return the map with the rock moved to the left or to the right if it's possible and unchanged if it's not
def move_side(map, direction : str, current_figure : str) : 
    # to get the position of the rock, where are the points of the rock
    positions=get_position_of_the_rock(map,current_figure)
    
    # deciding wether we can move the rock or not to the right 
    # searching if a rock is against the right wall
    fully_on_the_right = False
    for i in range(len(map)):
        if map[i][6] ==2 :
            fully_on_the_right = True
    # if not, we can move the rock to the right
    if direction == ">" and not fully_on_the_right and can_move_right(map, direction, current_figure) : 

        if current_figure == "-" : 
            # sliding the 4 tiles to the right by just adding the last one and suppressing the first one
            map[positions[0][0]][positions[0][1]]=0
            map[positions[3][0]][positions[3][1]+1]=2

        if current_figure == "+" : 
            # the top head one tile to the right and we suppress the previous top head
            map[positions[0][0]][positions[0][1]+1]=2
            map[positions[0][0]][positions[0][1]]=0
            
            # sliding the 3 middle one to the right by just adding the last one and suppressing the first one
            map[positions[1][0]][positions[1][1]]=0
            map[positions[3][0]][positions[3][1]+1]=2

            # the bottom head one tile to the right and we suppress the previous bottom head
            map[positions[4][0]][positions[4][1]+1]=2
            map[positions[4][0]][positions[4][1]]=0

        if current_figure == "j" : 
            # for the 2 tiles above, we just suppress the first one and add the second one to the right
            map[positions[0][0]][positions[0][1]]=0
            map[positions[1][0]][positions[1][1]]=0
            map[positions[0][0]][positions[0][1]+1]=2
            map[positions[1][0]][positions[1][1]+1]=2

            # for the 3 tiles below, we just suppress the first one and add the last one to the right
            map[positions[2][0]][positions[2][1]]=0
            map[positions[4][0]][positions[4][1]+1]=2

        if current_figure == "|" :
            # sliding the 4 tiles to the right by just suppressing each one and adding it to the right
            for point in positions:
                map[point[0]][point[1]]=0
                map[point[0]][point[1]+1]=2

        if current_figure == "@" :
            # sliding the cube to the right by just adding the last one and suppressing the first one for each line 
            map[positions[0][0]][positions[0][1]]=0
            map[positions[2][0]][positions[2][1]]=0

            map[positions[1][0]][positions[1][1]+1]=2
            map[positions[3][0]][positions[3][1]+1]=2


    # deciding wether we can move the rock or not to the left 
    # searching if a rock is against the left wall
    fully_on_the_left = False
    for i in range(len(map)):
        if map[i][0] ==2 :
            fully_on_the_left = True 
    # if not, we can move the rock to the left
    if direction == "<" and not fully_on_the_left and can_move_left(map, direction, current_figure) : 

        if current_figure == "-" : 
            # sliding the 4 tiles to the left by just adding the last one and suppressing the first one
            map[positions[3][0]][positions[3][1]]=0
            map[positions[0][0]][positions[0][1]-1]=2

        if current_figure == "+" : 
            # the top head one tile to the left and we suppress the previous top head
            map[positions[0][0]][positions[0][1]-1]=2
            map[positions[0][0]][positions[0][1]]=0
            
            # sliding the 3 middle one to the left by just adding the last one and suppressing the first one
            map[positions[3][0]][positions[3][1]]=0
            map[positions[1][0]][positions[1][1]-1]=2

            # the bottom head one tile to the left and we suppress the previous bottom head
            map[positions[4][0]][positions[4][1]-1]=2
            map[positions[4][0]][positions[4][1]]=0

        if current_figure == "j" : 
            # for the 2 tiles above, we just suppress the first one and add the second one to the left
            map[positions[0][0]][positions[0][1]]=0
            map[positions[1][0]][positions[1][1]]=0
            map[positions[0][0]][positions[0][1]-1]=2
            map[positions[1][0]][positions[1][1]-1]=2

            # for the 3 tiles below, we just suppress the first one and add the last one to the left
            map[positions[4][0]][positions[4][1]]=0
            map[positions[2][0]][positions[2][1]-1]=2

        if current_figure == "|" :
            # sliding the 4 tiles to the left by just suppressing each one and adding it to the left
            for point in positions:
                map[point[0]][point[1]]=0
                map[point[0]][point[1]-1]=2

        if current_figure == "@" :
            # sliding the cube to the left by just adding the last one and suppressing the first one for each line 
            map[positions[1][0]][positions[0][1]]=0
            map[positions[3][0]][positions[3][1]]=0

            map[positions[0][0]][positions[0][1]-1]=2
            map[positions[2][0]][positions[2][1]-1]=2


    return map


# function to say if we can move down or if the rock 2 become a 1
# return True if we can move down and False if we can't
def is_able_to_move_down(map, current_figure : str) :
    # to get the position of the rock, where are the points of the rock
    positions=get_position_of_the_rock(map,current_figure)
    is_moving_down = True
    # deciding wether we can move the rock one tile down or not
    for point in positions:
        if map[point[0]+1][point[1]] == 1 : 
            is_moving_down = False
    return is_moving_down


# function to move the rock down one tile and not if it's not possible
# return the map with the rock moved down if it's possible and unchanged if it's not
def move_down(map, current_figure : str) :
    # to get the position of the rock, where are the points of the rock
    positions=get_position_of_the_rock(map,current_figure)

    # if we can move the rock down
    if is_able_to_move_down(map, current_figure) :
        if current_figure == "-" : 
            # sliding the 4 tiles down by just supressing each one and adding it one tile below
            for point in positions:
                map[point[0]][point[1]]=0
                map[point[0]+1][point[1]]=2

        if current_figure == "+" : 
            # the right one is sliding down by just adding the last one and suppressing the first one
            map[positions[3][0]+1][positions[3][1]]=2
            map[positions[3][0]][positions[3][1]]=0
            
            # sliding the 3 middle one down by just adding the last one and suppressing the first one
            map[positions[4][0]+1][positions[4][1]]=2
            map[positions[0][0]][positions[0][1]]=0

            # the left one is sliding down by just adding the last one and suppressing the first one
            map[positions[1][0]+1][positions[1][1]]=2
            map[positions[1][0]][positions[1][1]]=0

        if current_figure == "j" : 
            # for the 2 tiles above, we just suppress the first one and add the second one to the right
            map[positions[2][0]][positions[2][1]]=0
            map[positions[3][0]][positions[3][1]]=0
            map[positions[2][0]+1][positions[2][1]]=2
            map[positions[3][0]+1][positions[3][1]]=2

            # for the 3 tiles below, we just suppress the first one and add the last one to the right
            map[positions[0][0]][positions[0][1]]=0
            map[positions[4][0]+1][positions[4][1]]=2

        if current_figure == "|" :
            # sliding the 4 tiles down by just supressing the top one and adding one the lowest one
            map[positions[0][0]][positions[0][1]]=0
            map[positions[3][0]+1][positions[3][1]]=2

        if current_figure == "@" :
            # sliding the cube down by just adding the last one and suppressing the first one for each column 
            map[positions[0][0]][positions[0][1]]=0
            map[positions[2][0]+1][positions[2][1]]=2

            map[positions[1][0]][positions[1][1]]=0
            map[positions[3][0]+1][positions[3][1]]=2

    return map


# function to place the rock on the map, as fixed
def place_the_rock(map):
    for i in range(len(map)):
        for j in range(7):
            if map[i][j] == 2 :
                map[i][j]=1
    return map


# function to copy the map
def copy_map(map):
    mapped=[[0]*7 for i in range(len(map))]
    for i in range(len(map)):
        for j in range(7):
            mapped[i][j]=map[i][j]
    return mapped


# function to clean the 0 lines of the map
def clean_map(map):
    map_cleaned=[]
    for i in range(len(map)):
        if 1 in map[i]:
            map_cleaned.append(map[i])
    return map_cleaned


# making a 15 blocks deepth map 
map=[[0]*7 for i in range(5)]
# to make the ground, in order for the rock to not fall, to stop falling 
map[0]=[0,0,2,2,2,2,0]
map[4]=[1,1,1,1,1,1,1]
# rock entry = 2
# rock placed = 1
# free block = 0
# we need 3 lines that are empty between the tail of the rock we put and the head of the higher rock we've put before 


# types of rocks : 

# - for ####

# + for  #
#       ###
#        #

# j for   #
#         #
#       ###

# | for #
#       #
#       #
#       #

# @ for ##
#       ##

rock_shapes = ["-","+","j","|","@"]
print("rock_shapes",rock_shapes,"\n")

# number_of rounds to do : 2022 but not 2023 
number_of_rounds=2022
# number of rocks have fallen
number_rock=0
# lap the round 2022 times to get the final map height 




####################
# Turn 1
####################

rock_to_place=rock_shapes[number_rock%5]
# print("rock_to_place",rock_to_place)

# print_map(map)


round=0
directory=line[round]
round+=1
# print("round : ",round-1)
# print("directory : ",directory) 

map=move_side(map,directory,rock_to_place)
# print_map(map)
is_moving_down = is_able_to_move_down(map,rock_to_place)
if is_moving_down :
    map=move_down(map,rock_to_place)
# print_map(map)

is_moving_down = is_able_to_move_down(map,rock_to_place)
while is_moving_down: 
    # print("round : ",round, (round%len(line)))
    directory=get_next_instruction(line,round)
    # print("directory : ",directory) 
    round+=1
    map=move_side(map,directory,rock_to_place)
    # print_map(map)
    is_moving_down = is_able_to_move_down(map,rock_to_place)
    if is_moving_down :
        map=move_down(map,rock_to_place)
    # print_map(map)

place_the_rock(map)
# print_map(map)

map=clean_map(map)
# print_map(map)

number_rock+=1


####################
# Turn x
####################

for number_of_rock in range(1,number_of_rounds):
    rock_to_place=rock_shapes[number_of_rock%5]
    # print("rock_to_place",rock_to_place)

    mapped=place_the_entry(map,rock_to_place)
    # print_map(mapped)
        
    map=mapped+map
    # print_map(map)

    is_moving_down = is_able_to_move_down(map,rock_to_place)
    while is_moving_down: 
        #print("round : ",round)
        directory=get_next_instruction(line,round)
        #print("directory : ",directory) 
        if round == 39 :
            round = 0
        else : 
            round+=1
        
        map=move_side(map,directory,rock_to_place)
        # print_map(map)
        is_moving_down = is_able_to_move_down(map,rock_to_place)
        if is_moving_down :
            map=move_down(map,rock_to_place)
        # print_map(map)


    place_the_rock(map)
    # print_map(map)

    map=clean_map(map)
    # print_map(map)

print_map(map)

print("résultat : ",len(map)-1)
# we found 3068 as expected for test.txt
# I don't know the result why it doesn't work for input17.txt