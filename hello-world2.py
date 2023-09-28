import tkinter as tk
from tkinter import ttk, messagebox

def on_sair():
    if messagebox.askokcancel("Sair", "Deseja sair?"):
        root.destroy()

root = tk.Tk()

frm = ttk.Frame(root, padding=10)
frm.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))

# Centralizar os textos e botões
frm.grid_columnconfigure(0, weight=1)
frm.grid_rowconfigure(0, weight=1)
frm.grid_rowconfigure(1, weight=1)

ttk.Label(frm, text="Olá Mundo!").grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
ttk.Button(frm, text="Sair", command=on_sair).grid(column=0, row=1, sticky=(tk.N, tk.S, tk.E, tk.W))

# Centralizar a janela na tela
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

root.mainloop()