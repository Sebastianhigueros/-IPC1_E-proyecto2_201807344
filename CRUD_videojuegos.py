from Videojuego import VideoJuego
from comentarios import Comentarios
import json
import csv

class CRUD_videojuegos:
	#Constructor
	def __init__(self):
		self.Videojuego = []
		self.Contador = 0

		#crear un videojuego
	def crear_Videojuego(self,Nombre,Anio,precio,categoria1,categoria2,categoria3,Foto,Banner,Descripcion):
		for videojuego in self.Videojuego:
			if videojuego.Nombre == Nombre:
				print ("el juego ya existe")
				return False
		self.Videojuego.append(VideoJuego(self.Contador,Nombre,Anio,precio,categoria1,categoria2,categoria3,Foto,Banner,Descripcion))
		print('el juego se creo correctamente')
		self.Contador += 1
		return True	

			#buscar un videojuego
	def buscar_Videojuego(self,Nombre):
		for videojuego in self.Videojuego:
			if videojuego.Nombre == Nombre:
				return videojuego.dump()

		return None	

		# modificar videojuego
	def modificar_Videojuego(self,Nombre,nuevo_Nombre,nuevo_Anio,nuevo_precio,nuevo_categoria1,nuevo_categoria2,nuevo_categoria3,nuevo_Foto,nuevo_Banner,nuevo_Descripcion):
		for videojuego in self.Videojuego:
			if videojuego.Nombre == Nombre:
				videojuego.Nombre = nuevo_Nombre
				videojuego.Anio = nuevo_Anio
				videojuego.precio = nuevo_precio
				videojuego.categoria1 = nuevo_categoria1
				videojuego.categoria2 = nuevo_categoria2
				videojuego.categoria3 = nuevo_categoria3
				videojuego.Foto = nuevo_Foto
				videojuego.Banner = nuevo_Banner
				videojuego.Descripcion = nuevo_Descripcion
				return videojuego.dump()
		return None	

				# busqueda de juegos por categoria
	def buscar_categoria(self,categoria):
		for videojuego in self.Videojuego:
			if videojuego.categoria1 == categoria or videojuego.categoria2 == categoria or videojuego.categoria3 == categoria:
				juegos = list[videojuego]			
		return json.dumps(VideoJuego.dump() for juego in juegos)

			# eliminar juego si el usuario es administrador
	def Eliminar_Videojuego(self,Nombre):
		for videojuego in self.Videojuego:
			if videojuego.Nombre == Nombre:
				self.Videojuego.remove(videojuego) 		
				return True
		return False	

	def mostrar_juego(self,ID_V):
		for videojuego in self.Videojuego:
			if videojuego.ID_V == ID_V:
				return videojuego.dump()
		return None			
				
	def comentar(self,Nombre,usuario,fecha,comentario):
		for juego in self.Videojuego:
			if juego.Nombre == Nombre:
				comentario = juego.Videojuego[11].append(Comentarios(usuario,fecha,comentario))
				return comentario.dump()

	def comentarios_de_juego(self,Nombre):
		for juego in self.Videojuego:
			if juego.Nombre == Nombre:
				return json.dumps(Comentarios.dump() for comentario in Videojuego[11])

						
		# mostrar lista de videojuegos
	def lista_videojuegos(self):
	
		return json.dumps([VideoJuego.dump() for Videojuego in self.Videojuego])				