import customtkinter


# Importações mantidas conforme seu exemplo
# from frontend.components import ExitButton
# from games import TurtleKart, SpaceInvaders

class GamesScreen(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("700x450")
        self.title("Hub")

        # Configuração do Grid Principal (O frame de scroll ocupa o topo, Exit fica embaixo)
        self.grid_rowconfigure(0, weight=1)  # Área dos jogos cresce
        self.grid_rowconfigure(1, weight=0)  # Botão Exit fixo embaixo
        self.grid_columnconfigure(0, weight=1)

        # 1. Container de Scroll para os Jogos
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self,
                                                                 label_text="Escolha seu Jogo")
        self.scrollable_frame.grid(row=0, column=0, padx=20, pady=(20, 10),
                                   sticky="nsew")

        # Configura duas colunas dentro do frame de scroll para ficarem "lado a lado"
        self.scrollable_frame.grid_columnconfigure((0, 1), weight=1)

        # O seu dicionário de jogos
        self.games = {
            "Turtle Racing Game": "TurtleKart",  # Substitua pela classe real
            "Space Invaders": "SpaceInvaders",  # Substitua pela classe real
            "Game 3": "Exemplo3",
            "Game 4": "Exemplo4",
            "Game 5": "Exemplo5",
        }

        # 2. Gerar os botões dinamicamente
        self.list_games()

        # 3. Botão de Exit (Sempre visível no rodapé)
        # Utilizando o seu ExitButton customizado
        self.exit_button = customtkinter.CTkButton(self, text="EXIT",
                                                   command=self.destroy,
                                                   fg_color="transparent",
                                                   border_width=2)
        # Se preferir usar sua classe: self.exit_button = ExitButton(self)
        self.exit_button.grid(row=1, column=0, padx=20, pady=20)

    def list_games(self):
        row = 0
        column = 0

        for game_name, game_class in self.games.items():
            # Criamos o botão dentro do scrollable_frame
            button = customtkinter.CTkButton(
                master=self.scrollable_frame,
                text=game_name,
                command=lambda g=game_class: self.open_game(g),
                height=100,  # Altura maior conforme seu mockup
                font=("Hack Nerd Font", 17)
            )
            button.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

            # Lógica para alternar colunas (0 e 1)
            column += 1
            if column > 1:
                column = 0
                row += 1

    def open_game(self, game_class):
        print(f"Iniciando: {game_class}")
        # Aqui você instancia a classe do jogo: game_class()