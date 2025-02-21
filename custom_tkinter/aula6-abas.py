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

# Aula 06 - Tabview (Abas no tkinter)
tabview = ctk.CTkTabview(master=janela, width=400, corner_radius=20, border_width=2, border_color="black", 
        fg_color="teal", segmented_button_fg_color="red", segmented_button_selected_color="green", segmented_button_selected_hover_color="gray", 
        segmented_button_unselected_color="black", segmented_button_unselected_hover_color="purple") # Modificadores de aparencia dos atributos da tabview
tabview.pack()
tabview.add("Nomes")
tabview.add("Idades")
tabview.add("Sexo")
tabview.add("Endereços")

tabview.tab("Nomes").grid_columnconfigure(0, weight=1)
tabview.tab("Idades").grid_columnconfigure(0, weight=1)
tabview.tab("Sexo").grid_columnconfigure(0, weight=1)
tabview.tab("Endereços").grid_columnconfigure(0, weight=1)

# Adicionando elementos na nossa tabview
text = ctk.CTkLabel(tabview.tab("Nomes"), text="Salvador Dali\nAda Lovelace\nPablo Picasso\nClaude Monet\nLeonardo Da Vinci")
text.pack()

text2 = ctk.CTkLabel(tabview.tab("Idades"), text="50\n36\n60\n55\n70")
text2.pack()

text3 = ctk.CTkLabel(tabview.tab("Sexo"), text="Masculino\nFeminino\nMasculino\nMasculino\nMasculino")
text3.pack()

text4 = ctk.CTkLabel(tabview.tab("Endereços"), text="Rua 1\nRua 2\nRua 3\nRua 4\nRua 5")
text4.pack()

janela.mainloop()
