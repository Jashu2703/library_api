from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {"id": 1, "title": "The Alchemist", "author": "Paulo Coelho", "year": 1988},
    {"id": 2, "title": "1984", "author": "George Orwell", "year": 1949}
]

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Library API"}), 200


@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books), 200

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if book:
        return jsonify(book), 200
    return jsonify({"message": "Book not found"}), 404

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    new_book['id'] = books[-1]['id'] + 1 if books else 1
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        return jsonify({"message": "Book not found"}), 404
    data = request.get_json()
    book.update(data)
    return jsonify(book), 200

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b["id"] != book_id]
    return jsonify({"message": f"Book {book_id} deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
