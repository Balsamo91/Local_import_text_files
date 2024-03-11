def add_note(note, filename="notes.txt"):
    """Append a note to specified file."""
    with open(filename, "a")as file:
        file.write(note + "\n")

def list_notes(filename="notes.txt"):
    """Read all notes from the specified file and print them."""
    try:
        note_list = []
        with open(filename, "r") as file:
            notes = file.readlines()
            for note in notes:
                note_list.append(note.strip())
        return note_list
    except FileNotFoundError:
        return []
