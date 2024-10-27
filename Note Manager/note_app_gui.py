import tkinter as tk
from tkinter import messagebox, simpledialog
from note_manager import NoteManager

class NoteApp:
    def __init__(self, root):
        self.manager = NoteManager()
        self.root = root

        self.root.title("Gestor de Notas")
        self.root.geometry("400x600")  # Tamaño de la ventana
        self.root.configure(bg="#e0f7fa")

        # Configuración de la interfaz
        self.setup_login_ui()

    def setup_login_ui(self):
        self.clear_ui()
        self.login_frame = tk.Frame(self.root, bg="#e0f7fa")
        self.login_frame.pack(pady=20)

        tk.Label(self.login_frame, text="Iniciar Sesión", font=("Arial", 24, "bold"), bg="#e0f7fa", fg="#00796b").pack(pady=10)

        self.username_entry = tk.Entry(self.login_frame, width=30, font=("Arial", 12))
        self.username_entry.pack(pady=5)
        self.username_entry.insert(0, "Usuario")

        self.password_entry = tk.Entry(self.login_frame, show="*", width=30, font=("Arial", 12))
        self.password_entry.pack(pady=5)
        self.password_entry.insert(0, "Contraseña")

        tk.Button(self.login_frame, text="Entrar", command=self.login, bg="#00796b", fg="white", font=("Arial", 12, "bold"), bd=0, relief="flat").pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username and password:  # Reemplaza con tu lógica de autenticación
            self.setup_ui()  # Llama a la interfaz principal si la autenticación es exitosa
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingresa un usuario y contraseña válidos.")

    def setup_ui(self):
        self.clear_ui()
        self.root.configure(bg="#e0f7fa")

        # Título
        title_label = tk.Label(self.root, text="Notas", font=("Arial", 24, "bold"), bg="#e0f7fa", fg="#00796b")
        title_label.pack(pady=10)

        # Botón de Cerrar Sesión
        tk.Button(self.root, text="Cerrar Sesión", command=self.logout, bg="#ff6b6b", fg="white", font=("Arial", 12, "bold"), bd=0, relief="flat").pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=5)

        # Lista de notas
        self.note_list = tk.Listbox(self.root, width=50, height=15, font=("Arial", 12), bg="#ffffff", fg="#333333", selectbackground="#CCB078", bd=0, relief="flat")
        self.note_list.pack(pady=10)
        self.refresh_notes()

        # Campo de búsqueda
        self.search_entry = tk.Entry(self.root, width=50, font=("Arial", 12), bd=1, relief="flat")
        self.search_entry.pack(pady=5)
        self.search_entry.insert(0, "Buscar notas...")
        self.search_entry.bind("<KeyRelease>", self.search_notes)

        # Botones para las acciones
        button_frame = tk.Frame(self.root, bg="#e0f7fa")
        button_frame.pack(pady=5)

        # Añadiendo un poco de espaciado
        tk.Button(button_frame, text="Crear Nota", command=self.create_note, bg="#00796b", fg="white", font=("Arial", 12), bd=0, relief="flat").grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Ver Nota", command=self.view_note, bg="#00796b", fg="white", font=("Arial", 12), bd=0, relief="flat").grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Actualizar Nota", command=self.update_note, bg="#00796b", fg="white", font=("Arial", 12), bd=0, relief="flat").grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="Eliminar Nota", command=self.delete_note, bg="#00796b", fg="white", font=("Arial", 12), bd=0, relief="flat").grid(row=0, column=3, padx=5)

    def search_notes(self, event):
        query = self.search_entry.get().lower()
        self.note_list.delete(0, tk.END)
        for note in self.manager.view_notes():
            if query in note['title'].lower():
                self.note_list.insert(tk.END, note['title'])

    def logout(self):
        self.setup_login_ui()

    def clear_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def refresh_notes(self):
        self.note_list.delete(0, tk.END)
        for note in self.manager.view_notes():
            self.note_list.insert(tk.END, note['title'])

    def create_note(self):
        title = simpledialog.askstring("Crear Nota", "Título de la nota:")
        content = simpledialog.askstring("Crear Nota", "Contenido de la nota:")
        if title and content:
            self.manager.create_note(title, content)
            self.refresh_notes()
            messagebox.showinfo("Éxito", "Nota creada exitosamente.")

    def view_note(self):
        selected_index = self.note_list.curselection()
        if selected_index:
            note = self.manager.view_notes()[selected_index[0]]
            messagebox.showinfo(note['title'], note['content'])
        else:
            messagebox.showwarning("Advertencia", "Selecciona una nota para ver.")

    def update_note(self):
        selected_index = self.note_list.curselection()
        if selected_index:
            note = self.manager.view_notes()[selected_index[0]]
            title = simpledialog.askstring("Actualizar Nota", "Nuevo título:", initialvalue=note['title'])
            content = simpledialog.askstring("Actualizar Nota", "Nuevo contenido:", initialvalue=note['content'])
            if title and content:
                self.manager.update_note(selected_index[0], title, content)
                self.refresh_notes()
                messagebox.showinfo("Éxito", "Nota actualizada exitosamente.")
        else:
            messagebox.showwarning("Advertencia", "Selecciona una nota para actualizar.")

    def delete_note(self):
        selected_index = self.note_list.curselection()
        if selected_index:
            self.manager.delete_note(selected_index[0])
            self.refresh_notes()
            messagebox.showinfo("Éxito", "Nota eliminada exitosamente.")
        else:
            messagebox.showwarning("Advertencia", "Selecciona una nota para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()









