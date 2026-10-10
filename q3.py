def odd_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
num = int(input("Enter a number : "))
if odd_even(num):
    print(f"{num} is even")
else:
    print(f"{num} is odd")