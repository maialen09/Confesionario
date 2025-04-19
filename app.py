from flask import Flask, render_template, request, jsonify, session
from flask_session import Session
import mysql.connector

app = Flask(__name__)

app.secret_key = 'mi_clave_secreta_super_segura'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

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

def anadir_confesion(titulo, confesion):
    with mysql.connector.connect(**db_config) as conn:
        cursor = conn.cursor()
        query = "INSERT INTO Confesiones(titulo, usuario, texto) VALUES(%s, %s, %s)"
        cursor.execute(query, (titulo, session.get('usuario'), confesion))
        conn.commit()
        return True
        

def obtener_usuarios_y_contrasenas():
    with mysql.connector.connect(**db_config) as conn:
        cursor = conn.cursor()
        query = "SELECT nombre, contrasena FROM Usuarios"
        cursor.execute(query)
        datos = cursor.fetchall()
        return datos

def obtener_confesion_por_id(id):
    with mysql.connector.connect(**db_config) as conn:
        cursor = conn.cursor()
        query = "SELECT titulo, texto, usuario FROM Confesiones WHERE id=%s"
        cursor.execute(query, (id,))
        datos = cursor.fetchall()
        return datos
    
def insertar_comentarios(textoComentario,idConfesion,usuario):
    with mysql.connector.connect(**db_config) as conn:
        cursor = conn.cursor()
        query = "INSERT INTO Comentarios(id_confesion,usuario,texto) VALUES (%s, %s, %s)"
        cursor.execute(query, (idConfesion,usuario,textoComentario))
        conn.commit()
        return True
    

def sumar_like(usuario,comentario_id): 
    with mysql.connector.connect(**db_config) as conn:
        cursor = conn.cursor()
        query = "INSERT INTO Likes(usuario, comentario_id) VALUES (%s,%s)"
        cursor.execute(query, (usuario, comentario_id))
        conn.commit()
        return True
    

