import os

class DiaryDesignsFeatures:
    def entry_start(self) -> str:
        return "[ E n t e r i n g   D i a r y   E n t r y . . . ]"

    def entry_number(self, number: int) -> str:
        return f"Entry: {number}"

    def closing(self) -> str:
        return "[ C l o s i n g . . . ]"

    def separator(self, char: str = "-") -> str:
        return char * 40

class EntryAndTitleManager:
    def __init__(self, base_dir, diary_filename="my_life.txt"):
        self.base_dir = base_dir
        self.diary_path = os.path.join(base_dir, diary_filename)

    def get_last_entry_number(self) -> int:
        """Scan the diary file and return the last entry number."""
        entry_number = 0
        if os.path.exists(self.diary_path):
            with open(self.diary_path, "r") as f:
                for line in f:
                    if line.startswith(">>Entry:"):
                        try:
                            entry_number = int(line.replace(">>Entry:", "").strip())
                        except ValueError:
                            continue
        return entry_number

    def add_title_if_empty(self, title="=== My Life Diary ==="):
        """Add a title at the top if the file is new or empty."""
        if not os.path.exists(self.diary_path) or os.path.getsize(self.diary_path) == 0:
            with open(self.diary_path, "a") as diary_title:
                diary_title.write(f"{title}\n\n")