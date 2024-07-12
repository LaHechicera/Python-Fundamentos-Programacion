class jugador: #la palabra "class" es como un molde que crea un objeto en este caso se creo un objeto "jugador"
    def inicio(self, nom, ape, ciudad, juego): #siempre se utiliza "self" al inicio de una clase para referirse a si mismo
        self.nom = nom
        self.ape = ape
        self.ciudad = ciudad
        self.juego = juego

class registro:
    def inicio(self):
        self.registros = []

    def registro(self, jugador):
        self.registros.append(jugador)

    def listaregistro(self):
        print("Todas las inscripciones:")
        for i, jugador in enumerate(self.listaregistro, start=1):
            print(f"{i}. {jugador.nom} {jugador.ape} ({jugador.ciudad}) - {jugador.juego}")

    def detallejuegos(self, juego):
        filename = f"{juego}_registrations.txt"
        with open(filename, "w") as file:
            file.write(f"Registrations for {juego}:\n")
            for jugador in self.registros:
                if jugador.juego == juego:
                    file.write(f"{jugador.nom} {jugador.ape} ({jugador.ciudad})\n")
        print(f"Detalles del {juego} han sido guardados en el archivo {filename}")


def principal():
    torneo = registro()

    while True:
        print("----Inscripción para torneo de videojuegos----")
        print(" \nSeleccione una opción")
        print(" \n1. Inscripción a videojuegos del torneo\n2. Lista inscripciones\n3. Lista detalle por videojuego\n4. Salir")

        op = input("Ingrese su opcion: ")

        if op == "1":
            nom = input("Ingrese su primer nombre: ").lower()
            ape = input("Ingrese su apellido: ").lower()
            ciudad = input("Ingrese su ciudad: ").lower()
            juego = input("Ingrese el nombre del juego (Fortnite, League of Legends, or Valorant): ").lower()
            jugador1 = jugador(nom, ape, ciudad, juego)
            torneo.registro(jugador1)
            print("El jugador a sido registrado con exito!")
        elif op == "2":
            torneo.listaregistro()
        elif op == "3":
            juego = input("Ingrese el juego a listar (Fortnite, League of Legends, or Valorant): ")
            torneo.detallejuegos(juego)
        elif op == "4":
            print("Salio del programa")
            break
        else:
            print("Opcion no valida, intente de nuevo")

print(principal())