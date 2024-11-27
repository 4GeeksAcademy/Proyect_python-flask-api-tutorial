from flask import Flask, jsonify
from flask import request

# Crear una instancia de Flask
app = Flask(__name__)

# Variable global 'todos' que contiene la lista de tareas
todos = [
    { "label": "My first task", "done": False }
]

# Definir el endpoint "/todos"
@app.route('/todos', methods=['GET'])
def get_todos():
    # Retornar los datos en formato JSON usando jsonify
    return jsonify(todos)


# Endpoint POST para agregar una nueva tarea a la lista 'todos'
@app.route('/todos', methods=['POST'])
def add_new_todo():
    # Capturar el cuerpo de la solicitud como un diccionario de Python
    request_body = request.json
    print("Incoming request with the following body", request_body)

    # Agregar el nuevo 'todo' a la lista global
    todos.append(request_body)

    return jsonify(todos)


# Endpoint DELETE para borrar una tarea de la lista 'todos'
# @app.route('/todos/<int:position>', methods=['DELETE'])
# def delete_todo(position):
#     print("This is the position to delete:", position)
#     return 'something'
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    return jsonify(todos), 200

    # if 0 <= position < len(todos):
    #     todos.pop(position)
    #     return jsonify(todos), 200  # Código 200 indica que la eliminación fue exitosa
    # else:
    #     # Si la posición no es válida, retornar un error 404
    #     return jsonify({"error": "Invalid position"}), 404





# Asegúrate de que estas líneas estén al final
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
