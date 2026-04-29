import random

with (open("./integers.txt","w")) as numbers:    
    for line in range(20):
        numbers.write(f"{random.randint(1,100)}\n")

with (open("./numbers.txt","r")) as nums_infile:
    numbers_list = [int(line.strip()) for line in nums_infile]

with (open("./double.txt","w")) as squares:
    for nums in numbers_list:
        squared = nums ** 2
        squares.write(f"Base:{nums} = Squared: {squared}\n")