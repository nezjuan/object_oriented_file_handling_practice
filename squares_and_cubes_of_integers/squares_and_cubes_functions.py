import random
import os

base_dir = os.path.dirname(__file__)

class IntegerFileGenerator:
    def integer_generator(self):
        with open(os.path.join(base_dir, "integers.txt"), "w") as numbers:  
            numbers.write("== GENERATED INTEGERS ==\n")
            for line in range(20):
                numbers.write(f"{random.randint(1,100)}\n")
            numbers.write("========== End =========\n")