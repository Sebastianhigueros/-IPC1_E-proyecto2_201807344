from Videojuego import VideoJuego
import json
import csv

class CRUD_videojuegos:
	#Constructor
	def __init__(self):
		self.Videojuego = []
		self.Contador = 0;

		#crear un perfil de videojuego
	def crear_Videojuego(self, Nombre,Anio,precio,categoria1,categoria2,categoria3,Foto,Banner,Descripcion):
		for Videojuego in self.Videojuego:
			if Videojuego.Nombre == Nombre:
				print ("el juego ya existe")
				return False
			self.Videojuego.append(Videojuego(self.Contador,Nombre,Anio,precio,categoria1,categoria2,categoria3,Foto,Banner,Descripcion))
			self.Contador += 1
			return True	

			#buscar un videojuego
	def buscar_Videojuego(self,Nombre):
		for Videojuego in self.Videojuego:
			if Videojuego.Nombre == Nombre:
				return Videojuego.dump()

		return None	

		# modificar videojuego
	def modificar_Videojuego(self,Nombre,nuevo_Nombre,nuevo_Anio,nuevo_precio,nuevo_categoria1,nuevo_categoria2,nuevo_categoria3,nuevo_Foto,nuevo_Banner,nuevo_Descripcion):
		for Videojuego in self.Videojuego:
			if self.Nombre == Nombre:
				self.Nombre = nuevo_Nombre
				self.Anio = nuevo_Anio
				self.precio = nuevo_precio
				self.categoria1 = nuevo_categoria1
				self.categoria2 = nuevo_categoria2
				self.categoria3 = nuevo_categoria3
				self.Foto = nuevo_Foto
				self.Banner = nuevo_Banner
				self.Descripcion = nuevo_Descripcion
				return True
			return False	

				# busqueda de juegos por categoria
	def buscar_categoria(self,categoria):
		for Videojuego in self.Videojuego:
			if Videojuego.categoria1 == categoria or Videojuego.categoria2 == categoria or Videojuego.categoria3 == categoria:
				return videojuego.dump()			
			return None	

			# eliminar juego si el usuario es administrador
	def Eliminar_Videojuego(self,Nombre):
		for Videojuego in self.Videojuego:
			if Videojuego.Nombre == Nombre:
				self.Videojuego.remove(Videojuego) 		
				return True
			return False	


				# lectura de archivo CSV
	def lectura_de_archivo(self,ruta):
		numero_linea = 0;
		with open(ruta, 'r') as csv_File:
			linea = csv.reader(File)

			if numero_linea > 0 :
				self.Videojuego[numero_linea].ID_V = self.Contador
				self.Videojuego[numero_linea].Nombre = linea[0]
				self.Videojuego[numero_linea].Anio = linea[1]
				self.Videojuego[numero_linea].precio = linea[2]
				self.Videojuego[numero_linea].categoria1 = linea[3]
				self.Videojuego[numero_linea].categoria2 = linea[4]
				self.Videojuego[numero_linea].categoria3 = linea[5]
				self.Videojuego[numero_linea].Foto = linea[6]
				self.Videojuego[numero_linea].Banner = linea[7]
				self.Videojuego[numero_linea].Descripcion = linea[8]
				
				self.Contador += 1
			
			else:
				data = list(linea)
		

		numero_linea += 1


	def mostrar_juego(self,Nombre):
		for videojuego in self.Videojuego:
			if Videojuego.Nombre == Nombre:
				return Videojuego.dump()
						
				



		# mostrar la informacion del juego
	def lista_videojuegos(self):
	
		return json.dumps([Videojuego.dump() for Videojuego in self.Videojuego])				