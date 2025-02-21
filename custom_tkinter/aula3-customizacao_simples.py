import customtkinter as ctk # Importa o modulo customtkinter

janela = ctk.CTk() # Cria a janela

# configurando a janela principal
janela.title("App teste")
janela.geometry("700x400")
janela.maxsize(width=900, height=400) # limita o tamanho maximo da janela
janela.minsize(width=500, height=300) # limita o tamanho minimo da janela
janela.resizable(width=False, height=False) # impede que a janela seja redimensionada
# janela.iconify() # Fecha determinada janela
# janela.deiconify() # reabre a janela

# customizando o tema da aplicacao = Aula 03

# janela._set_appearance_mode("dark") # Define o tema da aplicacao para dark
janela._set_appearance_mode("light") # Define o tema da aplicacao para dark
# janela._set_appearance_mode("system") # Define o tema da aplicacao para o tema do sistema

janela.mainloop()