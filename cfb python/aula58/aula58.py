from tkinter import *

app = Tk() # Instancia o objeto Tk
app.title("Aula 58")
app.geometry("500x300")
app.configure(bg="#dde")

# O anchor é um atributo que define a posição do texto em relação ao ponto de ancoragem
# anchor => N, NE, E, SE, S, SW, W, NW, CENTER
Label(app, text="Nome", bg="#dde", fg="#009", anchor=CENTER).pack(padx=20)
vnome = Entry(app)
vnome.place(x=150, y=30, width=200, height=20)

Label(app, text="Telefone", bg='#dde', fg="#009", anchor=CENTER).pack(padx=20)
vtelefone = Entry(app)
vtelefone.place(x=150, y=60, width=200, height=20)

app.mainloop() # Exibe a janela