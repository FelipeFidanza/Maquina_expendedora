# Máquina expendedora

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
