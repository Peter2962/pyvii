class PayloadAttributeNotFoundException(Exception):
	def __init__(self, attribute):
		self.attribute = attribute
		super().__init__()

	def __str__(self):
		return self.attribute + " is not a defined payload attribute"