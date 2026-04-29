with(open("./my_life.txt","a")) as diary_entry:
    while True:
        text_line=input("Text to Input: ")
        diary_entry.write(f"> {text_line}\n")
        choice=input("Are There More(Y/N)?: ").upper()
        if choice!=("Y"):
            print("[C l o s i n g . . .]")
            break
