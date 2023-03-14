# import rules
from .rules.max import Max
from .rules.min import Min
from .rules.email import Email
from .rules.password import Password
from .rules.required import Required

# import exceptions
from .exceptions.rule_not_found_exception import RuleNotFoundException

class Validator():
	"""
	Attributes:
	-----------
	schema : dict {
		'name': ['required'],
		'email': ['required', 'email']
	}
	payload : dict {
		'name': 'name_value',
		'email': 'email_value'
	}
	"""
	schema = {}
	payload = {}
	errors = {}

	def __init__(self):
		self.default_rules = {
			'max': Max,
			'min': Min,
			'email': Email,
			'password': Password,
			'required': Required
		}

	def validate(self, schema, payload):
		self.schema = schema
		self.payload = payload
		self.errors = {}

		for key in self.payload:
			payload_attr_value = self.payload[key]
			for attr in schema:
				"""
				set_rules is required to be a list
				"""
				set_rules = schema[attr]
				for set_rule in set_rules:
					set_rule_name = Validator.get_clean_rule_name(set_rule)
					
					"""
					make sure the rule exists in the rules list
					"""
					if set_rule_name not in self.default_rules.keys():
						raise RuleNotFoundException(set_rule_name)

					set_rule_class = self.default_rules[set_rule_name]
					rule_object = set_rule_class(attr, set_rule)
					
					additional_validator_args = ''
					set_rule_split = set_rule.split(':')
					
					if len(set_rule_split) > 1:
						additional_validator_args = set_rule_split[1]

					if rule_object.validate(payload_attr_value, set_rule) == False:
						"""
						if validation fails for each rule, create a list for each
						attr in self.errors dict
						"""
						if attr not in self.errors.keys():
							self.errors[attr] = []

						self.errors[attr].append(
							rule_object.getMessage()
						)

	def get_clean_rule_name(set_rule):
		return set_rule.split(':')[0]

	def has_error(self, key):
		if key in self.errors.keys():
			return True

		return False

	def has_errors(self):
		if len(self.errors.keys()) > 0:
			return True

		return False

	def get_errors(self):
		return self.errors