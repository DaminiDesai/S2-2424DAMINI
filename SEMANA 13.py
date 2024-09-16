import tkinter as tk
from tkinter import messagebox, Listbox

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplicación GUI Básica")
        self.geometry("400x300")

        # Etiqueta
        self.label = tk.Label(self, text="Ingresa un dato:")
        self.label.pack()

        # Campo de texto
        self.entry = tk.Entry(self)
        self.entry.pack()

        # Botón "Agregar"
        self.add_button = tk.Button(self, text="Agregar", command=self.add_item)
        self.add_button.pack()

        # Lista para mostrar datos
        self.listbox = Listbox(self)
        self.listbox.pack()

        # Botón "Limpiar"
        self.clear_button = tk.Button(self, text="Limpiar", command=self.clear_list)
        self.clear_button.pack()

    def add_item(self):
        item = self.entry.get()
        if item:
            self.listbox.insert(tk.END, item)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor ingresa un dato.")

    def clear_list(self):
        self.listbox.delete(0, tk.END)
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    app = App()
    app.mainloop()
