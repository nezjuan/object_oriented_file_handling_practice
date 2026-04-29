import random

with (open("./integers.txt","w")) as numbers:    
    for line in range(20):
        numbers.write(f"{random.randint(1,100)}\n")

with (open("./double.txt","w")) as squares:
    for nums in squares:
        squared = nums ** 2
        squared.write(str(nums) + "\n")