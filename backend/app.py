from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB_PATH = 'data.sqlite'

# Criar tabela se não existir
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/save', methods=['POST'])
def save_text():
    data = request.json
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO entries (text) VALUES (?)', (text,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Text saved'})

@app.route('/entries', methods=['GET'])
def get_entries():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM entries')
    rows = cursor.fetchall()
    conn.close()
    return jsonify([{'id': r[0], 'text': r[1]} for r in rows])

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
