import random

with (open("./numbers.txt","w")) as numbers:  
    for line in range(20):
        numbers.write(f"{random.randint(1,100)}\n")  

with (open("./numbers.txt","r")) as nums_infile:
    numbers_list = [int(line.strip()) for line in nums_infile]

with (open("./even.txt","w")) as even_numbers:
    for nums in numbers_list:
        if nums % 2 == 0:
            even_numbers.write(str(nums) + "\n")

with (open("./odd.txt","w")) as odd_numbers:
    for nums in numbers_list:
        if nums % 2 != 0:
            odd_numbers.write(str(nums) + "\n")

print("=============================================================================\n"
      "[FINISHED OBJECTIVE]: even.txt and odd.txt created/extracted from numbers.txt\n"
      "=============================================================================\n")