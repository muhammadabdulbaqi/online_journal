from flask import Flask, jsonify, request
from database import db_utils


app = Flask(__name__)

@app.route('/api/entries', methods=['GET'])
def get_entries():
    entries = db_utils.get_all_entries()
    result = [
        {
            "id": entry[0],
            "title": entry[1],
            "content": entry[2],
            "created_at": entry[3]
        }
        for entry in entries
    ]
    return jsonify(result), 200

@app.route('/api/entries/<int:entry_id>', methods=['GET'])
def get_entry(entry_id):
    entry = db_utils.get_entry(entry_id)
    if entry:
        result = {
            "id": entry[0],
            "title": entry[1],
            "content": entry[2],
            "created_at": entry[3]
        }
        return jsonify(result), 200       
    return jsonify({"error": "Entry not found"}), 404

@app.route('/api/entries', methods=['POST'])
def create_entry():
    data = request.get_json()
    title = data.get("title")
    content = data.get("content")

    if not title or not content:
        return jsonify({"error": "Missing title or content"}), 400

    db_utils.create_entry(title, content)
    return jsonify({"message": "Entry created"}), 201

@app.route('/api/entries/<int:entry_id>', methods=['PUT'])
def update_entry(entry_id):
    data = request.get_json()
    title = data.get("title")
    content = data.get("content")

    if not title or not content:
        return jsonify({"error": "Missing title or content"}), 400

    db_utils.update_entry(entry_id, title, content)
    return jsonify({"message": "Entry updated"}), 200

@app.route('/api/entries/<int:entry_id>', methods=['DELETE'])
def delete_entry(entry_id):
    db_utils.delete_entry(entry_id)
    return jsonify({"message": "Entry deleted"}), 204

if __name__ == '__main__':
    db_utils.init_db()  
    app.run(debug=True, port=5000)
