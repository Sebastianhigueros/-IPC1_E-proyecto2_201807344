from Videojuego import VideoJuego


class Usuario:


	def __init__(self,ID,Nombre,Apellido,nombre_usuario,Contrasena, tipo):
		self.ID = ID
		self.Nombre = Nombre
		self.Apellido = Apellido
		self.nombre_usuario = nombre_usuario
		self.Contrasena = Contrasena
		self.tipo = tipo
		self.videojuegos = []

	def dump(self):
		return {
			'ID' : self.ID,
			'Nombre' : self.Nombre,
			'Apellido' : self.Apellido,
			'nombre_usuario' : self.nombre_usuario,
			'Contrasena' : self.Contrasena,
			'tipo' : self.tipo,
			'videojuego': devolver_juegos()

		}