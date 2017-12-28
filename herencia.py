class Terrestre(object):
	
	def __init__(self, velocidadcaminar):
		super(Terrestre, self).__init__()
		self.velocidadcaminar = velocidadcaminar
		
	def caminar(self):
			print "estoy caminando"

	def desplazar(self):
			print "el animal anda"

class Acuatico(object):
	
	def __init__(self, velocidaddenado):
		super(Acuatico, self).__init__()
		self.velocidaddenado = velocidaddenado

	def nada(self):
			print "estoy nadando"

	def desplazar(self):
			print "el animal nada"

class cocodrilo (Terrestre, Acuatico):


cocodrilo1 = cocodrilo(1)
cocodrilo1.desplazar()	

#change 1

