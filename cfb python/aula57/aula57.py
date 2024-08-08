from tkinter import *

app = Tk() # Instancia o objeto Tk
app.title("Aula 57") # Define o título da janela
app.geometry("500x300") # Define o tamanho da janela
app.configure(background="#008") # Define a cor de fundo da janela
app.resizable(width=False, height=False) # Impede que a janela seja redimensionada
app.attributes("-alpha", 1) # Define a transparência da janela
app.attributes("-topmost", True) # Define que a janela ficará sempre no topo
app.attributes("-fullscreen", True) # Define que a janela será exibida em tela cheia

txt1 = Label(app, text="Curso de Python", background="#018", foreground="#fff", font=("Arial", 20, "bold italic")) # Define o texto
txt1.place(x=10, y=10, width=300, height=30)  # Define a posição e o tamanho do texto

vtxt = "Modulo Tkinter" # Define o texto
vbg = "#ff0" # Define a cor de fundo
vfg = "#f00" # Define a cor da fonte
vfont = ("Arial", 20, "bold italic") # Define a fonte
txt2 = Label(app, text=vtxt, bg=vbg, fg=vfg, font=vfont) # Define o texto
txt2.place(x=10, y=50, width=300, height=30) # Define a posição e o tamanho do texto

app.mainloop()