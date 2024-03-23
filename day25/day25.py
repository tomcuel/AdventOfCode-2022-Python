# opening the file 
with open("input25.txt","r") as file : 
    lines=file.read().strip().split("\n")


# String to digit with a dictionary
string_to_digit = {"0": 0, "1": 1, "2": 2, "-": -1,  "=": -2}
print(string_to_digit)

# Digit to string with a dictionary
digit_to_string = {d: s for s,d in string_to_digit.items()}
print(digit_to_string)


# converting from snafu to decimal
answer=0
# for each line in the file
for line in lines:
    # temp variable to store the answer
    temp=0
    # p variable to store the power of 5
    p=1
    # reversing the line
    line=line[::-1]
    # for each character in the line
    # going from the last character to the first, the lowest power of 5 to the highest
    for i in range (len(line)):
        temp+=string_to_digit[line[i]]*p
        p*=5
    answer+=temp


# converting the answer from decimal to snafu 
result=""
while answer > 0:
    # out dictionnary values are -2, -1, 0, 1, 2
    # it's the formula when you're in base 5 and want this dictionary
    index=((answer+2)%5)-2
    # adding the character to the result
    result+=digit_to_string[index]
    # going a power of 5 lower
    answer=answer-index
    answer//=5

print("\nThe result is :",result[::-1]," in snafu notation\n")


# we found 2=-1=0 as expected for test.txt