from metal import Metal
from papel import Papel
from plastico import Plastico
from vidro import Vidro
from organico import Organico
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

lista = []

#Função que registra os resíduos
def registroResiduo():
    massa = entryPeso.get()
    tipo = varTipo.get()
    
    if tipo == "Plástico": 
        if massa == "":
          messagebox.showinfo("Erro", f"Massa de resíduo {tipo} deve ser preenchida.")
        elif not massa.isdigit():
          messagebox.showinfo("Erro", f"Massa do resíduo {tipo} inválida.")
        else:
          p = Plastico(massa, tipo, reciclavel=True)
          salvar(p)
          messagebox.showinfo("Registro de resíduos", f"{massa}Kg de {tipo} registrado com sucesso!")
    elif tipo == "Orgânico": 
        if massa == "":
          messagebox.showinfo("Erro", f"Massa do resíduo {tipo} deve ser preenchida.")
        elif not massa.isdigit():
          messagebox.showinfo("Erro", f"Massa do resíduo {tipo} inválida.")
        else:
          o = Organico(massa, tipo, reciclavel=False)
          salvar(o)
          messagebox.showinfo("Registro de resíduos", f"{massa}Kg de resíduo {tipo} registrado com sucesso!")
    elif tipo == "Metal": 
        if massa == "":
          messagebox.showinfo("Erro", "Massa do resíduo deve ser preenchida.")
        elif not massa.isdigit():
          messagebox.showinfo("Erro", f"Massa do resíduo {tipo} inválida.")
        else:
          m = Metal(massa, tipo, reciclavel=True)
          salvar(m)
          messagebox.showinfo("Registro de resíduos", f"{massa}Kg de {tipo} registrado com sucesso!")
    elif tipo == "Vidro": 
        if massa == "":
          messagebox.showinfo("Erro", "Massa do resíduo deve ser preenchida.")
        elif not massa.isdigit():
          messagebox.showinfo("Erro", f"Massa do resíduo {tipo} inválida.")
        else:
          v = Vidro(massa, tipo, reciclavel=True)
          salvar(v)
          messagebox.showinfo("Registro de resíduos", f"{massa}Kg de {tipo} registrado com sucesso!")
    elif tipo == "Papel": 
        if massa == "":
          messagebox.showinfo("Erro", "Massa do resíduo deve ser preenchida.")
        elif not massa.isdigit():
          messagebox.showinfo("Erro", f"Massa do resíduo {tipo} inválida.")
        else:
          pa = Papel(massa, tipo, reciclavel=True)
          salvar(pa)
          messagebox.showinfo("Registro de resíduos", f"{massa}Kg de {tipo} registrado com sucesso!")  
   
#Função que salva os resíduos na lista
def salvar(obj):
    lista.append(obj)

def atualizarListbox():
    listbox.delete(0, tk.END)
    for obj in lista:
        listbox.insert(tk.END, obj.mostrar())


#Criação das janelas e seus elementos(botões, entradas e tabs)
janela = tk.Tk()
janela.title("Registro de Resíduos")
janela.geometry("500x300")

janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)

janelinha = ttk.Notebook(janela)
janelinha.grid(row=0, column=0, sticky="nsew")

tab1 = ttk.Frame(janelinha)

for i in range(6):
    tab1.grid_rowconfigure(i, weight=1)
tab1.grid_columnconfigure(0, weight=1)
tab1.grid_columnconfigure(1, weight=1)

tab2 = ttk.Frame(janelinha)
tab2.grid_rowconfigure(0, weight=1)
tab2.grid_columnconfigure(0, weight=1)

janelinha.add(tab1, text="Registro")
janelinha.add(tab2, text="Resíduos")

label1 = tk.Label(tab1, text="Massa(Kg):", font=("",15))
label1.grid(row=0, column=0, sticky="w", padx=10)

entryPeso = tk.Entry(tab1, font=("", 15))
entryPeso.grid(row=0, column=1, sticky="nsew", padx=10, pady=5)

tk.Label(tab1, text="Tipo", font=("", 15)).grid(row=4, column=0, sticky="w", padx=10)
varTipo = tk.StringVar(value="Orgânico")

tk.Radiobutton(tab1, text="Orgânico", font=("", 10), variable=varTipo, value="Orgânico").grid(row=4, column=1, sticky="w", padx=10)
tk.Radiobutton(tab1, text="Plástico", font=("", 10), variable=varTipo, value="Plástico").grid(row=4, column=1, sticky="e", padx=10)
tk.Radiobutton(tab1, text="Vidro", font=("", 10), variable=varTipo, value="Vidro").grid(row=5, column=1, sticky="w", padx=10)
tk.Radiobutton(tab1, text="Metal", font=("", 10), variable=varTipo, value="Metal").grid(row=5, column=1, sticky="e", padx=10)
tk.Radiobutton(tab1, text="Papel", font=("", 10), variable=varTipo, value="Papel").grid(row=6, column=1, sticky="w", padx=10)
tk.Button(tab1, text="Registrar", font=("", 15), command=registroResiduo).grid(row=7, columnspan=2)

#Criação da lista de registro de resíduos
listbox = tk.Listbox(tab2)
listbox.config(font=("", 15))
listbox.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
tk.Button(tab2, text="Atualizar",font=("", 15), command=atualizarListbox).grid(row=1, column=0, sticky="nsew")

#Função que impede que 
janela.mainloop()