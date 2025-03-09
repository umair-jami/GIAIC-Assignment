# Regular variable
# Constant
PI=3.14
# Class Name
BankAccount="ClassName"
# Private variable
_password="123"
print(_password)

# Private with Name Mangling
_scret_key="1234"
print(_scret_key)

# Summary of Naming Conventions
# Convention	Used For	Example
# snake_case	Variables & functions	user_name, total_price
# CamelCase	Classes	BankAccount, DataScienceModel
# UPPER_CASE	Constants	MAX_SPEED, PI
# _single_underscore	Private variable (by convention)	_config
# __double_underscore	Name mangling (avoid external access)	__password
# __dunder__	Special methods	__init__, __str__