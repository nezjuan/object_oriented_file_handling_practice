import random
import os

base_dir = os.path.dirname(__file__)

class NumberFileGenerator:
    def number_generator(self):
        with open(os.path.join(base_dir, "numbers.txt"), "w") as numbers:  
            for line in range(20):
                numbers.write(f"{random.randint(1,100)}\n")

class EvenOddExtractor:
    def even_extractor(self, numbers_list):
        with open(os.path.join(base_dir, "even.txt"), "w") as even_numbers:
            for nums in numbers_list:
                if nums % 2 == 0:
                    even_numbers.write(str(nums) + "\n")

    def odd_extractor(self, numbers_list):
        with open(os.path.join(base_dir, "odd.txt"), "w") as odd_numbers:
            for nums in numbers_list:
                if nums % 2 != 0:
                    odd_numbers.write(str(nums) + "\n")