class BaseRule():
	"""
	Attributes:
	-----------
	message : str (message to be returned from the inheriting rule class)
	attrs : dict (a dictionary containing attributes to be replaced)
	"""
	def __init__(self, message, attrs):
		self.message = message
		self.attrs = attrs

	def getMessage(self):
		for placeholder in self.attrs.keys():
			self.message = self.message.replace(placeholder, self.attrs[placeholder])
		return self.message
