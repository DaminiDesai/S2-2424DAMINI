import tkinter as tk
from tkinter import messagebox, Listbox, END

class AplicacionGestorTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        self.tareas = []

        # Campo de entrada para nuevas tareas
        self.campo_tarea = tk.Entry(root, width=50)
        self.campo_tarea.pack(pady=10)

        # Botones para gestionar tareas
        self.boton_agregar = tk.Button(root, text="Añadir Tarea", command=self.agregar_tarea)
        self.boton_agregar.pack(pady=5)

        self.boton_completar = tk.Button(root, text="Marcar como Completada", command=self.completar_tarea)
        self.boton_completar.pack(pady=5)

        self.boton_eliminar = tk.Button(root, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.boton_eliminar.pack(pady=5)

        # Listbox para mostrar las tareas
        self.lista_tareas = Listbox(root, width=50, height=10)
        self.lista_tareas.pack(pady=10)

        # Asignar atajos de teclado
        self.root.bind('<Return>', lambda event: self.agregar_tarea())
        self.root.bind('<c>', lambda event: self.completar_tarea())
        self.root.bind('<Delete>', lambda event: self.eliminar_tarea())
        self.root.bind('<Escape>', lambda event: root.quit())

    def agregar_tarea(self):
        contenido_tarea = self.campo_tarea.get()
        if contenido_tarea:
            self.tareas.append(contenido_tarea)
            self.actualizar_lista_tareas()
            self.campo_tarea.delete(0, END)
        else:
            messagebox.showwarning("Advertencia", "Por favor ingrese una tarea.")

    def completar_tarea(self):
        try:
            indice_seleccionado = self.lista_tareas.curselection()[0]
            tarea_completada = f"{self.tareas[indice_seleccionado]} (Completada)"
            self.tareas[indice_seleccionado] = tarea_completada
            self.actualizar_lista_tareas()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor seleccione una tarea.")

    def eliminar_tarea(self):
        try:
            indice_seleccionado = self.lista_tareas.curselection()[0]
            del self.tareas[indice_seleccionado]
            self.actualizar_lista_tareas()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor seleccione una tarea.")

    def actualizar_lista_tareas(self):
        self.lista_tareas.delete(0, END)
        for tarea in self.tareas:
            self.lista_tareas.insert(END, tarea)

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionGestorTareas(root)
    root.mainloop()