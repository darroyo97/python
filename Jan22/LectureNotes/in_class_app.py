# Bank Account App
class AccountHolder:
    def __init__(self, fname, lname, mname, type, status, balance):
        self.fname = fname
        self.lname = lname
        self.mname = mname
        self.type = type
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
            account = AccountHolder(fname, lname, mname, type, status, balance)
            self.accounts.append(account)
            return print(f'{type } account has been open for {fname} {mname} {lname} with a balance of {balance}')
            # then we going to store it into our list of accounts
            # return a message to user if it was succesful
        else:
            return "Insufficient Funds, to open an account myst have deposit of at least $100"

            # definition of main that includes a while loop with menu of things user wants to do
            # main()
    def show_members(self):
        for members in self.accounts:
            print(
                f'{members.type} account \n Name: {members.fname} {members.mname} {members.lname} \n  Balance: {members.balance}')


def main():
    wellsfargo = Bank("wells fargo", "123 Sesame St.")
    action = 1
    while action != 6:
        print("1. Create An Account: ")
        print("2. Print List Of All Account Holders: ")
        print("6. Exit Application: ")

        action = int(input("What would you like to do? "))

        if (action == 1):
            fname = input("What is the first name? ")
            mname = input("What is the middle name? ")
            lname = input("What is the last name? ")
            type = input("What would you like to open? (Checking or Saving)")
            balance = int(input("Amount you wish to deposit? "))

            wellsfargo.open_new_account(
                fname, lname, mname, type, "open", balance)
        elif (action == 2):
            wellsfargo.show_members()
        elif (action == 6):
            break


main()
