#opening the file and splitting for each monkey : 
with open("input11.txt", "r") as file:
    input = file.read().strip().split("\n\n")

# doing the data :
# we have at data[i]: 
# 1. number of the monkey : i 
# 2. items_worry
# 3. operation we does on the items_worry he has : symbol + number 
# 4. test made : divisible by something : number 
# 5. the result of the test : number to which we add the items_worry
datas=[[] for _ in range(len(input))]

# getting the differents things of the input for each monkey and putting them in the data list 
for instruction in input : 
    # spliting the instruction
    instruction = instruction.split("\n")
    
    monkey = int(instruction[0].split(" ")[1][:-1])
    
    items_worry = instruction[1].split(":")[1].strip().split(", ")
    items_worry=[int(x) for x in items_worry]

    operation = instruction[2].split("old ")[1].strip().split(" ")

    test = int(instruction[3].split(" ")[-1]) 
    true_result = int(instruction[4].split(" ")[-1])
    false_result = int(instruction[5].split(" ")[-1])

    print("number of monkey : ", monkey)
    print("items_worry : ", items_worry)
    print("operation : ", operation)
    print("test : ", test)
    print("true result : ", true_result)
    print("false result : ", false_result)
    print("\n")

    datas[monkey]=[items_worry, operation, test, true_result, false_result]

# checking that we have the right data :
print("our data input :\n")
for monkey in datas :
    print(monkey)
print("\n")

# needed because of the time it takes to do the 1000 rounds
modulo=1
for monkey in datas : 
    modulo *= monkey[2]

print("modulo : ", modulo)

# making a function that does the operatuon on the items_worry given the form of the operation in data
def operation_expression(operation : list, x : int) : 
    if operation[0] == "+" : 
        ans = x + int(operation[1])
    
    elif operation[0] == "*" : 
        # disjonction depending on what the things the operation is about 
        if operation[1] == "old" : 
            ans = x*x
        else : 
            ans = x*int(operation[1])
        
    return ans % modulo

# number of monkey :
N=len(datas)

# list of the number of items that have been inspected by each monkey
inspected_items=[0 for _ in range(N)]

# making the 1000 round happening : 
for i in range (10000) :
    for monkey in datas : 
        # getting the data for the monkey
        items_worry = monkey[0]
        operation = monkey[1]
        test = monkey[2]
        true_result = monkey[3]
        false_result = monkey[4]

        #adding the number of items that have been inspected by the monkey to inspected_items
        index_monkey = datas.index(monkey)
        inspected_items[index_monkey]+=len(items_worry)
        # here, we don't care if it has already been inspected by the monkey, 
        # himself doesn't care 

        # doing the operation on the items_worry
        items_worry = [operation_expression(operation, x) for x in items_worry]

        # going through the items_worry to see to which monkey they go
        for x in items_worry : 
            # if the item is divisible by the test
            if x%test == 0 : 
                # adding the true_result to the monkey that corresponds
                datas[true_result][0].append(x)
            else : 
                # adding the false_result to the monkey that corresponds
                datas[false_result][0].append(x)

        # clearing the items that have been inspected by the monkey
        monkey[0]=[]


print("items that monkeys are holding after 20 rounds :")
for monkey in datas : 
    print(monkey[0])

print("inspected_items : ", inspected_items,"\n")

# getting the two monkeys that have inspected the most items, that are the most active 
sorted_inspected_items=sorted(inspected_items)
print("result : ", sorted_inspected_items[-1]*sorted_inspected_items[-2],"\n")

# we found 2713310158 as expected with test.txt