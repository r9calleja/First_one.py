import csv
import config 


class Cliente:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni.strip()
        self.nombre = nombre.strip()
        self.apellido = apellido.strip()

    def __str__(self):
        return f"({self.dni}) {self.nombre} {self.apellido}"


class Clientes:

    lista = []

    def __init__(self):
        with open(config.DATABASE_PATH, "r", newline="\n") as fichero:
            reader = csv.reader(fichero, delimiter=";")
            for dni, nombre, apellido in reader:
                cliente = Cliente(dni, nombre, apellido)
                self.lista.append(cliente)

    def buscar(self, dni):
        for cliente in self.lista:
            if cliente.dni == dni:
                return cliente
        return None

    def crear(self, dni, nombre, apellido):
        if not isinstance(dni, str):
            raise TypeError("El DNI debe ser una cadena")
        if not dni.isalnum():
            raise ValueError("El DNI debe contener solo números y letras")
        if len(dni) != 9:
            raise ValueError("El DNI debe tener 9 caracteres")
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una cadena")
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")
        if not isinstance(apellido, str):
            raise TypeError("El apellido debe ser una cadena")
        if not apellido:
            raise ValueError("El apellido no puede estar vacío")

        cliente = Cliente(dni, nombre, apellido)
        self.lista.append(cliente)
        self.guardar()
        return cliente

    def modificar(self, dni, nombre, apellido):
        cliente = self.buscar(dni)
        if cliente is None:
            raise ValueError("El cliente no existe")

        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una cadena")
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")
        if not isinstance(apellido, str):
            raise TypeError("El apellido debe ser una cadena")
        if not apellido:
            raise ValueError("El apellido no puede estar vacío")

        cliente.nombre = nombre
        cliente.apellido = apellido
        self.guardar()
        return cliente

    def borrar(self, dni):
        cliente = self.buscar(dni)
        if cliente is None:
            raise ValueError("El cliente no existe")

        self.lista.remove(cliente)
        self.guardar()
        return cliente

    def guardar(self):
        with open(config.DATABASE_PATH, "w", newline="\n") as fichero:
        
            writer = csv.writer(fichero, delimiter=";")
            for cliente in self.lista:
                writer.writerow((cliente.dni, cliente.nombre, cliente.apellido))


if __name__ == "__main__":
    clientes = Clientes()

    cliente = clientes.crear("12345678A", "Juan", "Pérez")
    print(cliente)

    cliente = clientes.modificar("12345678A", "María", "López")
    print(cliente)

    cliente = clientes.borrar("12345678A")
    print(cliente)
