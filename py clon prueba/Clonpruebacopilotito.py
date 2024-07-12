class Player:
    def __init__(self, first_name, last_name, city, game):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.game = game

class TournamentRegistration:
    def __init__(self):
        self.registrations = []

    def register(self, player):
        self.registrations.append(player)

    def list_registrations(self):
        print("All registrations:")
        for i, player in enumerate(self.registrations, start=1):
            print(f"{i}. {player.first_name} {player.last_name} ({player.city}) {player.game}")

    def print_game_details(self, game):
        filename = f"{game}_registrations.txt"
        with open(filename, "w") as file:
            file.write(f"Registrations for {game}:\n")
            for player in self.registrations:
                if player.game == game:
                    file.write(f"{player.first_name} {player.last_name} ({player.city})\n")
        print(f"Details for {game} saved to {filename}")


def main():
    tournament = TournamentRegistration()

    while True:
        print("\nMenu:")
        print(" \n1. Inscripción a videojuegos del torneo\n2. Lista inscripciones\n3. Lista detalle por videojuego\n4. Salir")

        choice = input("Enter your choice: ")

        if choice == "1":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            city = input("Enter city: ")
            game = input("Enter game (Fortnite, League of Legends, or Valorant): ").lower()
            player = Player(first_name, last_name, city, game)
            tournament.register(player)
            print("Player registered successfully.")
        elif choice == "2":
            tournament.list_registrations()
        elif choice == "3":
            game = input("Enter game (Fortnite, League of Legends, or Valorant): ")
            tournament.print_game_details(game)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

print(main())