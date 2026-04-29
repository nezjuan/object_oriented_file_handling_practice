import random
import os

base_dir = os.path.dirname(__file__)

class NumberFileGenerator:
    def number_generator(self):
        with open(os.path.join(base_dir, "numbers.txt"), "w") as numbers:  
            numbers.write("== GENERATED NUMBERS ==\n")
            for line in range(20):
                numbers.write(f"{random.randint(1,100)}\n")
            numbers.write("========End=======\n")

class EvenOddExtractor:
    def even_extractor(self, numbers_list):
        with open(os.path.join(base_dir, "even.txt"), "w") as even_numbers:
            even_numbers.write("== EVEN NUMBERS ==\n")
            for nums in numbers_list:
                if nums % 2 == 0:
                    even_numbers.write(str(nums) + "\n")
            even_numbers.write("========End=======\n")

    def odd_extractor(self, numbers_list):
        with open(os.path.join(base_dir, "odd.txt"), "w") as odd_numbers:
            odd_numbers.write("== ODD NUMBERS ==\n")
            for nums in numbers_list:
                if nums % 2 != 0:
                    odd_numbers.write(str(nums) + "\n")
            odd_numbers.write("========End=======\n")   