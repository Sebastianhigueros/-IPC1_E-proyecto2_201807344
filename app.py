from flask import Flask, request, jsonify
from CRUD_usuario import CRUD_usuario
from CRUD_videojuegos import CRUD_videojuegos
from flask_cors import CORS
from datetime import datetime

videojuegos = CRUD_videojuegos()
Usuarios = CRUD_usuario()


Usuarios.crear_usuario('Usuario','Maestro','admin','admin','Administrador')
videojuegos.crear_Videojuego('Call of duty: Black ops 2', '2012','650', 'fps', '','', 'https://cdn.hobbyconsolas.com/sites/navi.axelspringer.es/public/styles/cover_290x414/public/media/image/2016/08/caratula-call-duty-black-ops-2.jpg','https://i.pinimg.com/originals/2b/f9/90/2bf990a4064ae797673a3a790a6dcec6.jpg','Superando las expectativas de los fans con respecto a esta franquicia que ha batido todos los récords, Call of Duty®: Black Ops II lleva a los jugadores a un futuro cercano, la Guerra Fría del siglo XXI, donde la tecnología y las armas han dado pie a una nueva generación bélica.')
videojuegos.crear_Videojuego('FIFA 18', '2017', '540' , 'deportes', '','', 'https://498930-1579140-raikfcquaxqncofqfm.stackpathdns.com/wp-content/uploads/2017/09/DJdHDgoW0AE_DTc-1.jpg','https://puregaming.es/wp-content/uploads/2018/11/fifa-18.jpg','FIFA 18 es un videojuego de fútbol, desarrollado por Electronic Arts y publicado por EA Sports Canadá y EA Sports Rumania. Es el 25.º de la serie de videojuegos de la FIFA. Salió a la venta el 29 de septiembre de 2017, siendo la portada del mismo Cristiano Ronaldo.​')



app = Flask(__name__)

CORS(app)



@app.route('/inicio_sesion', methods = ['POST'])
def inicio():

    response = {}
    usuario = request.json['nombre_usuario']
    Contrasena = request.json['Contrasena']
    busqueda =  Usuarios.buscar_usuario(usuario, Contrasena)

    if busqueda is not None:
    	return{
    		"estado": 1,
    		"datos": busqueda["tipo"],
    		"usuario": busqueda["nombre_usuario"]

    	}
    else:
    	return{
    		"estado": 0,
    		"datos": "el usuario no se encontro"

    	}	

@app.route('/Registro', methods = ['POST'])	
def registrar():

	response = {}


	nombre = request.json['nombre']
	apellido = request.json['apellido']
	usuario = request.json['nombre_usuario']
	contrasena = request.json['contrasena']
	confirmacion = request.json['confirmarcontrasena']
		
	if contrasena == confirmacion and Usuarios.crear_usuario(nombre,apellido,usuario,contrasena,"Cliente") == True:
		response["estado"] = 1
		return response
	response["estado"] = 0
	return response	

@app.route('/informacion_usuario',methods=['POST'])
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
		
	if contrasena == confirmacion and Usuarios.crear_usuario(nombre,apellido,usuario,contrasena,"Administrador") == True:
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

		response["Contrasena"] = usuario["Contrasena"]
		response["estado"] = 1
		return response
	response["estado"] = 0
	return response	


@app.route('/modificacion', methods = ['POST'])
def modificar(): 

	response = {}

	usuario = request.json['nombre_usuario']
	nombre = request.json['nuevo_nombre']
	apellido = request.json['nuevo_apellido']
	nuevousuario = request.json['nuevo_nombreusuario']
		
	modificacion = Usuarios.modificar_usuario(usuario,nombre,apellido,nuevousuario)

	if modificacion is not None :
		return {
			"estado":1,
			"usuario":modificacion['nombre_usuario']
		}


@app.route('/listar')
def listar():

	return Usuarios.listar_usuarios();

@app.route('/biblioteca')
def biblioteca() :
	usuario = request.json["nombre_usuario"]
	return 	Usuarios.listar_biblioteca(usuario)			


@app.route('/crear_videojuego', methods = ['POST'])
def crear_videojuego():
	response = {}


	
	nombre_juego = request.json["Nombre"]
	anio = request.json["Anio"]
	precio = request.json["precio"]
	cate1 = request.json["categoria1"]
	cate2 = request.json["categoria2"]
	cate3 = request.json["categoria3"]
	Foto = request.json["Foto"]
	Banner = request.json["Banner"]
	Descripcion = request.json["Descripcion"]	

	if videojuegos.crear_Videojuego(nombre_juego,anio,precio,cate1,cate2,cate3,Foto,Banner,Descripcion) == True:
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

	juego = Usuarios.agregar_videojuego(usuario,ID,juego,Anio,precio,cate1,cate2,cate3,Foto,Banner,Descripcion)
	if juego == True:
		response["estado"] = 1
		response["juego"] = juego
		return response
	response["estado"] = 0
	return response

@app.route('/pagina_juego')
def mostrar():

	ID = request.json["ID_V"]
	juego = videojuegos.mostrar_juego(ID)


	if juego is  None:
		return {
			'estado' : 0,
			'datos' : 'Juego no encontrado'

		}
		
	else:
		return {
			'datos' : juego,
			'estado': 1
		}

@app.route('/info_juego',methods=['POST'])
def buscarjuego():

	juego = request.json['Nombre']

	info = videojuegos.buscar_Videojuego(juego)

	if info is not None:

		return{

			"estado": 1,
			"datos": info
		}

	else:
		
		return {

			"estado":0,
			"datos": 'no se encontro el juego'
		}	

@app.route('/modificar_juego', methods=['POST'])
def modificarjuego():

	nombre = request.json['Nombre']
	nuevo_nombre = request.json['nuevo_Nombre']
	nuevo_anio = request.json['nuevo_Anio']
	nuevo_precio = request.json['nuevo_precio']
	nueva_cate1 = request.json['nuevo_categoria1']
	nueva_cate2 = request.json['nuevo_categoria2']
	nueva_cate3 = request.json['nuevo_categoria3']
	nueva_Foto = request.json['nuevo_Foto']
	nuevo_Banner = request.json['nuevo_Banner']
	nuevo_desc = request.json['nuevo_Descripcion']

	modificacion = videojuegos.modificar_Videojuego(nombre,nuevo_nombre,nuevo_anio,nuevo_precio,nueva_cate1,nueva_cate2,nueva_cate3,nueva_Foto,nuevo_Banner,nuevo_desc)

	if modificacion is not None:
		return{
			'estado': 1,
			'datos': modificacion
		}
	else:
		return{
			'estado': 0,
			'datos':'no se encontro el juego'
		}	


@app.route('/Eliminar_juego', methods = ['POST'])
def eliminar():

	response = {}

	Nombre_juego = request.json['Nombre']

	eliminado = videojuegos.Eliminar_Videojuego(Nombre_juego)

	if eliminado == True :
		response["estado"] = 1
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
	nombrejuego = request.json['Nombre']
	usuario = request.json['usuario']
	fecha = datetime.now()
	comentario = request.json['comentario']

	videojuegos.comentar(nombrejuego,usuario,fecha,comentario)	
	response['estado'] = 1
	return response

@app.route('/lista_comentarios', methods=['POST'])
def listar_comentarios():
	juego = request.json['Nombre']
	return videojuegos.comentarios_de_juego(juego)




@app.route('/')
def index():
	return '<h1>servidor levantado</h1>'

if __name__ == '__main__':
	app.run(threaded=True, port=1000,debug=True)