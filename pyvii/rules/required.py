from ..base_rule import BaseRule

class Required(BaseRule):
	def __init__(self, **kwargs):
		attr = kwargs.get('attr')
		self.message = '[attr] is required'
		super().__init__(self.message, {
			'[attr]': attr
		})

	def validate(self, value):
		if not value:
			return False

		return True