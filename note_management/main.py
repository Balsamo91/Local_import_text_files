from note_manager import add_note, list_notes

while True:
    print("\n Note-taking Application")
    print("1. Add note")
    print("2. List notes")
    print("3, exit")
    choice = input("choose and option: ")

    if choice == "1":
        note = input("Write your note: ")
        add_note(note)
        print("Note added successfully")

    elif choice == "2":
        notes = list_notes()
        print("\nNotes:")
        for note in notes:
            print(f"- {note}")
        if not notes:
            print("No notes available")

    elif choice == "3":
        print("Bye")
        break
    else:
        print("Invalid command")