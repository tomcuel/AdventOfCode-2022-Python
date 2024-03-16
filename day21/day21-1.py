# opening the file 
with open ("input21.txt","r") as file : 
    lines=file.read().strip().split("\n")

datas={}

# parsing the data
for line in lines:
    line=line.split(" ")
    monkey=line[0][:-1]

    # in that case, we just have one number
    if len(line) ==2 : 
        datas[monkey]=int(line[1])
    else:
        datas[monkey]=line[1:]

# priting the data to ckheck if it's correct
print(datas)

# making a recursive function to go trough the nodes
def calculate(name : str) :
    # if the value is an integer, we can return it, because it's already been calculated
    if isinstance(datas[name],int) : 
        return datas[name]
    
    parts=datas[name]
    left=calculate(parts[0])
    right=calculate(parts[2])

    # depending on the operator, we do the operation
    if parts[1] == "+" : 
        return(left+right)
    
    if parts[1] == "*" :
        return(left*right)
    
    if parts[1] == "/" :
        return(left/right)
    
    if parts[1] == "-" :
        return(left-right)
    
answer=calculate("root")
print("\nThe answer is : ",answer,"\n")

# we found 152 as expected with test.txt