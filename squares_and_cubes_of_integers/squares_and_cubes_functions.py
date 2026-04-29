import random
import os

base_dir = os.path.dirname(__file__)

class IntegerFileGenerator:
    def integer_generator(self):
        with open(os.path.join(base_dir, "integers.txt"), "w") as numbers:  
            numbers.write("** GENERATED INTEGERS **\n")
            for line in range(20):
                numbers.write(f"{random.randint(1,100)}\n")
            numbers.write("********** End *********\n")

class SquaredTxtFile:
    def squared_txt_file(self, numbers_list):
        with open(os.path.join(base_dir, "double.txt"), "w") as squares:
            for nums in numbers_list:
                squared = nums ** 2
                squares.write(f"Base:{nums} - Squared:{squared}\n")

class CubedTxtFile:
    def cubed_txt_file(self, numbers_list):
        with open(os.path.join(base_dir, "triple.txt"), "w") as cubes:
            for nums in numbers_list:
                cubed = nums ** 3
                cubes.write(f"Base:{nums} - Cubed:{cubed}\n")