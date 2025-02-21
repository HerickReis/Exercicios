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

janela._set_appearance_mode("dark") # Define o tema da aplicacao para dark
# janela._set_appearance_mode("light") # Define o tema da aplicacao para dark
# janela._set_appearance_mode("system") # Define o tema da aplicacao para o tema do sistema

# Criando nova janela
def nova_tela():
    nova_janela = ctk.CTkToplevel(janela, fg_color="teal") # Cria uma nova janela
    nova_janela.geometry("500x250")

# btn_novatela = ctk.CTkButton(master=janela, text="Nova tela", command=nova_tela).place(x=300, y=100)


# Aula 08 - Dialogs

def abrir_dialog():
    dialog = ctk.CTkInputDialog(title="Caixa de dialogo", text="Digite seu nome:",
                                button_fg_color="blue", button_text_color="white", button_hover_color="gray", entry_border_color="blue", entry_fg_color="lightgray")
    print("Nome: ", dialog.get_input())

btn = ctk.CTkButton(janela, text="Abrir Dialog", command=abrir_dialog)
btn.pack()

janela.mainloop()
