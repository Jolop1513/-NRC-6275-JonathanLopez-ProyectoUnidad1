#importar la libreria flask
from flask import Flask, redirect, request, render_template, url_for
#importamos la libreria json par poder manipular archivos de este tipo
import json
app = Flask(__name__, template_folder='templates')

#----------------------- Ruta principal ------------------
@app.route('/')
#contenedor para llamar a index.html
def index():
    return render_template('/index.html')
#----------------------- ************** ------------------
""" -------------------------------------------------------
                        Archivos json
"""
clientes = {}
""" -------------------------------------------------------
"""
""" -------------------------------------------------------
                Registro y autenticacion de usuarios
    -------------------------------------------------------
"""
# ☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼ Autenticacion ☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼
@app.route('/login')
#contenedor para llamar a login.html
def login():
    return render_template('/login.html')
# Validacion de datos
@app.route('/iniciando', methods =["GET", "POST"])
def iniciando():
    if request.method == 'POST':
        l_usuario = request.form.get('l_usuario')
        l_passwd = request.form.get('l_passwd')

        with open('clientes.json') as file:
            registrados = json.loads(file.read())
            for n in range(len(registrados)):   
              print(registrados[n]['usuario'])
            return redirect(url_for('index'))
            
    else:
      return render_template('index.html')
# ☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼
@app.route('/tienda')
#contenedor para llamar a registro.html
def tienda():
    return render_template('/tienda.html')

# ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲ Registro de usuarios ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲
@app.route('/registro')
#contenedor para llamar a registro.html
def registro():
    return render_template('/registro.html')

@app.route('/registrando', methods =["GET", "POST"])
def registrando():
    if request.method == 'POST':
        with open('clientes.json') as file:
            registrados = json.load(file)
        #Obtenemos los datos ingresados en el formulario
        id_cliente = len(registrados)
        nombre = request.form.get('nombre')
        apellido =request.form.get('apellido')
        correo = request.form.get('correo')
        usuario = request.form.get('usuario')
        contrasenia = request.form.get('contrasenia')

        clientes = {
            'id_cliente':id_cliente, 
            'nombre': nombre,
            'apellido':apellido,
            'correo': correo,
            'usuario': usuario,
            'contrasenia': contrasenia
        }
        
        registrados.append(clientes)

        with open('clientes.json', 'w') as file:
            json.dump(registrados, file)
        
        return redirect(url_for('login'))
    else:
      return render_template('login.html')
#terminado
# ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲

""" -------------------------------------------------------
                 *****************************
    -------------------------------------------------------
"""
#ejecutar
if __name__ == '__main__':
    app.run(debug=True)