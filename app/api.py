from flask import Flask, request, jsonify
from app.reservas import verificar_disponibilidad

app = Flask(__name__)
reservas = []

@app.route('/reservar', methods=['POST'])
def reservar():
    data = request.get_json()
    disponible = verificar_disponibilidad(reservas, data)
    if disponible:
        reservas.append(data)
        return jsonify({"mensaje": "Reservada con éxito"}), 201
    else:
        # Victor Figueroa: agregar código HTTP 409 Conflict para indicar que la sala no está disponible
        return jsonify({"mensaje": "Sala no disponible"}), 409

# Victor Figueroa: Exportar explícitamente el objeto app para que sea importable en tests
__all__ = ["app"]