def insertar_confesiones_falsas():
    confesiones = [
        ('anonimo1', 'Confesión pizzera', 'Me comí la última porción de pizza y culpé a mi hermano.'),
        ('anonimo2', 'Cara de sabio', 'Siempre pongo cara de que entiendo, pero no tengo idea.'),
        ('anonimo3', 'Excusa para zafarme', 'Una vez fingí estar enfermo para no ir a una cita.'),
        ('anonimo4', 'Culpable del 10', 'Copié en un examen y aún me siento mal por eso.'),
        ('anonimo5', 'Artista secreto', 'Tengo una cuenta secreta donde subo dibujos y nadie lo sabe.'),
        ('anonimo6', 'Pequeño hurto', 'Una vez me robé una pluma del trabajo y nunca la devolví.'),
        ('anonimo7', 'Olvidos amistosos', 'Siempre me olvido de la fecha de cumpleaños de mis amigos, pero les mando un mensaje rápido al final del día.'),
        ('anonimo8', 'Música por encajar', 'Dije que me gustaba una canción solo para encajar con un grupo de personas.'),
        ('anonimo9', 'Fútbol fingido', 'Una vez fingí saber de fútbol para impresionar a un chico, aunque no tengo idea.'),
        ('anonimo10', 'Pensamientos secretos', 'Tengo una cuenta secreta en Twitter donde comparto mis pensamientos más raros.'),
        ('anonimo11', 'Actuando de adulto', 'A veces me disfrazo de "adulto responsable", pero en realidad no sé lo que estoy haciendo.'),
        ('anonimo12', 'Sueño laboral', 'Me he quedado dormido en una reunión y nadie lo notó.'),
        ('anonimo13', 'Uniforme estratégico', 'Solía ponerme el uniforme de la escuela solo para no hacer tareas en casa.'),
        ('anonimo14', 'Compras de mentira', 'Hago compras en línea solo para luego devolver todo.'),
        ('anonimo15', 'Mentira cinéfila', 'Le dije a mi amigo que ya había visto una película, solo para no parecer fuera de onda.'),
        ('anonimo16', 'Historia inventada', 'Una vez me inventé una historia para parecer interesante en una cita.'),
        ('anonimo17', 'Alergia falsa', 'Fingí tener una alergia para evitar comer algo que no me gustaba.'),
        ('anonimo18', 'Burla y culpa', 'A veces me burlo de la gente, pero luego me siento muy culpable.'),
        ('anonimo19', 'Culto fingido', 'He fingido tener conocimientos sobre arte solo para que me consideren culto.'),
        ('anonimo20', 'Fail académico', 'Una vez traté de impresionar a un profesor y terminé diciendo algo totalmente incorrecto.'),
        ('anonimo21', 'Gimnasio fantasma', 'No me gusta ir al gimnasio, pero siempre digo que lo hago para parecer saludable.'),
        ('anonimo22', 'Culpa leve', 'A veces me siento culpable por no ser tan amable como debería.'),
        ('anonimo23', 'Postre robado', 'Me he comido el postre de alguien sin que se dieran cuenta.'),
        ('anonimo24', 'Tecno-farsante', 'A veces me hago pasar por experto en tecnología solo para que la gente me pida consejos.'),
        ('anonimo25', 'Incómodo con elogios', 'Me siento incómodo cuando alguien me da un cumplido, por eso siempre cambio de tema.'),
        ('anonimo26', 'Risa fingida', 'Fingí entender un chiste solo para no quedar mal.'),
        ('anonimo27', 'Mensaje fantasma', 'Una vez escribí un mensaje de texto para alguien y lo borré antes de enviarlo.'),
        ('anonimo28', 'Desorden oculto', 'Me hago pasar por organizado, pero mi cuarto está siempre un desastre.'),
        ('anonimo29', 'Amigo sin nombre', 'Una vez me olvidé el nombre de una persona y tuve que llamarla "amigo/a" por todo el día.'),
        ('anonimo30', 'Mentira culinaria', 'Cuando me dicen que algo está rico, siempre digo que sí, aunque no me guste.'),
        ('anonimo31', 'Ternura escondida', 'Tengo una colección secreta de muñecos de peluche, aunque ya soy adulto.'),
        ('anonimo32', 'Escucha egoísta', 'A veces dejo que mis amigos me cuenten problemas solo para sentirme importante.'),
        ('anonimo33', 'Mentira vinera', 'Una vez actué como si entendiera de vinos, aunque no me gusta ninguno.'),
        ('anonimo34', 'Amor felino secreto', 'Mi gato es mi mejor amigo, pero nunca se lo he dicho a nadie.'),
        ('anonimo35', 'Error ignorado', 'Una vez envié un correo equivocado a todo mi equipo de trabajo, pero lo ignoré.'),
        ('anonimo36', 'Risa por compromiso', 'Me río cuando alguien hace un chiste que no entiendo, solo para no quedar mal.'),
        ('anonimo37', 'Ocupado ficticio', 'Fingí estar ocupado en el trabajo para no tener que hacer ciertas tareas.'),
        ('anonimo38', 'Excusa con Netflix', 'Una vez le dije a mi mamá que estaba en una reunión importante cuando solo estaba viendo una serie.'),
        ('anonimo39', 'Recomendación improvisada', 'Cada vez que alguien me pide una recomendación, siempre recomiendo lo primero que encuentro en Google.'),
        ('anonimo40', 'Emociones bloqueadas', 'Me siento incómodo cuando tengo que hablar de mis emociones, así que prefiero no hacerlo.'),
        ('anonimo41', 'Lector imaginario', 'Solía decir que amaba leer libros, pero nunca lo hacía realmente.'),
        ('anonimo42', 'Excusas sociales', 'A veces pongo excusas para no asistir a eventos sociales, aunque en realidad solo quiero estar en casa.'),
        ('anonimo43', 'Aventurero de palabra', 'Me encanta hacer que mis amigos crean que soy muy aventurero, pero en realidad no lo soy.'),
        ('anonimo44', 'Olvido disimulado', 'Una vez me olvidé del cumpleaños de un amigo, pero fingí que estaba esperando que me lo dijeran.'),
        ('anonimo45', 'Conversaciones vacías', 'A veces empiezo conversaciones solo para no sentirme solo, pero luego me arrepiento.'),
        ('anonimo46', 'Consejero inseguro', 'Me hace sentir bien cuando la gente me pide consejo, aunque no siempre tenga la respuesta correcta.'),
        ('anonimo47', 'Cine por presión', 'Una vez vi una película solo para poder hablar de ella con otras personas.'),
        ('anonimo48', 'Bici secreta', 'Tengo miedo de que alguien descubra que nunca aprendí a montar en bicicleta.'),
        ('anonimo49', 'Gato por cortesía', 'No me gustan los gatos, pero siempre digo que sí para encajar en la conversación.'),
        ('anonimo50', 'Receta fingida', 'A veces sigo utitulona receta solo para no decepcionar a los demás, aunque no me guste lo que cociné.')
    ]

    
    with mysql.connector.connect(**db_config) as conn:
        cursor = conn.cursor()
        query = "INSERT INTO Confesiones (usuario, titulo, texto) VALUES (%s, %s, %s)"
        cursor.executemany(query, confesiones)
        conn.commit()

