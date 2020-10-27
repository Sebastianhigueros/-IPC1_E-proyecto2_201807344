from usuario import Usuario
from Videojuego import VideoJuego
import json

class CRUD_usuario:
	#constructor
	def __init__(self):
		self.usuario = []
		self.contador = 0;

		# registro de usuarios
	def crear_usuario(self,Nombre,Apellido,nombre_usuario,Contrasena,tipo):
		for usuario in self.usuario:
			if usuario.nombre_usuario == nombre_usuario:
				return False
		self.usuario.append(Usuario(self.contador,Nombre,Apellido,nombre_usuario,Contrasena,tipo))
		print("se creo el usuario")	
		self.contador += 1
		return True

		# busqueda para inicio de sesion	
	def buscar_usuario(self,nombre_usuario,Contrasena):
		for x in self.usuario:
			if x.nombre_usuario == nombre_usuario and x.Contrasena == Contrasena :
				print("se encontro el usuario")
				return True
		return False

	def buscar_Contrasena(self,nombre_usuario):
		for usuario in self.usuario:
			if usuario.nombre_usuario == nombre_usuario :
				print(usuario.Contrasena)
				return True
		return False		

		#mostrar los usuarios del sistema	
	def listar_usuarios(self):

		return json.dumps([usuario.dump() for usuario in self.usuario])


			# modificar la informacion del usuario
	def modificar_usuario(self,nuevo_nombre,nuevo_apellido,nuevo_nombreusuario,nueva_contrasena):
		for usuario in self.usuario:
			if usuario.nombre == nuevo_nombre:
				return False
		usuario.nombre = nuevo_nombre
		usuario.apellido = nuevo_apellido
		usuario.nombre_usuario = nuevo_nombreusuario
		usuario.Contrasena = nueva_contrasena
		print('modificacion exitosa')
		return True

		# devolver juegos a la biblioteca
	def agregar_videojuego(self,ID_V,nombre_videojuego,anio,precio,categoria1,categoria2,categoria3,Foto,Banner,Descripcion):
		for usuario in self.usuario:
			if usuario.videojuegos.nombre == nombre_videojuego:
				return False
		usuario.videojuegos.append(
		VideoJuego(ID_V,nombre_videojuego,anio,precio,categoria1,categoria2,categoria3,Foto,Banner,Descripcion))	
		return True

	def listar_biblioteca(self):
		
		return json.dumps([Videojuego.dump() for videojuego in usuario.videojuegos])	
		



		