# Bank Account App
class Account Holder:
    def __init__(self, fname, lname, mname, type, status, balance):
        self.first_name = fname
        self.last_name = lname
        self.middle_name = mname
        self.account_type = type
        self.status = status
        self.balance = balance


class Bank:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.accounts = []