def obtener_confesiones():
    with mysql.connector.connect(**db_config) as conn:
        cursor = conn.cursor()
        query = "SELECT usuario, titulo, texto, id FROM Confesiones"
        cursor.execute(query)
        datos = cursor.fetchall()
        return datos
    
def obtener_confesiones_usuario(usuario):
    with mysql.connector.connect(**db_config) as conn:
        cursor = conn.cursor()
        query = "SELECT titulo,texto,id FROM Confesiones WHERE usuario= %s"
        cursor.execute(query, (usuario,))
        datos = cursor.fetchall()
        return datos


    

def obtener_comentarios(id_confesion):
    with mysql.connector.connect(**db_config) as conn:
        cursor = conn.cursor()
        query = """
        SELECT 
            c.usuario, 
            c.texto, 
            c.id, 
            (
                SELECT COUNT(*) 
                FROM Likes l 
                WHERE l.comentario_id = c.id
            ) AS num_likes
        FROM Comentarios c
        WHERE c.id_confesion = %s
        """
        cursor.execute(query, (id_confesion,))
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
    #### insertar_confesiones_falsas() # Comentar esto
    confesiones = obtener_confesiones()
    return render_template('home.html', confesioness = confesiones, usuario = session.get('usuario'))

@app.route('/crear_confesion')
def crear_confesion():
    return render_template('crear_confesion.html')

@app.route('/conectar')
def conectar():
    return render_template('conectar.html')
    

@app.route('/mis_confesiones')
def mis_confesiones():
    confesiones = obtener_confesiones_usuario(session.get('usuario'))
    return render_template('mis_confesiones.html', confesiones=confesiones)

@app.route('/confesion/<int:id>')
def ver_confesion(id):
    datos = obtener_confesion_por_id(id)
    comments = obtener_comentarios(id)
    return render_template('confesion.html', id=id, datos=datos, comments=comments)


@app.route('/insertar_usuario', methods=['POST'])
def insertar_usuario():
    user = request.json['user']
    contrasena = request.json['contrasena']
    existe = anadir_usuario(user, contrasena)
    return jsonify({"existe": existe})

@app.route('/insertar_confesion', methods=['POST'])
def insertar_confesion():
    titulo = request.json['title']
    confesion = request.json['conf']
    existe = anadir_confesion(titulo, confesion)
    return jsonify({"existe": existe})

@app.route('/insertar_comentario', methods=['POST'])
def insertar_comentario():
    textoComentario = request.json['textoComentario']
    idConfesion = request.json['idConfesion']
    resultado = insertar_comentarios(textoComentario,idConfesion, session.get('usuario'))
    return jsonify({"resultado": resultado})


@app.route('/incrementar_like', methods=['POST'])
def incrementar_like():
    idComentario = request.json['idComentario']
    resultado = sumar_like(session.get('usuario'), idComentario)
    return jsonify({"resultado": resultado})



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
               session['usuario'] = user
               return jsonify({"success": True, "message": "Usuario y contraseña correctos", "datos": usuario})
           else:
               return jsonify({"success": False, "message": "Contraseña incorrecta", "datos": usuario})
        
    return jsonify({"success": False, "message": "El usuario no existe", "datos": usuarios})      

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

