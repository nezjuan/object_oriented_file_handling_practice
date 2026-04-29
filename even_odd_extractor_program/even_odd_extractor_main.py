from even_odd_extractor_functions import NumberFileGenerator, EvenOddExtractor

num_txt_file = NumberFileGenerator()
num_txt_file.number_generator()

with (open("./numbers.txt","r")) as nums_infile:
    numbers_list = [int(line.strip()) for line in nums_infile]

even_odd_extractor = EvenOddExtractor()
even_odd_extractor.even_extractor(numbers_list)
even_odd_extractor.odd_extractor(numbers_list)

print("=============================================================================\n"
      "[FINISHED OBJECTIVE]: even.txt and odd.txt created/extracted from numbers.txt\n"
      "=============================================================================\n")