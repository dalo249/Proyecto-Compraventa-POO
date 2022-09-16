class Moto:

    def __init__(self, placa: str, modelo: str, marca: str, cilindraje: int, categoria: int, precio_unitario, cantidad : int):

        self.placa: str = placa
        self.modelo: str = modelo
        self.marca: str = marca
        self.cilindraje: str = cilindraje
        self.categoria: int = categoria
        self.precio_unitario: float = precio_unitario
        self.cantidad: int = cantidad




class Mi_catalogo:


    def __init__(self,):

        self.mis_motos : dict[str, Moto] = {}

    def agregar_moto(self, mi_moto: Moto):
        self.mis_motos[mi_moto.placa] = mi_moto

    def eliminar_moto_venta(self, placa: str) :
        if placa in self.mis_motos.keys():
            del self.mis_motos[placa]




class Usuario:

    def __init__(self, cedula: str, nombre: str):

        self.cedula : str = cedula
        self.nombre : str = nombre
        self.mi_catalogo = Mi_catalogo()

    def agregar_moto_a_mi_catalogo(self, mi_moto: Moto):
         self.mi_catalogo.agregar_moto(mi_moto)

class Compraventa:

    def __init__(self):

        self.motos_disponibles = {}
        self.usuarios = {}

    def registrar_moto(self, placa: str, modelo : str, marca : str, cilindraje: int, categoria : int, precio_unitario: float, cantidad: int, cedula: str):
        if placa not in self.motos_disponibles.keys():
            moto = Moto(placa, modelo, marca, cilindraje, categoria, precio_unitario, cantidad)
            self.motos_disponibles[placa] = moto

    def buscar_usuario(self, cedula) -> Usuario:
        pass

    def agregar_moto_a_mi_catalogo(self, moto: Moto, cedula: str):
        mi_moto = moto
        usuario = self.buscar_usuario(cedula)
        usuario.agregar_moto_a_mi_catalogo(mi_moto)


    def buscar_moto_disponible(self, categoria: int, marca: str, cilindraje: int, placa: int)-> Moto:
        """
        Este metodo permite filtrar las motos disponibles en dos categorias: motos nuevas y usadas
        nota: las motos nuevas no tienen placa, para acceder a una moto especifica el usuario debe ingresar su marca y cilindraje
        :param categoria: si ingresa 1 -> motos usadas, si ingresa 2 -> motos nuevas
        :param marca: parametro buscar moto nueva
        :param cilindraje: parametro para buscar moto nueva
        :param placa: unico parametro necesario para buscar una moto especifica de categoria motos usadas .
        :return: moto especifica nueva o usada -> diccionario motos_disponibles
        """
        if categoria == 2:
          if marca in self.motos_disponibles.values():
            if cilindraje in self.motos_disponibles.values():
              return self.motos_disponibles[str: marca, cilindraje]


        else:
            if placa in self.motos_disponibles.keys():
                return self.motos_disponibles[placa]


    def comprar_moto(self, categoria: int, marca: str, cilindraje: int, placa: int):

        if categoria == 2:
             Moto_usada = self.buscar_moto_disponibles[placa]
             del self.motos_disponibles[Moto_usada]

        else:
            Moto_nueva = self.buscar_moto_disponible[str: marca, cilindraje]
            del self.motos_disponibles[Moto_nueva]










