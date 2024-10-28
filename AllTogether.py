### Part Four -- your code goes here. 
import random
list = [random.randint(1,100) for I in range(10)]
print(list)

index = 0 
while index < len(list):
    if list[index] % 2 == 0:
        list.pop(index)
    else:
        index = index + 1

print("odd numbers are",list)



