import datetime


# Mensajes posibles: Texto, Imagen, Video, Gif, Documento
class MensajeWhatsApp:
	'''
	Representa un mensaje de WhatsApp
	'''
	def __init__(self, mensaje, emisor, receptor):
		'''
		Son todos strings
		'''
		if not emisor or not receptor:
			raise ValueError("El mensaje debe tener un emisor y un receptor")
		self.mensaje = mensaje
		self.emisor = str(emisor)
		self.receptor = str(receptor)
		self.fecha = datetime.datetime.now()

	def largo_mensaje(self):
		return len(mensaje)

	def __len__(self):
		return len(mensaje)

	def __str__(self):
		return f"Hora: {str(self.fecha)} De: {self.emisor} Para: {self.receptor} \nMensaje: {self.mensaje}"


class ChatWhatsApp:
	'''
	Representa un chat de WhatsApp
	'''
	def __init__(self, usuario):
		self.usuario = usuario
		self.mensajes = []
		#self.ultima_vista. #HAY QUE ACTUALIZAR!!!!

	def agregar_mensaje(self, mensaje_whatsapp):
		'''Recibe una instancia de la clase MensajeWhatsApp'''
		self.mensajes.append(mensaje_whatsapp)

	def __len__(self):
		return len(mensajes)

	def __str__(self):
		return "\n".join([f"--> {str(m)}" if m.emisor == self.usuario else f"<-- {str(m)}" for m in self.mensajes])

class AgendaWhatsApp:
	"""Representa una Agenda de WhatsApp con muchos chats abiertos"""
	def __init__(self, usuario):
		self.usuario = usuario
		self.chats = {}

	def enviar_mensaje(self, contacto, mensaje):
		'''Si el contacto no está, tira ValueError'''
		if not contacto in self.chats:
			raise ValueError("El contacto no esta")

		mensaje_wp = MensajeWhatsApp(mensaje, self.usuario, contacto)
		self.chats[contacto].agregar_mensaje(mensaje_wp)  # self.chats[contacto] es un ChatWhatsApp!!!

	def recibir_mensaje(self, contacto, mensaje):
		'''Si el contacto no está, tira ValueError'''
		if not contacto in self.chats:
			raise ValueError("El contacto no esta")

		mensaje_wp = MensajeWhatsApp(mensaje, contacto, self.usuario)
		self.chats[contacto].agregar_mensaje(mensaje_wp)

	def agregar_contacto(self, nuevo_contacto):
		if nuevo_contacto in self.chats:
			raise ValueError("El contacto ya existe!")

		self.chats[nuevo_contacto] = ChatWhatsApp(self.usuario)

	def mostrar_chat(self, contacto):
		if not contacto in self.chats:
			raise ValueError("El contacto no esta!")
		print(self.chats[contacto])
	

	def __repr__(self):
		return f"AgendaWhatsApp: {self.usuario}, Chats: {len(self.chats)}"

	def __str__(self):
		return f"Agenda de: {self.usuario}.\nContactos: " + ",".join(self.chats.keys())



def main():
	wp = AgendaWhatsApp("Ale")

	wp.agregar_contacto("Grace")

	wp.enviar_mensaje("Grace", "¡Hola Grace!")

	wp.recibir_mensaje("Grace", "¡Hola Ale!")

	print(wp)
	print()


	wp.agregar_contacto("Alan")
	wp.enviar_mensaje("Alan", "Haceee Alan")

	print(wp)
	print()

	wp.mostrar_chat("Grace")
	print()

	wp.enviar_mensaje("Barbara", "Esto debería fallar Alan")

main(