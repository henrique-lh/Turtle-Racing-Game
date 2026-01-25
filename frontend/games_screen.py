import customtkinter

from games import TurtleKart, SpaceInvaders


customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")


class GamesScreen(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.selected_game = None

        self.geometry("700x450")
        self.title("Hub")

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_columnconfigure(0, weight=1)

        self.scrollable_frame = customtkinter.CTkScrollableFrame(
            self, label_text="Escolha seu Jogo"
        )
        self.scrollable_frame.grid(
            row=0, column=0, padx=20, pady=(20, 10), sticky="nsew"
        )

        self.scrollable_frame.grid_columnconfigure((0, 1), weight=1)

        # Seus jogos
        self.games = {
            "Turtle Racing Game": TurtleKart,
            "Space Invaders": SpaceInvaders,
        }

        self.list_games()

        self.exit_button = customtkinter.CTkButton(
            self,
            text="EXIT",
            command=self.on_exit,
            fg_color="transparent",
            border_width=2,
        )
        self.exit_button.grid(row=1, column=0, padx=20, pady=20)

    def list_games(self):
        row = 0
        column = 0
        for game_name, game_class in self.games.items():
            button = customtkinter.CTkButton(
                master=self.scrollable_frame,
                text=game_name,
                command=lambda g=game_class: self.choose_game(g),
                height=100,
                font=("Arial", 17, "bold"),
            )
            button.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

            column += 1
            if column > 1:
                column = 0
                row += 1

    def choose_game(self, game_class):
        self.selected_game = game_class
        # Pequeno delay para permitir que a animação visual do botão ocorra
        self.after(100, self._finish)

    def _finish(self):
        self.quit()  # Encerra o mainloop, devolvendo o controle para run_hub

    def on_exit(self):
        self.selected_game = None
        self.quit()

    # --- AQUI ESTÁ A CORREÇÃO PRINCIPAL ---
    def destroy(self):
        """
        Sobrescreve o método destroy padrão para cancelar
        tarefas pendentes (como check_dpi_scaling) antes de fechar.
        """
        try:
            # Obtém todos os IDs de tarefas agendadas no sistema Tcl/Tk
            # 'after info' retorna uma tupla com os IDs das tarefas pendentes
            pending_tasks = self.tk.call('after', 'info')

            # O retorno pode variar dependendo da versão do Tk,
            # garantimos que seja iterável
            if pending_tasks:
                for task_id in pending_tasks:
                    try:
                        # Cancela cada tarefa pendente
                        self.after_cancel(task_id)
                    except Exception:
                        # Se falhar ao cancelar uma, ignoramos e tentamos a próxima
                        pass
        except Exception:
            pass  # Ignora qualquer erro durante a tentativa de limpeza

        # Chama o destroy original para fechar a janela
        super().destroy()


def run_hub():
    app = GamesScreen()
    app.mainloop()

    # Captura o jogo selecionado antes de destruir a janela
    selected_game = app.selected_game

    # Destroi a janela do CustomTkinter para liberar recursos
    try:
        app.destroy()
    except Exception:
        pass

    return selected_game