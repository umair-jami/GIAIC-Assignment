class Bank:
    bank_name = "MyBank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

# Test
print(Bank.bank_name)
Bank.change_bank_name("NewBank")
print(Bank.bank_name)
