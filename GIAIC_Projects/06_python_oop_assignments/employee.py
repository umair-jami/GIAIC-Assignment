class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

# Test
e = Employee("John", 50000, "123-45-6789")
print(e.name)
print(e._salary)
try:
    print(e.__ssn)
except AttributeError as err:
    print(err)
