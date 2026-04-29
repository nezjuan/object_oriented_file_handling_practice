from even_odd_extractor_functions import NumberFileGenerator, EvenOddExtractor
import os

current_dir = os.path.dirname(__file__)

num_txt_file = NumberFileGenerator()
num_txt_file.number_generator()

numbers_file_path = os.path.join(current_dir, "numbers.txt")

with open(numbers_file_path, "r") as nums_infile:
    numbers_list = [int(line.strip()) for line in nums_infile]

even_odd_extractor = EvenOddExtractor()
even_odd_extractor.even_extractor(numbers_list)
even_odd_extractor.odd_extractor(numbers_list)

print(f"{'='*80}\n"
      f" [FINISHED OBJECTIVE]: even.txt and odd.txt created/extracted from numbers.txt\n"
      f"{'='*80}\n")