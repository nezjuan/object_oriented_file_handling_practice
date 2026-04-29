import os
from simple_diary_entry_program_functions import DiaryDesignsFeatures , EntryAndTitleManager

base_dir = os.path.dirname(__file__)
design = DiaryDesignsFeatures()
file_manager = EntryAndTitleManager(base_dir)
entry_number = file_manager.get_last_entry_number()
file_manager.add_title_if_empty()

with open(file_manager.diary_path, "a") as diary_entry:
    while True:
        print(design.entry_start())
        entry_number += 1
        print(design.entry_number(entry_number))
        diary_entry.write(f">>Entry: {entry_number}\n")

        text_line = input("Text to Input: ")
        diary_entry.write(f">{text_line}\n")

        choice = input("Are There More(Y/N): ").upper()
        if choice != "Y":
            print(design.separator("*"))
            print(design.closing())
            break

with open(file_manager.diary_path, "a") as diary_counter:
    diary_counter.write(f"Total Entries: {entry_number}\n")