from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulando um banco de dados em memória
contacts = []

# Rota para a URL raiz
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Contact Manager API!"}), 200

# Rota para listar todos os contatos
@app.route('/contacts', methods=['GET'])
def get_contacts():
    return jsonify(contacts), 200

# Rota para criar um novo contato
@app.route('/contacts', methods=['POST'])
def create_contact():
    data = request.get_json()
    if not data or not all(k in data for k in ('name', 'email', 'phone')):
        return jsonify({"error": "Missing fields. 'name', 'email', and 'phone' are required."}), 400

    new_contact = {
        'id': len(contacts) + 1,
        'name': data['name'],
        'email': data['email'],
        'phone': data['phone']
    }
    contacts.append(new_contact)
    return jsonify(new_contact), 201

# Rota para obter detalhes de um contato específico
@app.route('/contacts/<int:contact_id>', methods=['GET'])
def get_contact(contact_id):
    contact = next((c for c in contacts if c['id'] == contact_id), None)
    if not contact:
        return jsonify({"error": "Contact not found."}), 404
    return jsonify(contact), 200

# Rota para atualizar um contato
@app.route('/contacts/<int:contact_id>', methods=['PUT'])
def update_contact(contact_id):
    data = request.get_json()
    contact = next((c for c in contacts if c['id'] == contact_id), None)
    if not contact:
        return jsonify({"error": "Contact not found."}), 404

    contact.update({
        'name': data.get('name', contact['name']),
        'email': data.get('email', contact['email']),
        'phone': data.get('phone', contact['phone'])
    })
    return jsonify(contact), 200

# Rota para deletar um contato
@app.route('/contacts/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    global contacts
    contacts = [c for c in contacts if c['id'] != contact_id]
    return jsonify({"message": "Contact deleted successfully."}), 200

if __name__ == '__main__':
    app.run(debug=True)
