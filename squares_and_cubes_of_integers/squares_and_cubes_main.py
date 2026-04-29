from squares_and_cubes_functions import IntegerFileGenerator
import os

current_dir = os.path.dirname(__file__)

integer_txt_file = IntegerFileGenerator()
integer_txt_file.integer_generator()

with (open("./double.txt","w")) as squares:
    for nums in numbers_list:
        squared = nums ** 2
        squares.write(f"Base:{nums} = Squared: {squared}\n")

with (open("./triple.txt","w")) as cubes:
    for nums in numbers_list:
        cubed = nums ** 3
        cubes.write(f"Base:{nums} = Cubed: {cubed}\n")