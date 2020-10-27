class VideoJuego:

	def __init__(self,ID_V,Nombre,Anio,precio,categoria1,categoria2,categoria3,Foto,Banner,Descripcion):
		self.ID_V = ID_V
		self.Nombre = Nombre
		self.Anio = Anio
		self.precio = precio
		self.categoria1 = categoria1
		self.categoria2 = categoria2
		self.categoria3 = categoria3
		self.Foto = Foto
		self.Banner = Banner
		self.Descripcion = Descripcion

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