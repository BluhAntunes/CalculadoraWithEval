import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora")
janela.config(bg="lightblue")

display_area = tk.Entry(janela, width=20)
display_area.grid(column=6, row=1)
def result():
    a = display_area.get()
    b = eval(a)
    display_area.delete(0, 600)
    display_area.insert(0, b)
    print(b)

byantunes = tk.Label(janela, text="Calculadora by Antunes")
byantunes.grid(column=4,row=5)
botao = tk.Button(janela, text="Aperte aqui", command=result, width=8, height=3)
botao.grid(column=6, row=2)
def c():
    display_area.delete(0, 9)

botaoc = tk.Button(janela, text="C", command=c, width=8, height=3)
botaoc.grid(column=6, row=3)
pos = 0


def botao1a():
    global pos
    pos = pos+1
    display_area.insert(pos, "1")
def botao2a():
    global pos
    pos = pos+1
    display_area.insert(pos, "2")
def botao3a():
    global pos
    pos = pos+1
    display_area.insert(pos, "3")
def botao4a():
    global pos
    pos = pos+1
    display_area.insert(pos, "4")
def botao5a():
    global pos
    pos = pos+1
    display_area.insert(pos, "5")
def botao6a():
    global pos
    pos = pos+1
    display_area.insert(pos, "6")
def botao7a():
    global pos
    pos = pos+1
    display_area.insert(pos, "7")
def botao8a():
    global pos
    pos = pos+1
    display_area.insert(pos, "8")
def botao9a():
    global pos
    pos = pos+1
    display_area.insert(pos, "9")
def botao0a():
    global pos
    pos = pos+1
    display_area.insert(pos, "0")
def botaomenos():
    global pos
    pos = pos+1
    display_area.insert(pos, "-")
def botaomais():
    global pos
    pos = pos+1
    display_area.insert(pos, "+")
def botaodiv():
    global pos
    pos = pos+1
    display_area.insert(pos, "/")
def botaomul():
    global pos
    pos = pos+1
    display_area.insert(pos, "*")

botao1 = tk.Button(janela, text="1", command=botao1a, width=8, height=3)
botao1.grid(column=1, row=1)

botao2 = tk.Button(janela, text="2", command=botao2a, width=8, height=3)
botao2.grid(column=2, row=1)

botao3 = tk.Button(janela, text="3", command=botao3a, width=8, height=3)
botao3.grid(column=3, row=1)

botao4 = tk.Button(janela, text="4", command=botao4a, width=8, height=3)
botao4.grid(column=1, row=2)

botao5 = tk.Button(janela, text="5", command=botao5a, width=8, height=3)
botao5.grid(column=2, row=2)

botao6 = tk.Button(janela, text="6", command=botao6a, width=8, height=3)
botao6.grid(column=3, row=2)

botao7 = tk.Button(janela, text="7", command=botao7a, width=8, height=3)
botao7.grid(column=1, row=3)

botao8 = tk.Button(janela, text="8", command=botao8a, width=8, height=3)
botao8.grid(column=2, row=3)

botao9 = tk.Button(janela, text="9", command=botao9a, width=8, height=3)
botao9.grid(column=3, row=3)

botao0 = tk.Button(janela, text="0", command=botao0a, width=8, height=3)
botao0.grid(column=2, row=4)

botaodiva = tk.Button(janela, text="/", command=botaodiv, width=8, height=3)
botaodiva.grid(column=4, row=1)

botaomula = tk.Button(janela, text="X", command=botaomul, width=8, height=3)
botaomula.grid(column=5, row=1)

botaomaisa = tk.Button(janela, text="+", command=botaomais, width=8, height=3)
botaomaisa.grid(column=4, row=2)

botaomenosa = tk.Button(janela, text="-", command=botaomenos, width=8, height=3)
botaomenosa.grid(column=5, row=2)

janela.mainloop()