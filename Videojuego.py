class VideoJuego:

	def __init__(self,ID_V,Nombre,Anio,precio,categoria1,categoria2,categoria3,Foto,Banner,Descripcion):
		self.__ID_V = ID_V
		self.__Nombre = Nombre
		self.__Anio = Anio
		self.__precio = precio
		self.__categoria1 = categoria1
		self.__categoria2 = categoria2
		self.__categoria3 = categoria3
		self.__Foto = Foto
		self.__Banner = Banner
		self.__Descripcion = Descripcion

	def dump(self):
		return{
			'ID_V' : self.ID_V,
			'Nombre' : self.Nombre,
			'Anio' : self.Anio,
			'precio' : self.precio,
			'categoria1' : self.categoria1,
			'categoria2' : self.categoria2,
			'categoria3' : self.categoria3,
			'Foto' : self.Foto,
			'Banner' : self.Banner,
			'Descripcion' : self.Descripcion
		}