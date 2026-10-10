str1 = "I LOVE YOU"
list = str1.split()
largest = list[1]
for word in list:
    if word.len() > largest.len() :
        largest = word

print("largest is : ",largest)