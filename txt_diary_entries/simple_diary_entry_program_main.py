import os
from simple_diary_entry_program_functions import DiaryDesigns

base_dir = os.path.dirname(__file__)
design = DiaryDesigns()

entry_number = 0
with open(os.path.join(base_dir, "my_life.txt"), "a") as diary_entry:
    while True:
        print(design.entry_start())
        entry_number += 1
        print(design.entry_number(entry_number))

        text_line = input("Text to Input: ")
        diary_entry.write(f"{text_line}\n")

        choice = input("Are There More(Y/N)?: ").upper()
        if choice != "Y":
            with open(os.path.join(base_dir, "my_life.txt"), "a") as diary_counter:
                diary_counter.write(f"Total Entries: {entry_number}\n")
            print(design.separator("*"))
            print(design.closing())
            break