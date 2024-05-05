from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Mock database for to-dos
todos = [
    {"id": "1", "title": "Grocery Shopping", "description": "Buy milk, eggs, and bread."},
    {"id": "2", "title": "Workout", "description": "Go for a 30-minute run."}
]

@app.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/api/todos', methods=['POST'])
def create_todo():
    if not request.json or not 'title' in request.json:
        abort(400)
    todo = {
        'id': str(len(todos) + 1),
        'title': request.json['title'],
        'description': request.json.get('description', "")
    }
    todos.append(todo)
    return jsonify(todo), 201

@app.route('/api/todos/<string:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((todo for todo in todos if todo['id'] == todo_id), None)
    if todo is None:
        abort(404)
    return jsonify(todo)

@app.route('/api/todos/<string:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((todo for todo in todos if todo['id'] == todo_id), None)
    if todo is None:
        abort(404)
    if not request.json:
        abort(400)
    todo['title'] = request.json.get('title', todo['title'])
    todo['description'] = request.json.get('description', todo['description'])
    return jsonify(todo)

@app.route('/api/todos/<string:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todo = next((todo for todo in todos if todo['id'] == todo_id), None)
    if todo is None:
        abort(404)
    todos = [todo for todo in todos if todo['id'] != todo_id]
    return jsonify({}), 204

if __name__ == '__main__':
    app.run(debug=True)
