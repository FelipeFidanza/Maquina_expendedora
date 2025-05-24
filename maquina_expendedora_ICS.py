'''
El siguiente programa simula una máquina expendedora. La misma acepta 4 tipos de billetes: de $1, $2, $5 y $10.
Se pueden ingresar como máximo 5 billetes. La máquina expendedora debe devolver el vuelto, siempre se debe intentar devolver el billete
de mayor valor (por ejemplo si el vuelto es de $10, se debe devolver un billete de $10 y no 10 de $1).

La máquina contiene snacks y refrescos. Tiene 5 filas (A-E) y 6 columnas (1-6). Cada fila tiene el mismo tipo de snack con su precio.
Es decir que existen 5 precios diferentes. Además, una vez que se ingrese la fila con la columna particular para sacar un producto, se
debe verificar si hay existencias de ese tipo. En caso de no haber, se debe informar por pantalla y devolver el monto ingresado.

Si se selecciona un producto pero el monto ingresado no es suficiente, también se debe devolver lo ingresado e informar que el monto
es insuficiente. Solamente se puede seleccionar un producto a la vez. Suponer también que la máquina siempre puede devolver billetes
de todos los tipos.

Los errores son:
    1. Error de exceso de billetes.
    2. Cantidad ingresada no alcanza el costo del producto.
    3. No hay existencias.
'''

#El primer valor es el valor de los productos de esa fila, los demás son las existencias
import os

existencias = [
    [24, 7, 6, 7, 5, 2, 4], # Galletitas $24
    [15, 5, 5, 2, 7, 4, 6], # Alfajor $15
    [8, 6, 1, 7, 3, 5, 3], # Chicle $8
    [37, 4, 3, 7, 4, 5, 1], # Chips $37
    [45, 7, 6, 7, 7, 4, 5] # Coca-cola $45
]

class MaquinaExpendedora():
    def __init__(self, existencias): # Inicializo la máquina con sus existencias y precios, además de la cantidad de billetes de cada tipo
        self.__existencias = existencias

    def __str__(self):  
        resultado = "Máquina Expendedora\n"
        resultado += "     " + "  ".join([f"{i}" for i in range(1, 7)]) + "\n"
        letras = ['A', 'B', 'C', 'D', 'E']
        productos = ['Galletitas', 'Alfajor', 'Chicle', 'Chips', 'Coca-Cola']

        for i, fila in enumerate(self.__existencias):
            resultado += f"{letras[i]}  | " + "  ".join(str(fila[j]) for j in range(1, 7)) + f" | {productos[i]} (${fila[0]})\n"

        return resultado

    
    def ingresa_billetes(self):
        os.system('cls')
        print(self)
        print("Ingrese cantidad de billetes (límite de 5 en total)")
        uno = int(input("billetes de 1: "))
        os.system('cls')
        print(self)
        print("Ingrese cantidad de billetes (límite de 5 en total)")
        dos = int(input("billetes de 2: "))
        os.system('cls')
        print(self)
        print("Ingrese cantidad de billetes (límite de 5 en total)")
        cinco = int(input("billetes de 5: "))
        os.system('cls')
        print(self)
        print("Ingrese cantidad de billetes (límite de 5 en total)")
        diez = int(input("billetes de 10: "))
        self.total_ingresado = uno*1 + dos*2 + cinco*5 + diez*10 # total ingresado a tener en cuenta para el vuelto
        if uno + dos + cinco + diez > 5:
            # Error de exceso
            self.__mensaje_error(1, self.__devuelve_vuelto(self.total_ingresado), self.total_ingresado)
            return False
        else:
            self._cantidad1 = uno
            self._cantidad2 = dos
            self._cantidad5 = cinco
            self._cantidad10 = diez
            return True

    def buscar_existencias(self, fila, columna):
        # Si hay existencias en la fila y columna ingresada
        if self.__existencias[fila][columna] > 0:
            # Si el monto ingresado es mayor o igual al coste del producto    
            if self.total_ingresado >= self.__existencias[fila][0]:
                self.__existencias[fila][columna] -= 1
                self.__mensaje_exito(fila, self.__devuelve_vuelto(self.total_ingresado - self.__existencias[fila][0]), self.total_ingresado - self.__existencias[fila][0])
            # Si el monto ingresado no alcanza el precio del producto
            else:
                # Debo informar y devolver el vuelto
                self.__mensaje_error(2, self.__devuelve_vuelto(self.total_ingresado), self.total_ingresado)
        #Si no hay existencias
        else:
            self.__mensaje_error(3, self.__devuelve_vuelto(self.total_ingresado), self.total_ingresado)
    
    def __devuelve_vuelto(self, numero):
        # Calculo la cantidad de billetes de cada tipo a devolver
        cantidad10 = numero//10
        cantidad5 = (numero%10)//5
        cantidad2 = ((numero%10)%5)//2
        cantidad1 = ((numero%10)%5)%2
        return [cantidad1, cantidad2, cantidad5, cantidad10]

    def __mensaje_error(self, tipo, billetes, vuelto=0):
        os.system('cls')
        print(self)
        if tipo == 1:
            print(f"Error. La cantidad máxima de billetes aceptados de 5, por favor intente de nuevo. Su vuelto es de ${vuelto} en:")
        if tipo == 2:
            print(f"Error. Dinero ingresado insuficiente, por favor intente de nuevo. Su vuelto es de ${vuelto} en:")
        if tipo == 3:
            print(f"Error. No hay existencias en la fila y columna seleccionada, por favor intente de nuevo. Su vuelto es de ${vuelto} en:")

        print(f"\t- {billetes[0]} billetes de $1")
        print(f"\t- {billetes[1]} billetes de $2")
        print(f"\t- {billetes[2]} billetes de $5")
        print(f"\t- {billetes[3]} billetes de $10")
        input("Presione enter para continuar...")

    def __mensaje_exito(self, producto, billetes, vuelto):
        os.system("cls")
        print(self)
        if producto == 0:
            print(f"Compraste unas Galletitas, su vuelto es de ${vuelto} en:")
        elif producto == 1:
            print(f"Compraste un Alfajor, su vuelto es de ${vuelto} en:")
        elif producto == 2:
            print(f"Compraste un Chicle, su vuelto es de ${vuelto} en:")
        elif producto == 3:
            print(f"Compraste unos Chips, su vuelto es de ${vuelto} en:")
        elif producto == 4:
            print(f"Compraste una Coca-Cola, su vuelto es de ${vuelto} en:")
        
        print(f"\t- {billetes[0]} billetes de $1")
        print(f"\t- {billetes[1]} billetes de $2")
        print(f"\t- {billetes[2]} billetes de $5")
        print(f"\t- {billetes[3]} billetes de $10")
        input("Presione enter para continuar...")

    def recarga_existencias(self, cantidad, producto):
        for i in range(1, 7):
            # Verifico si puedo cargar un producto en esa columna
            if self.__existencias[producto][i] < 7:
                self.__existencias[producto][i] += cantidad
                cantidad = 0
                # Si pasó el límite de 7
                if self.__existencias[producto][i] > 7:
                    cantidad = self.__existencias[producto][i] - 7
                    self.__existencias[producto][i] = 7
        os.system('cls')
        print(self)
        return f"Artículos recargados. cantidad sobrante: {cantidad}."

