import json
import os

class NoteManager:
    def __init__(self, filename='notes.json'):
        self.filename = filename
        self.notes = self.load_notes()

    def load_notes(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    def save_notes(self):
        with open(self.filename, 'w') as file:
            json.dump(self.notes, file, indent=4)

    def create_note(self, title, content):
        note = {'title': title, 'content': content}
        self.notes.append(note)
        self.save_notes()

    def view_notes(self):
        return self.notes

    def update_note(self, index, title, content):
        if 0 <= index < len(self.notes):
            self.notes[index] = {'title': title, 'content': content}
            self.save_notes()

    def delete_note(self, index):
        if 0 <= index < len(self.notes):
            del self.notes[index]
            self.save_notes()
