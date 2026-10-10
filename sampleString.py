def occurance(str, sub_str):
    pos = []
    index = str.find(sub_str)
    while index != -1:
        pos.append(index)
        index = str.find(sub_str, index + 1)
    return pos if pos else -1
str = input("Enter a strings : ")
sub_str = input("Enter the string for search: ")
res = occurance(str, sub_str)
print("index : ",res)


