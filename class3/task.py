# print number from 1 to 100
# for every 3rd number add foo
# for every 5th number add bar
# for every 10th number add buzz

for i in range(101):   # i=1, i=2, i=3
    output = str(i)    # output="1", output="2", output="3"
    if i % 3 == 0:
        output += " foo"
    if i % 5 == 0:
        output += " bar"
    if i % 10 == 0:
        output += " buzz"
    print(output)
