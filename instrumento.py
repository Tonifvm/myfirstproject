class instrumento :
	"""docstring for instrumento"""
	def __init__(self, precio):
		self.precio = precio
		
	def tocar(self):
		print "estamos tocando algo de musica"

	def romper(self):
		print "son" , self.precio , "euros"

class Bateria(instrumento):
	pass

class Guitarra(instrumento):
	def__init__ (self, precio, tipocuerda):
		instrumento.__init__(self, precio)	



		
		
		