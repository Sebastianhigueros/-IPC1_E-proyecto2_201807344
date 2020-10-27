from flask import Flask, request, jsonify
from CRUD_usuario import CRUD_usuario
from CRUD_videojuegos import CRUD_videojuegos
from CRUD_comentarios import CRUD_comentarios
from flask_cors import CORS

comentarios = CRUD_comentarios()
videojuegos = CRUD_videojuegos()
Usuarios = CRUD_usuario()


Usuarios.crear_usuario('Usuario','Maestro','admin','admin','Administrador')



app = Flask(__name__)

CORS(app)



@app.route('/inicio_sesion', methods = ['POST'])
def inicio():

    response = {}

    usuario = request.json['nombre_usuario']
    Contrasena = request.json['Contrasena']

    busqueda =  Usuarios.buscar_usuario(usuario, Contrasena)
    if busqueda == True:
    	response["estado"] = 1
    	return response

    response["estado"] = 0
    return response

@app.route('/Registro', methods = ['POST'])	
def registrar():

	response = {}


	nombre = request.json['nombre']
	apellido = request.json['apellido']
	usuario = request.json['nombre_usuario']
	contrasena = request.json['contrasena']
		
	if Usuarios.crear_usuario(nombre,apellido,usuario,contrasena,"cliente") == True:
		response["estado"] = 1
		return response
	response["estado"] = 0
	return response	



@app.route('/Recuperar', methods =['POST'])
def recuperar_contrasena():
	response = {}

	Nombre_usuario = request.json["Nombre_usuario"]

	usuario = Usuarios.buscar_Contrasena(Nombre_usuario)

	if usuario == True:
		response["estado"] = 1
		response["Contrasena"] = usuario.Contrasena
		return response
	
	response["estado"] = 0
	return response



@app.route('/modificacion', methods = ['POST'])
def modificar(): 

	response = {}

	nombre = request.json['nuevo_nombre']
	apellido = request.json['nuevo_apellido']
	usuario = request.json['nuevo_nombreusuario']
	contrasena = request.json['nueva_contrasena']  
		
	modificacion = Usuarios.modificar_usuario(nombre,apellido,usuario,contrasena)

	if modificacion is not False :
		response["estado"] = 1
		return response
	response["estado"] = 0	
	return response


@app.route('/listar')
def listar():

	return Usuarios.listar_usuarios();

@app.route('/biblioteca')
def biblioteca() :
	
	return 	Usuarios.listar_biblioteca()			


@app.route('/crear_videojuego', methods = ['POST'])
def crear_videojuego():
	response = {}


	
	nombre_juego = request.json['nombre']
	anio = request.json['Anio']
	precio = request.json['precio']
	cate1 = request.json['categoria1']
	cate2 = request.json['categoria2']
	cate3 = request.json['categoria3']
	Foto = request.json['Foto']
	Banner = request.json['Banner']
	Descripcion = request.json['Descripcion']	

	if videojuegos.crear_videojuego(nombre_juego,anio,cate1,cate2,cate3,Foto,Banner,Descripcion) == True:
		response["estado"] = 1
		return response
	response["estado"] = 0
	return response	


@app.route('/agregar_Videojuego', methods = ['POST'])
def agregar():
	
	response = {}


	ID = request.json['ID']
	juego = request.json['Nombre']
	Anio = request.json['Anio']
	precio = request.json['precio']
	cate1 = request.json['categoria1']
	cate2 = request.json['categoria2']
	cate3 = request.json['categoria3']
	Foto = request.json['Foto']
	Banner = request.json['Banner']
	Descripcion = request.json['Descripcion']


	if Usuarios.agregar_videojuego(ID,juego,Anio,precio,cate1,cate2,cate3,Foto,Banner,Descripcion) == True:
		response["estado"] = 1
		return response
	response["estado"] = 0
	return response

@app.route('/pagina_juego', methods = ['POST'])
def mostrar():
	response = {}

	Nombre = request.json['Nombre']

	juego = videojuegos.mostrar_juego(Nombre)

	if juego is not None:

		return {
					'datos' : juego,
					'estado': 1
		}
	else :

		return {
					'estado' : 0,
					'datos' : 'Juego no encontrado'

		}
				




@app.route('/cargar', methods = ['POST'])
def carga():
	response = {}


	Ruta = request.json['ruta']

	if videojuegos.lectura_de_archivo(Ruta) == True:
		response["estado"] = 1
	response ["estado"] = 0
	return response


@app.route('/Eliminar_juego', methods = ['POST'])
def eliminar():

	response = {}

	Nombre_juego = request.json['Nombre']

	eliminado = videojuegos.Eliminar_Videojuego(Nombre_juego)

	if eliminado == True :
		respose["estado"] = 1
		return response
	response["estado"] = 0
	return response


@app.route('/listar_juegos')
def lista():

	return videojuegos.lista_videojuegos()





@app.route('/comentar', methods = ['POST'])
def comentar():
	response = {}

	usuario = request.json['usuario']
	fecha = request.json['fecha']
	comentario = request.json['comentario']

	if comentarios.comentar(usaurio,comentario) == True:
		response["estado"] = 1
		return response
	response["estado"] = 0
	return response					



@app.route('/')
def index(name):
	return '<h1>servidor levantado</h1>'

if __name__ == '__main__':
	app.run(threaded=True, port=1000,debug=True)