from flask import Flask, jsonify
from maquina_expendedora_ICS import MaquinaExpendedora

app = Flask(__name__)

existencias = [
    [24, 7, 6, 7, 5, 2, 4], # Galletitas $24
    [15, 5, 5, 2, 7, 4, 6], # Alfajor $15
    [8, 6, 1, 7, 3, 5, 3], # Chicle $8
    [37, 4, 3, 7, 4, 5, 1], # Chips $37
    [45, 7, 6, 7, 7, 4, 5] # Coca-cola $45
]
maquina = MaquinaExpendedora(existencias)

@app.route("/")
def home():
    return str(maquina).replace("\n", "<br>")

@app.route("/comprar/<fila>/<int:col>/<int:cant1>/<int:cant2>/<int:cant5>/<int:cant10>")
def comprar(fila, col, cant1, cant2, cant5, cant10):
    billetes = [cant1, cant2, cant5, cant10]
    if not maquina.comprueba_billetes(billetes):
        return jsonify({"error": "No se pudo procesar el dinero. Exceso de billetes."}), 400
    
    fila_num = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}.get(fila.upper())
    if fila_num is None or not (1 <= col <= 6):
        return jsonify({"error": "Fila o columna invalida"}), 400

    maquina.buscar_existencias(fila_num, col)
    vuelto = maquina.devuelve_vuelto(fila_num)
    return str(maquina).replace("\n", "<br>") + f"\nCompra procesada. Su vuelto es de ${vuelto}"


@app.route("/recargar/<int:cantidad>/<producto>")
def recargar(cantidad, producto):
    producto = {"GALLETITAS": 0, "ALFAJOR": 1, "CHICLE": 2, "CHIPS": 3, "COCA-COLA": 4}.get(producto.upper())
    maquina.recarga_existencias(cantidad, producto)
    return str(maquina).replace("\n", "<br>") + "\nRecarga realizada."

if __name__ == "__main__":
    app.run()
