from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for demonstration purposes
data_store = {}


@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data_store)


@app.route('/data/<key>', methods=['GET'])
def get_data_by_key(key):
    if key in data_store:
        return jsonify({key: data_store[key]})
    else:
        return jsonify({"error": "Key not found"}), 404


@app.route('/data', methods=['POST'])
def add_data():
    if request.is_json:
        data = request.get_json()
        data_store.update(data)
        return jsonify(data), 201
    else:
        return jsonify({"error": "Request must be JSON"}), 400


@app.route('/data/<key>', methods=['PUT'])
def update_data(key):
    if request.is_json:
        data = request.get_json()
        if key in data_store:
            data_store[key] = data.get('value', data_store[key])
            return jsonify({key: data_store[key]})
        else:
            return jsonify({"error": "Key not found"}), 404
    else:
        return jsonify({"error": "Request must be JSON"}), 400


@app.route('/data/<key>', methods=['DELETE'])
def delete_data(key):
    if key in data_store:
        del data_store[key]
        return jsonify({"message": "Key deleted"}), 200
    else:
        return jsonify({"error": "Key not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
