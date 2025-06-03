import os
import time

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

    
    def comprueba_billetes(self, lista_billetes):
        # Total ingresado a tener en cuenta para el vuelto
        self.total_ingresado = lista_billetes[0]*1 + lista_billetes[1]*2 + lista_billetes[2]*5 + lista_billetes[3]*10 
        if sum(lista_billetes) > 5:
            # Error de exceso
            self.__mensaje_error(1, self.__devuelve_vuelto(self.total_ingresado), self.total_ingresado)
            return False
        else:
            self._cantidad1 = lista_billetes[0]
            self._cantidad2 = lista_billetes[1]
            self._cantidad5 = lista_billetes[2]
            self._cantidad10 = lista_billetes[3]
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
        print("Presione enter para continuar...")
        time.sleep(3)

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
        print("Presione enter para continuar...")
        time.sleep(3)

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

def ingresa_billetes(maquina):
    os.system('cls')
    print(maquina)
    print("Ingrese cantidad de billetes (límite de 5 en total)")
    #uno = int(input("billetes de 1: "))
    time.sleep(2)
    os.system('cls')
    print(maquina)
    print("Ingrese cantidad de billetes (límite de 5 en total)")
    #dos = int(input("billetes de 2: "))
    time.sleep(2)
    os.system('cls')
    print(maquina)
    print("Ingrese cantidad de billetes (límite de 5 en total)")
    #cinco = int(input("billetes de 5: "))
    time.sleep(2)
    os.system('cls')
    print(maquina)
    print("Ingrese cantidad de billetes (límite de 5 en total)")
    #diez = int(input("billetes de 10: "))
    time.sleep(2)

    return [0, 0, 0, 5]



# Flujo del programa
maquina = MaquinaExpendedora(existencias)

for i in range(3):
    os.system('cls')
    print(maquina)
    print("0-Salir" + " "*2 + "|" + " "*2 + "1-Comprar" + " "*2 + "|" + " "*2 + "2-Recargar")
    
    # Desea comprar
    if i == 0:

        # Lógica de ingresar billetes
        maquina.comprueba_billetes(ingresa_billetes(maquina))
        
        # Lógica de ingresar fila y columna
        os.system('cls')
        print(maquina)
        print("Ingrese fila: ")
        time.sleep(3)
        fila = convertir_fila("D")

        os.system('cls')
        print(maquina)
        print("Ingrese columna: ")
        time.sleep(3)
        columna = 3

        # Lógica de buscar existencias
        maquina.buscar_existencias(fila, columna)

    # Desea recargar
    elif i == 1:
        # Pido cantidad
        os.system('cls')
        print(maquina)
        print("Ingrese la cantidad: ")
        time.sleep(3)
        cantidad = 15

        # Pido artículo
        os.system('cls')
        print(maquina)
        print("Ingrese el producto (1-Galletitas | 2-Alfajor | 3-Chicle | 4-Chips | 5-Coca cola)")
        time.sleep(3)
        producto = 3
        producto -= 1 # Para acomodarlo a la lista de python que arranca en 0

        os.system('cls')
        print(maquina)
        print(maquina.recarga_existencias(cantidad, producto))
        time.sleep(3)

    # Desea salir
    elif i == 2:
        continue
       

os.system('cls')
print(maquina)
print("Hasta luego...")
