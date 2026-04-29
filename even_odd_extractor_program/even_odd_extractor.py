import random

with (open("./numbers.txt","w")) as numbers:    
    for line in range(20):
        numbers.write(f"{random.randint(1,100)}\n")    

with (open("./numbers.txt","r")) as nums_infile:
    numbers_list = [int(line.strip()) for line in nums_infile]


with (open("./even.txt")) as even_numbers:
    for line in even_numbers:
        data = even_numbers.readlines(20)
        if data % 2 == 0:
            