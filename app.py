from flask import Flask, render_template, request, jsonify
from CRUD_usuario import CRUD_usuario
from CRUD_videojuegos import CRUD_videojuegos
from CRUD_comentarios import CRUD_comentarios
import json
from flask_cors import CORS

comentarios = CRUD_comentarios()
videojuegos = CRUD_videojuegos()
Usuarios = CRUD_usuario()


Usuarios.crear_usuario('Usuario','Maestro','admin','admin','Administrador')

app = Flask(__name__)

CORS(app)

@app.route('/inicio_sesion', methods=['POST'])
def inicio():
	

	if request.method == 'POST':

		response = {}

		nombre_usuario = request.form.get('nombre_usuario')
		Contrasena = request.form.get('Contrasena')


		if Usuarios.buscar_usuario(nombre_usuario,Contrasena) == True :
			response["estado"] = 1
			return response
			
		response["estado"] = 0
		return response

@app.route('/Registro', methods = ['POST'])	
def registrar():

	response = {}

	if request.method == 'POST':
		nombre = request.form.get('nombre')
		apellido = request.form.get('apellido')
		usuario = request.form.get('nombre_usuario')
		contrasena = request.form.get('contrasena')
		
		if Usuarios.crear_usuario(nombre,apellido,usuario,contrasena,"cliente") == True:
			response["estado"] == 1
		response["estado"] = 0
		return response	



@app.route('/Recuperar', methods =['GET'])
def recuperar_contrasena():
	response = {}

	if request.method == 'GET':
		Nombre_usuario = request.args.get("Nombre_usuario", None)

		usuario = Usuarios.buscar_usuario(Nombre_usuario)

		if usuario == None:
			response["estado"] = 0
		else:
			response["estado"] = 1	
			response["Contrasena"] = usuario.Contrasena

	return response

@app.route('/crear_videojuego', methods = ['POST'])
def crear_videojuego():
	response = {}

	if request.method == 'POST':
		nombre_juego = request.form.get('nombre')
		anio = request.form.get('Anio')
		precio = request.form.get('precio')
		cate1 = request.form.get('categoria1')
		cate2 = request.form.get('categoria2')
		cate3 = request.form.get('categoria3')
		Foto = request.form.get('Foto')
		Banner = request.form.get('Banner')
		Descripcion = request.form.get('Descripcion')	

		if videojuegos.crear_videojuego(nombre_juego,anio,cate1,cate2,cate3,Foto,Banner,Descripcion) == True:
			response['estado'] = 1
		response['estado'] = 0
		return response	

@app.route('/agregar_Videojuego', methods = ['POST'])
def agregar():
	
	response = {}

	if request.method == 'POST':
		ID = request.form.get('ID')
		juego = request.form.get('Nombre')
		Anio = request.form.get('Anio')
		precio = request.form.get('precio')
		cate1 = request.form.get('categoria1')
		cate2 = request.form.get('categoria2')
		cate3 = request.form.get('categoria3')
		Foto = request.form.get('Foto')
		Banner = request.form.get('Banner')
		Descripcion = request.form.get('Descripcion')
		if Usuarios.agregar_Videojuego(ID,juego,Anio,precio,cate1,cate2,cate3,Foto,Banner,Descripcion) == True:
			response['estado'] = 1
		response['estado'] = 0
		return response

	@app.route('/pagina_juego', methods = ['POST'])
	def mostrar():
		response = {}

		if request.method == 'POST':
			Nombre = request.form.get('Nombre')

			juego = videojuegos.mostrar_juegos(Nombre)

			if juegos is not None:

				return {
					'datos' : juego,
					'estado': 1
				}
			else :

				return {
					'estado' : 0,
					'datos' : 'Juego encontrado'

				}
				




	@app.route('/cargar', methods == 'POST')
	def carga():
		response = {}

		if request.method == 'POST':
			Ruta = request.form.get('ruta')

		if videojuegos.lectura_de_archivo(Ruta) == True:
			response['estado'] = 1
		response ['estado'] = 0
		return response


	@app.route('/comentar', methods == 'POST')
	def comentar():
		response = {}

		if request.method == 'POST':
			usuario = request.form.get('usuario')
			fecha = request.form.get('fecha')
			comentario = request.form.get('comentario')

			if comentarios.comentar(usaurio,comentario) == True:
				response['estado'] = 1
			response['estado'] = 0
			return response					



@app.route("/<name>")
def index(name):
	return render_template("paginaPrincipal.html",name = "paginaPrincipal") 

if __name__ == '__main__':
	app.run(threaded=True, port=1000,debug=True)