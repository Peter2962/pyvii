from ..base_rule import BaseRule

class Confirmed(BaseRule):
	def __init__(self, **kwargs):
		self.args = kwargs.get('args')
		self.attr = kwargs.get('attr')
		self.matching_field = self.args[0]
		self.payload = kwargs.get('payload')
		self.message = '[attr] does not match [matching_field]'
		super().__init__(self.message, {
			'[attr]': self.attr,
			'[matching_field]': self.matching_field 
		})

	def validate(self, value):
		if len(self.args) != 1:
			return False

		if self.matching_field not in self.payload.keys():
			return False
		
		return True