from Videojuego import VideoJuego
from comentarios import Comentarios
import json
import csv

class CRUD_videojuegos:
	#Constructor
	def __init__(self):
		self.Videojuego = []
		self.Contador = 0

		#crear un perfil de videojuego
	def crear_Videojuego(self, Nombre,Anio,precio,categoria1,categoria2,categoria3,Foto,Banner,Descripcion):
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
				return Videojuego.dump()

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
				return True
		return False	

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


				# lectura de archivo CSV
	def lectura_de_archivo(self,ruta):
		numero_linea = 0;
		with open(ruta, 'r') as csv_File:
			linea = csv.reader(File)

			if numero_linea > 0 :
				
				self.Videojuego.append(VideoJuego(linea[0],linea[1],linea[2],linea[3],linea[4],linea[5],linea[6],linea[7],linea[8],linea[9],self.comentarios))


		return True		
		


	def mostrar_juego(self,ID):
		for videojuego in self.Videojuego:
			if videojuego.ID_V == ID:
				return videojuego.dump()
		return None			
				
	#def comentar(self,usuario,fecha,comentario):
		


		# mostrar lista de videojuegos
	def lista_videojuegos(self):
	
		return json.dumps([Videojuego.dump() for Videojuego in self.Videojuego])				