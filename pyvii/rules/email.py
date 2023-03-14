import re
from ..base_rule import BaseRule

class Email(BaseRule):
	def __init__(self, attr, rule):
		self.message = '[attr] is not a valid email'
		super().__init__(self.message, {
			'[attr]': attr
		})

	def validate(self, value, additional_args = ''):
		pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
		if re.match(pattern, value):
			return True

		return False