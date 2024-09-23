import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title("Agenda Personal")
root.geometry("400x400")

tree = ttk.Treeview(root, columns=("Fecha", "Hora", "Descripción"), show='headings')
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack(pady=20)

tk.Label(root, text="Fecha (DD/MM/AAAA)").pack()
fecha_entry = tk.Entry(root)
fecha_entry.pack()

tk.Label(root, text="Hora (HH:MM)").pack()
hora_entry = tk.Entry(root)
hora_entry.pack()

tk.Label(root, text="Descripción").pack()
descripcion_entry = tk.Entry(root)
descripcion_entry.pack()
def agregar_evento():
    fecha = fecha_entry.get()
    hora = hora_entry.get()
    descripcion = descripcion_entry.get()
    if fecha and hora and descripcion:
        tree.insert("", "end", values=(fecha, hora, descripcion))
        fecha_entry.delete(0, 'end')
        hora_entry.delete(0, 'end')
        descripcion_entry.delete(0, 'end')
    else:
        messagebox.showwarning("Advertencia", "Todos los campos deben ser llenados")

def eliminar_evento():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)
    else:
        messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar")

tk.Button(root, text="Agregar Evento", command=agregar_evento).pack(pady=5)
tk.Button(root, text="Eliminar Evento Seleccionado", command=eliminar_evento).pack(pady=5)
tk.Button(root, text="Salir", command=root.quit).pack(pady=5)
frame = tk.Frame(root)
frame.pack(pady=10)

# Agregar widgets al frame en lugar de directamente a root
frame.pack(side=tk.TOP)
root.mainloop()