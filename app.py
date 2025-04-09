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

def insertar_confesiones_falsas():
    confesiones = [
        ('anonimo1', 'Me comí la última porción de pizza y culpé a mi hermano.'),
        ('anonimo2', 'Siempre pongo cara de que entiendo, pero no tengo idea.'),
        ('anonimo3', 'Una vez fingí estar enfermo para no ir a una cita.'),
        ('anonimo4', 'Copié en un examen y aún me siento mal por eso.'),
        ('anonimo5', 'Tengo una cuenta secreta donde subo dibujos y nadie lo sabe.'),
        ('anonimo6', 'Una vez me robé una pluma del trabajo y nunca la devolví.'),
        ('anonimo7', 'Siempre me olvido de la fecha de cumpleaños de mis amigos, pero les mando un mensaje rápido al final del día.'),
        ('anonimo8', 'Dije que me gustaba una canción solo para encajar con un grupo de personas.'),
        ('anonimo9', 'Una vez fingí saber de fútbol para impresionar a un chico, aunque no tengo idea.'),
        ('anonimo10', 'Tengo una cuenta secreta en Twitter donde comparto mis pensamientos más raros.'),
        ('anonimo11', 'A veces me disfrazo de "adulto responsable", pero en realidad no sé lo que estoy haciendo.'),
        ('anonimo12', 'Me he quedado dormido en una reunión y nadie lo notó.'),
        ('anonimo13', 'Solía ponerme el uniforme de la escuela solo para no hacer tareas en casa.'),
        ('anonimo14', 'Hago compras en línea solo para luego devolver todo.'),
        ('anonimo15', 'Le dije a mi amigo que ya había visto una película, solo para no parecer fuera de onda.'),
        ('anonimo16', 'Una vez me inventé una historia para parecer interesante en una cita.'),
        ('anonimo17', 'Fingí tener una alergia para evitar comer algo que no me gustaba.'),
        ('anonimo18', 'A veces me burlo de la gente, pero luego me siento muy culpable.'),
        ('anonimo19', 'He fingido tener conocimientos sobre arte solo para que me consideren culto.'),
        ('anonimo20', 'Una vez traté de impresionar a un profesor y terminé diciendo algo totalmente incorrecto.'),
        ('anonimo21', 'No me gusta ir al gimnasio, pero siempre digo que lo hago para parecer saludable.'),
        ('anonimo22', 'A veces me siento culpable por no ser tan amable como debería.'),
        ('anonimo23', 'Me he comido el postre de alguien sin que se dieran cuenta.'),
        ('anonimo24', 'A veces me hago pasar por experto en tecnología solo para que la gente me pida consejos.'),
        ('anonimo25', 'Me siento incómodo cuando alguien me da un cumplido, por eso siempre cambio de tema.'),
        ('anonimo26', 'Fingí entender un chiste solo para no quedar mal.'),
        ('anonimo27', 'Una vez escribí un mensaje de texto para alguien y lo borré antes de enviarlo.'),
        ('anonimo28', 'Me hago pasar por organizado, pero mi cuarto está siempre un desastre.'),
        ('anonimo29', 'Una vez me olvidé el nombre de una persona y tuve que llamarla "amigo/a" por todo el día.'),
        ('anonimo30', 'Cuando me dicen que algo está rico, siempre digo que sí, aunque no me guste.'),
        ('anonimo31', 'Tengo una colección secreta de muñecos de peluche, aunque ya soy adulto.'),
        ('anonimo32', 'A veces dejo que mis amigos me cuenten problemas solo para sentirme importante.'),
        ('anonimo33', 'Una vez actué como si entendiera de vinos, aunque no me gusta ninguno.'),
        ('anonimo34', 'Mi gato es mi mejor amigo, pero nunca se lo he dicho a nadie.'),
        ('anonimo35', 'Una vez envié un correo equivocado a todo mi equipo de trabajo, pero lo ignoré.'),
        ('anonimo36', 'Me río cuando alguien hace un chiste que no entiendo, solo para no quedar mal.'),
        ('anonimo37', 'Fingí estar ocupado en el trabajo para no tener que hacer ciertas tareas.'),
        ('anonimo38', 'Una vez le dije a mi mamá que estaba en una reunión importante cuando solo estaba viendo una serie.'),
        ('anonimo39', 'Cada vez que alguien me pide una recomendación, siempre recomiendo lo primero que encuentro en Google.'),
        ('anonimo40', 'Me siento incómodo cuando tengo que hablar de mis emociones, así que prefiero no hacerlo.'),
        ('anonimo41', 'Solía decir que amaba leer libros, pero nunca lo hacía realmente.'),
        ('anonimo42', 'A veces pongo excusas para no asistir a eventos sociales, aunque en realidad solo quiero estar en casa.'),
        ('anonimo43', 'Me encanta hacer que mis amigos crean que soy muy aventurero, pero en realidad no lo soy.'),
        ('anonimo44', 'Una vez me olvidé del cumpleaños de un amigo, pero fingí que estaba esperando que me lo dijeran.'),
        ('anonimo45', 'A veces empiezo conversaciones solo para no sentirme solo, pero luego me arrepiento.'),
        ('anonimo46', 'Me hace sentir bien cuando la gente me pide consejo, aunque no siempre tenga la respuesta correcta.'),
        ('anonimo47', 'Una vez vi una película solo para poder hablar de ella con otras personas.'),
        ('anonimo48', 'Tengo miedo de que alguien descubra que nunca aprendí a montar en bicicleta.'),
        ('anonimo49', 'No me gustan los gatos, pero siempre digo que sí para encajar en la conversación.'),
        ('anonimo50', 'A veces sigo una receta solo para no decepcionar a los demás, aunque no me guste lo que cociné.')
        ]
    
    with mysql.connector.connect(**db_config) as conn:
        cursor = conn.cursor()
        query = "INSERT INTO Confesiones (usuario, texto) VALUES (%s, %s)"
        cursor.executemany(query, confesiones)
        conn.commit()

def obtener_confesiones():
    with mysql.connector.connect(**db_config) as conn:
        cursor = conn.cursor()
        query = "SELECT usuario, texto FROM Confesiones"
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
    ##insertar_confesiones_falsas()
    confesiones = obtener_confesiones()
    return render_template('home.html', confesioness = confesiones)

@app.route('/crear_confesion')
def crear_confesion():
    return render_template('crear_confesion.html')

@app.route('/conectar')
def conectar():
    return render_template('conectar.html')

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

