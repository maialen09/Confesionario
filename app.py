from flask import Flask, render_template, request, jsonify
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
        cursor = conn.cursor()
        query = "SELECT COUNT(*) FROM Usuarios WHERE nombre = %s"
        cursor.execute(query, (user,))
        count = cursor.fetchone()[0]
        if(count == 0):
            query = "INSERT INTO Usuarios(nombre, contrasena) VALUES(%s, %s)"
            cursor.execute(query, (user, contrasena))
            conn.commit()
            return False
        else:
            return True
        

def obtener_usuarios_y_contrasenas():
    with mysql.connector.connect(**db_config) as conn:
        cursor = conn.cursor()
        query = "SELECT nombre, contrasena FROM Usuarios"
        cursor.execute(query)
        datos = cursor.fetchall()
        return datos


@app.route('/')
def index():
    return render_template('main.html')  # Esto buscará el archivo en /templates/index.html

@app.route('/inicio_de_sesion')
def inicio_de_sesion():
    return render_template('inicio_de_sesion.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/insertar_usuario', methods=['POST'])
def insertar_usuario():
    user = request.json['user']
    contrasena = request.json['contrasena']
    existe = anadir_usuario(user, contrasena)
    return jsonify({"existe": existe})

@app.route('/comprobar_usuario', methods= ['POST'])
def comprobar_usuario():
    user = request.json['user']
    contrasena = request.json['contrasena']
    ### comprobar si ese usuario existe
    ## comprobar si la contrseña está bien 
    usuarios = obtener_usuarios_y_contrasenas()

    
     
    for usuario in usuarios: 
       nombre = usuario[0]
       contrasenaNueva = usuario[1]
     
       if (nombre == user):
           if (contrasena == contrasenaNueva):
               return jsonify({"success": True, "message": "Usuario y contraseña correctos", "datos": usuario})
           else:
               return jsonify({"success": False, "message": "Contraseña incorrecta", "datos": usuario})
        
    return jsonify({"success": False, "message": "El usuario no existe", "datos": usuarios})       


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

