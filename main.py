from frontend.games_screen import run_hub


def main():
    game_class = run_hub()

    if game_class is not None:
        print(game_class)
        game = game_class()

        if hasattr(game, 'config'):
            game.config()

        game.play()


if __name__ == "__main__":
    main()