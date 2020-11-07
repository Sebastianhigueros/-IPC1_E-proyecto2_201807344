from flask import Flask, request, jsonify
from CRUD_usuario import CRUD_usuario
from CRUD_videojuegos import CRUD_videojuegos
from flask_cors import CORS
from datetime import datetime

videojuegos = CRUD_videojuegos()
Usuarios = CRUD_usuario()


Usuarios.crear_usuario('Usuario','Maestro','admin','admin','Administrador')
videojuegos.crear_Videojuego('Call of duty: Black ops 2', '2012','650', 'fps', '','', 'https://images.app.goo.gl/u3jJFcBXmdDCbth9A','https://images.app.goo.gl/HBQzXUbVia3T5Ris5','Superando las expectativas de los fans con respecto a esta franquicia que ha batido todos los récords, Call of Duty®: Black Ops II lleva a los jugadores a un futuro cercano, la Guerra Fría del siglo XXI, donde la tecnología y las armas han dado pie a una nueva generación bélica.')
videojuegos.crear_Videojuego('FIFA 18', '2017', '540' , 'deportes', '','', 'https://images.app.goo.gl/NqYnBr1gVC88aSRq9','https://images.app.goo.gl/xkfniusoJfxP3wo47','FIFA 18 es un videojuego de fútbol, desarrollado por Electronic Arts y publicado por EA Sports Canadá y EA Sports Rumania. Es el 25.º de la serie de videojuegos de la FIFA. Salió a la venta el 29 de septiembre de 2017, siendo la portada del mismo Cristiano Ronaldo.​')




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
	confirmacion = request.json['confirmarcontrasena']
		
	if contrasna == confirmacion and Usuarios.crear_usuario(nombre,apellido,usuario,contrasena,"Cliente") == True:
		response["estado"] = 1
		return response
	response["estado"] = 0
	return response	

@app.route('/informacion_usuario')
def info():

	usuario = request.json['nombre_usuario']

	informacion = Usuarios.mostrar_usuario(usuario)

	if informacion is not None:

		return {
			"datos": informacion,
			"estado" : 1
		}
	else:
		return {
			"datos" : "no se encontro el usuario",
			"estado" : 0
		}	 


@app.route('/Registro_administrador', methods = ['POST'])	
def registraradmin():

	response = {}


	nombre = request.json['nombre']
	apellido = request.json['apellido']
	usuario = request.json['nombre_usuario']
	contrasena = request.json['contrasena']
	confirmacion = request.json['confirmarcontrasena']
		
	if contrasna == confirmacion and Usuarios.crear_usuario(nombre,apellido,usuario,contrasena,"Administrador") == True:
		response["estado"] = 1
		return response
	response["estado"] = 0
	return response	


@app.route('/Recuperar', methods =['POST'])
def recuperar_contrasena():
	response = {}

	Nombre_usuario = request.json["nombre_usuario"]

	usuario = Usuarios.buscar_Contrasena(Nombre_usuario)

	if usuario is not None:

		response["Contrasena"] = usuario.Contrasena
		response["estado"] = 1
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

	usuario = request.json['nombre_usuario']
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

	ID = request.json['ID']

	juego = videojuegos.mostrar_juego(ID)

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


@app.route('/buscar_juegos')
def buscar():

	response = {}

	Nombre_juego = request.json['Nombre']

	buscado = videojuegos.buscar_Videojuego(Nombre_juego)

	if buscado is not None:
		response['estado'] = 1
		return response
	response['estado'] = 0
	return response	

@app.route('/categorias', methods=['POST'])
def cate():

	response = {}
	categoria = request.json['Categoria']
	juegos = videojuegos.buscar_categoria(categoria)


	if juegos is not None:
		response['estado'] = 1
		response['datos'] = juegos
		return response
	response['estado'] = 0
	return response	


@app.route('/comentar', methods = ['POST'])
def comentar():
	response = {}

	usuario = request.json['usuario']
	fecha = datetime.now()
	comentario = request.json['comentario']

	videojuegos.comentar(usuario,fecha,comentario)	
	response['estado'] = 1
	return response



@app.route('/')
def index():
	return '<h1>servidor levantado</h1>'

if __name__ == '__main__':
	app.run(threaded=True, port=1000,debug=True)