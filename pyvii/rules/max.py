from ..base_rule import BaseRule

class Max(BaseRule):
	"""
	Max rule:
	---------------
	{
		'payload_attr': 'max:10'
	}
	"""
	def __init__(self, **kwargs):
		self.length_of_field = kwargs.get('args')[0]
		self.message = '[attr] must not be greater than ' + str(self.length_of_field) + ' characters'
		super().__init__(self.message, {
			'[attr]': kwargs.get('attr')
		})

	def validate(self, value):
		if len(value) > int(self.length_of_field):
			return False
		
		return True