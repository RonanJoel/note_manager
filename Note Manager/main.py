from note_manager import NoteManager

def main():
    manager = NoteManager()

    while True:
        print("\nNote Manager")
        print("1. Create a note")
        print("2. View notes")
        print("3. Update a note")
        print("4. Delete a note")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            manager.create_note(title, content)
            print("Note created successfully.")

        elif choice == '2':
            notes = manager.view_notes()
            if notes:
                for i, note in enumerate(notes):
                    print(f"{i + 1}. {note['title']}: {note['content']}")
            else:
                print("No notes available.")

        elif choice == '3':
            index = int(input("Enter note number to update: ")) - 1
            title = input("Enter new title: ")
            content = input("Enter new content: ")
            manager.update_note(index, title, content)
            print("Note updated successfully.")

        elif choice == '4':
            index = int(input("Enter note number to delete: ")) - 1
            manager.delete_note(index)
            print("Note deleted successfully.")

        elif choice == '5':
            print("Exiting the Note Manager.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
