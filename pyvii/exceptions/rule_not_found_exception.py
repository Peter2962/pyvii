class RuleNotFoundException(Exception):
	def __init__(self, rule):
		self.rule = rule
		super().__init__()

	def __str__(self):
		return self.rule + "does not exist as a validation rule"