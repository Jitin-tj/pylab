str1 = input("enter string 1 : ")
str2 = input("enter string 2 : ")

def check(str1, str2):
    list = []
    list2 = []
    for ch in str1:
        list += ch.lower()
    for ch2 in str2:
        list2 += ch2.lower()
    list.sort()
    list2.sort()
    if list == list2:
        print("is anagram")
    else:
        print("is not anagram")


check(str1, str2)
