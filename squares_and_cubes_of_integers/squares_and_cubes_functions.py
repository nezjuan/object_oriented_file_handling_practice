import random
import os

base_dir = os.path.dirname(__file__)

class IntegerFileGenerator:
    def integer_generator(self):
        with open(os.path.join(base_dir, "integers.txt"), "w") as numbers:
            numbers.write("=== GENERATED INTEGERS ===\n")
            for line in range(20):
                numbers.write(f"{random.randint(1,100)}\n")
            numbers.write("========= End ========\n")

class SquaredTxtFile:
    def squared_txt_file(self, numbers_list):
        with open(os.path.join(base_dir, "double.txt"), "w") as double_file:
            double_file.write("=== SQUARED INTEGERS ===\n")
            for num in numbers_list:
                double_file.write(f"Base: {num}, Square: {num**2}\n")
            double_file.write("========= End ========\n")

class CubedTxtFile:
    def cubed_txt_file(self, numbers_list):
        with open(os.path.join(base_dir, "triple.txt"), "w") as triple_file:
            triple_file.write("=== CUBED INTEGERS ===\n")
            for num in numbers_list:
                triple_file.write(f"Base: {num}, Cube: {num**3}\n")
            triple_file.write("========= End ========\n")