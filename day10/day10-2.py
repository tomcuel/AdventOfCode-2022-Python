# opening the file 
with open("input10.txt", "r") as file : 
    # splitting the file into lines
    lines=file.read().strip().split("\n")

# printing the lines to see the data
print("data input :\n",lines,"\n")

# number of cycle being done 
cycle=0
# value of the current X
X_current=1
# array of X, representing the table of the value of X for each cycle
X_array=[1]*241

# filling the X_array 

# looping through the lines
for line in lines :
    # checking if this is this first type of command
    if line=="noop" :  
        cycle+=1
        # updating the value of X, because the command is a noop stop the process
        X_array[cycle]=X_current          

    # looking at the second type of command
    else : 
        # splitting the line to separate the command and the value
        line=line.split(" ")
        # looking at the command, if it really is "addx"
        assert line[0]=="addx"
        value=int(line[1])
        
        # we fill the cycle+1 
        X_array[cycle+1]=X_current
        X_current+=value

        # we fill the cycle+2 and add +2 to the number of cycle since it's a "addx" command
        cycle+=2
        X_array[cycle]=X_current

# just to see if it does correponds to the online website submission
print("X_array :\n",X_array,"\n")

result=[[None]*40 for _ in range(6)]
for row in range (len(result)) : 
    for col in range (len(result[0])) : 
        # getting the number of cycle, the place in X_array
        cycle_result=row*40+col+1
        # condition to know whether result[row][col] is a "." (making it " " to have something more visual) or a "#"
        # because a cycle make us draw 2 symbols each time, because they are done by two most of the time until we find a noop that will make nothin special 
        # current_X correspond to the current sprite 
        # overlapping means this formula is true 
        # we're looking at the old value of X at this cycle time, not the one incremented after the instruction
        if  abs(X_array[cycle_result-1]-col) <= 1 :
            result[row][col]="#"
        else :
            result[row][col]=" "

# printing the result  
for row in result : 
    print("".join(row))

# we find the same result as the online website submission for test2.txt