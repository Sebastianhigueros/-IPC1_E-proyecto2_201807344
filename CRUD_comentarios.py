from CRUD_usuario import CRUD_usuario
from comentarios import Comentarios
from datetime import datetime

class CRUD_comentarios:

	def __init__(self):
		self.comentarios = []
		self.contador = 0

	def comentar(self,usuario,comentario):
		comentario.usuario = usuario
		comentario.fecha = datetime.datetime.now()
		comentario.comentario = comentario
		return comentario	