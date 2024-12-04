from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory database
items = {}

# GET all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# GET item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = items.get(item_id)
    if item is None:
        abort(404, description="Item not found")
    return jsonify({item_id: item})

# POST (create new item)
@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or 'name' not in request.json:
        abort(400, description="Invalid request")
    item_id = len(items) + 1
    items[item_id] = request.json['name']
    return jsonify({item_id: items[item_id]}), 201

# PUT (update existing item)
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    if item_id not in items:
        abort(404, description="Item not found")
    if not request.json or 'name' not in request.json:
        abort(400, description="Invalid request")
    items[item_id] = request.json['name']
    return jsonify({item_id: items[item_id]})

# DELETE item by ID
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id not in items:
        abort(404, description="Item not found")
    del items[item_id]
    return jsonify({"result": "Item deleted"})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
