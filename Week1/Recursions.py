# Practice Problem 1
def sum(x):
    if x == 1:
        return 1
    else:
        return x + sum(x - 1)


print(sum(10))


# Practice Problem 2
def fib(x):
    if x == 1:
        return 0
    elif x == 2 or x == 3:
        return 1
    else:
        return fib(x - 2) + fib(x - 1)


x = int(input("Enter an value: "))

if x < 0:
    print("Not possible")
else:
    for i in range(1, x + 1):
        print(fib(i))


# Practice Problem 3
def digits(x):
    if x < 10:
        return 1
    else:
        return 1 + digits(x / 10)


x = int(input("Enter a number: "))

digits(x)


# Practice Problem 4
def func(mylist):
    valuelist = mylist[1:len(mylist)]
    if len(mylist) == 1:
        return mylist[0]
    else:
        return max(mylist[0], func(valuelist))


mylist = [2, 36, 23, 12, 87, 93, 46]

print(func(mylist))
