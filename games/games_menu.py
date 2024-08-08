from games.snake_game import run as run_snake_game

class GamesMenu:

    def __init__(self, options):
        self.options = options
        self.max_width = len(max(self.options, key=len))

    def print_options(self):
        for option in self.options:
            padding = " " * (self.max_width - len(option))
            print(f"║ {option}{padding} ║")

    def draw_frame(self):
        print(f"{' ' * (int(self.max_width / 2 - 2))}OYUNLAR")
        top_bottom = "═" * (self.max_width + 2)
        print(f"╔{top_bottom}╗")
        print(f"║ {' ' * self.max_width} ║")
        self.print_options()
        print(f"║ {' ' * self.max_width} ║")
        print(f"╚{top_bottom}╝")

    def get_selection(self):
        while True:
            try:
                selection = int(input("Bir seçenek seçin: "))
                if selection == 0:
                    print("Ana menüye dönülüyor...")
                    return None
                elif selection > len(self.options) - 1:
                    print("Geçersiz seçenek!")
                else:
                    print(self.options[selection - 1], "seçildi.")
                    return selection
            except ValueError:
                print("Lütfen bir sayı girin.")

    def run(self):
        while True:
            self.draw_frame()
            selection = self.get_selection()
            if selection is None:
                break
            elif selection == 1:
                run_snake_game()
    

def run():
    options = [
        "1-Yılan Oyunu",
        "0-Ana Menüye Dön",
    ]
    games_menu = GamesMenu(options)
    games_menu.run()


if __name__ == '__main__':
    run()
