# Bank Account App
class AccountHolder:
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

    def open_new_account(self, fname, lname, mname, type, status, balance):
        if balance >= 100:
            # create an account holder
            # then we going to store it into our list of accounts
            # return a message to user if it was succesful
        else:
            # return of insufficient deposit amount

            # definition of main that includes a while loop with menu of things user wants to do
            # main()


wellsfargo = Bank("wells fargo", "123 Sesame St.")
wellsfargo.open_new_account("Veronica", "Leno", "Celeste", "Checking", 102)
