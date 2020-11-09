from usuario import Usuario
from Videojuego import VideoJuego
import json

class CRUD_usuario:
	#constructor
	def __init__(self):
		self.usuario = []
		self.contador = 0
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
				return x.dump()
		return None

	def buscar_Contrasena(self,nombre_usuario):
		for usuario in self.usuario:
			if usuario.nombre_usuario == nombre_usuario :
				return usuario.dump()
		return None	

	def mostrar_usuario(self,nombre_usuario):
		for usuario in self.usuario:
			if usuario.nombre_usuario == nombre_usuario:
				return usuario.dump()
			return None			
			
		#mostrar los usuarios del sistema	
	def listar_usuarios(self):

		return json.dumps([usuario.dump() for usuario in self.usuario])


			# modificar la informacion del usuario
	def modificar_usuario(self,nombre_usuario,nuevo_nombre,nuevo_apellido,nuevo_nombreusuario):
		for usuario in self.usuario:
			if usuario.nombre_usuario == nombre_usuario:
				usuario.Nombre = nuevo_nombre
				usuario.Apellido = nuevo_apellido
				usuario.nombre_usuario = nuevo_nombreusuario
				print('modificacion exitosa')
				return usuario.dump()
		return None		

		# devolver juegos a la biblioteca
	def agregar_videojuego(self,nombre_usuario,ID,nombre_videojuego,anio,precio,categoria1,categoria2,categoria3,Foto,Banner,Descripcion):
		for u in self.usuario:
			if u.nombre_usuario == nombre_usuario:
				for juego in u.videojuegos:
					if juego.nombre_videojuego == u.videojuegos.nombre_videojuego:
						return False
				u.videojuegos.append(VideoJuego(ID,nombre_videojuego,anio,precio,categoria1,categoria2,categoria3,Foto,Banner,Descripcion))
				return True		


	def listar_biblioteca(self,nombre_usuario):
		for usuario in self.usuario:
			if usuario.nombre_usuario == nombre_usuario:
				return json.dumps([videojuegos.dump() for videojuego in usuario.videojuegos])	
		



		