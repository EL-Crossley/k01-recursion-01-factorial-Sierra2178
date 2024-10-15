3# Put your function here
def factorial(num):
    if num == 1:
        return 1
    else:
        num = num*factorial(num-1)
        return num

# testing
num = int(input())
print(factorial(num))   