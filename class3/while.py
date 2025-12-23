# 0 1 1 2 3 5 8 13 21 34 55 89 144
# first = 0, second = 1, next = first + second = 0+1=1
# first = 1, second = 1, next = first + second = 1+1=2
# first = 1, second = 2, next = 3
# first = 2, second = 3, next = 5


limit = int(input("Enter the limit: "))

first = 0
second = 1
print(first)
print(second)

next = first + second

while next < limit:
    print(next)
    first = second
    second = next
    next = first + second
    