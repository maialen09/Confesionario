from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

db_config = {
    'user': 'admin',
    'password': 'calavera',
    'host': 'db',
    'database': 'Confesionario',
    'port': '3306'
}

def anadir_usuario(user, contrasena):
    with mysql.connector.connect(**db_config) as conn:
        cursor.conn.cursor()
        query = "SELECT COUNT(*) FROM Usuarios WHERE nombre = %s"
        cursor.execute(query, (user,))
        count = cursor.fetchone()[0]
        if(count == 0):
            query = "INSERT INTO Usuarios(nombre, contrasena) VALUES(%s, %s)"
            cursor.execute(query, (nombre, contrasena))
            conn.commit()
            return True
        else:
            return False

@app.route('/')
def index():
    return render_template('main.html')  # Esto buscará el archivo en /templates/index.html

@app.route('/insertar_usuario')
def insertar_usuario():
    user = request.json['user']
    contrasena = request.json['contrasena']
    existe = anadir_usuario(user, contrasena)
    return jsonify({"existe": existe})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

