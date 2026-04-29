import os
from squares_and_cubes_functions import IntegerFileGenerator, SquaredTxtFile, CubedTxtFile

current_dir = os.path.dirname(__file__)

# generate integers
integer_txt_file = IntegerFileGenerator()
integer_txt_file.integer_generator()

# read integers safely
numbers_file_path = os.path.join(current_dir, "integers.txt")
with open(numbers_file_path, "r") as nums_infile:
    numbers_list = [int(line.strip()) for line in nums_infile if line.strip().isdigit()]

# create squared file
squared_txt_file = SquaredTxtFile()
squared_txt_file.squared_txt_file(numbers_list)

# create cubed file
cubed_txt_file = CubedTxtFile()
cubed_txt_file.cubed_txt_file(numbers_list)

print(f"{'-'*85}\n"
      f"[FINISHED OBJECTIVE]: double.txt and triple.txt created/extracted from integers.txt\n"
      f"{'-'*85}\n")
