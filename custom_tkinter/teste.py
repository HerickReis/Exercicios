import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App:
    def __init__(self):
        self.janela = ctk.CTk()
        self.janela.geometry("400x300")
        self.janela.title("Customizando CTkTabview")

        # Criando o Tabview com todos os modificadores aplicados
        self.tabview = ctk.CTkTabview(
            master=self.janela, 
            width=300, 
            height=200, 
            corner_radius=10,                         # Bordas arredondadas do Tabview
            border_width=2,                           # Espessura da borda externa
            border_color="gray",                      # Cor da borda do Tabview
            fg_color="black",                         # Cor de fundo do Tabview
            segmented_button_fg_color="gray",          # Cor de fundo das abas
            segmented_button_selected_color="green",   # Cor da aba selecionada
            segmented_button_selected_hover_color="blue", # Cor ao passar o mouse na aba selecionada
            segmented_button_unselected_color="red",   # Cor das abas não selecionadas
            segmented_button_unselected_hover_color="purple" # Cor ao passar o mouse nas abas não selecionadas
        )
        self.tabview.pack(pady=20)

        # Adicionando abas
        self.tabview.add("Aba 1")
        self.tabview.add("Aba 2")
        self.tabview.add("Aba 3")

        # Definindo a aba inicial
        self.tabview.set("Aba 1")

        # Adicionando conteúdo na Aba 1
        self.label1 = ctk.CTkLabel(master=self.tabview.tab("Aba 1"), text="Conteúdo da Aba 1", text_color="white")
        self.label1.pack(pady=10)

        # Adicionando conteúdo na Aba 2
        self.label2 = ctk.CTkLabel(master=self.tabview.tab("Aba 2"), text="Conteúdo da Aba 2", text_color="white")
        self.label2.pack(pady=10)

        # Adicionando um botão na Aba 3
        self.botao = ctk.CTkButton(master=self.tabview.tab("Aba 3"), text="Clique Aqui")
        self.botao.pack(pady=10)

    def iniciar(self):
        self.janela.mainloop()

if __name__ == "__main__":
    app = App()
    app.iniciar()
