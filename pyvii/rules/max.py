from ..base_rule import BaseRule

class Max(BaseRule):
	def __init__(self, attr, args):
		self.length_of_field = args[0]
		self.message = '[attr] must not be greater than ' + str(self.length_of_field) + ' characters'
		super().__init__(self.message, {
			'[attr]': attr
		})

	def validate(self, value):
		if len(value) > int(self.length_of_field):
			return False
		
		return True