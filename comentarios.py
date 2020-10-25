class Comentarios:

	def __init__(self,usuario,fecha,comentario):
		self.__usuario = usuario
		self.__fecha = fecha
		self.comentario = comentario

	def dump(self):
		return{
			'usuario' : self.usuario,
			'fecha' : self.fecha,
			'comentario' : self.comentario
		}	