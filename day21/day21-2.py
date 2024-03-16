from sympy import symbols, solve_linear
from sympy.parsing.sympy_parser import parse_expr

#opening the file 
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

humn=symbols("humn")


# priting the data to ckheck if it's correct
print(datas)

# making a recursive function to go trough the nodes
def calculate(name : str) :
    # if name = humain, we can return the value
    if name == "humn" : 
        return humn

    # if the value is an integer, we can return it, because it's already been calculated
    if isinstance(datas[name],int) : 
        return datas[name]
    
    parts=datas[name]
    left=calculate(parts[0])
    right=calculate(parts[2])

    # depending on the operator, we do the operation
    return parse_expr(f"({left}){parts[1]}({right})")

left=calculate(datas["root"][0])
right=calculate(datas["root"][2])

answer=solve_linear(left-right)[1]
print("\nThe answer is : ",answer,"\n")

# we found 301 as expected with test.txt

# I didn't found it myself this one but I found it interesting to share
# it was good to see that sympy can be used to solve this kind of problem
# what we can do with expressions, how to solve this puzzle 