def convertir_fila(fila):
    if fila == "A":
        return 0
    elif fila == "B":
        return 1
    elif fila == "C":
        return 2
    elif fila == "D":
        return 3
    elif fila == "E":
        return 4

maquina = MaquinaExpendedora(existencias)

# Flujo del programa
while True:
    os.system('cls')
    print(maquina)
    print("0-Salir" + " "*2 + "|" + " "*2 + "1-Comprar" + " "*2 + "|" + " "*2 + "2-Recargar")
    try:
        opcion = int(input())
    except ValueError:
        os.system('cls')
        print(maquina)
        print("Entrada inválida. Por favor ingrese 0-1-2.")
        input("Presione enter para continuar...")
        continue
    
    # Desea comprar
    if opcion == 1:

        # Lógica de ingresar billetes
        while not maquina.ingresa_billetes():
            maquina.ingresa_billetes()
        
        # Lógica de ingresar fila y columna
        os.system('cls')
        print(maquina)
        fila = input("Ingrese fila: ").upper()
        while fila not in ["A", "B", "C", "D", "E"]:
            os.system("cls")
            print(maquina)
            fila = input("Ingrese fila válida (A-B-C-D-E): ").upper()
        fila = convertir_fila(fila)

        os.system('cls')
        print(maquina)
        columna = int(input("Ingrese columna: "))
        while columna not in [1, 2, 3, 4, 5, 6]:
            os.system("cls")
            print(maquina)
            columna = int(input("Ingrese columna válida (1-2-3-4-5-6): "))

        # Lógica de buscar existencias
        maquina.buscar_existencias(fila, columna)

    # Desea recargar
    elif opcion == 2:
        # Pido cantidad
        while True:
            os.system('cls')
            print(maquina)
            try:
                cantidad = int(input("Ingrese la cantidad: "))
                break
            except ValueError:
                os.system('cls')
                print(maquina)
                input("Debe ingresar un valor numérico.")
                continue

        # Pido artículo
        os.system('cls')
        print(maquina)
        print("Ingrese el producto (1-Galletitas | 2-Alfajor | 3-Chicle | 4-Chips | 5-Coca cola)")
        producto = input()
        while producto not in ["1", "2", "3", "4", "5"]:
            os.system('cls')
            print(maquina)
            input("Producto no válido. Intente nuevamente.")
            os.system('cls')
            print(maquina)
            print("Ingrese el producto (1-Galletitas | 2-Alfajor | 3-Chicle | 4-Chips | 5-Coca cola)")
            producto = input()
        producto = int(producto) - 1 # Para acomodarlo a la lista de python que arranca en 0

        os.system('cls')
        print(maquina)
        print(maquina.recarga_existencias(cantidad, producto))
        input()

    # Desea salir
    elif opcion == 0:
        break

    # Opcion no valida
    else:
        os.system('cls')
        print(maquina)
        input("Opción no válida. Intente nuevamente.")
       

os.system('cls')
print(maquina)
print("Hasta luego...")
