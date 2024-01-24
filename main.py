from games import TurtleKart

def main():
    user_bet = "yellow"
    game = TurtleKart()
    game.config()
    game.play(user_bet=user_bet)

if __name__ == "__main__":
    main()

