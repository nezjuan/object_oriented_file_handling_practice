class DiaryDesigns:
    def entry_start(self) -> str:
        return "[ E n t e r i n g   D i a r y   E n t r y . . . ]"

    def entry_number(self, number: int) -> str:
        return f"Entry: {number}"

    def closing(self) -> str:
        return "[ C l o s i n g . . . ]"

    def separator(self, char: str = "-") -> str:
        return char * 40