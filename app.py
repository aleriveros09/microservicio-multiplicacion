from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/multiplicar', methods=['GET'])
def multiplicar():
    try:
        # Obtenemos los parámetros de la URL
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        
        resultado = a * b
        
        return jsonify({
            "a": a,
            "b": b,
            "resultado": resultado
        })
    except (TypeError, ValueError):
        # Manejo de error si los parámetros no son números o faltan
        return jsonify({"error": "Parámetros inválidos. Asegúrate de enviar 'a' y 'b' como números."}), 400

if __name__ == '__main__':
    app.run(debug=True)
