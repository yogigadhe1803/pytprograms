class Bank:
    def __init__(self):
        self.acct = 100020
        self.name = 'Yogesh'
        self.phone = 9850556040
        self.bal = 567890000
        self.loan = 1500000.00

    def display_to_clerk(self):
        print('Coustemer name = ',self.name)
        print('Account no =',self.acct)
        print('Phone number',self.phone)
        print('Available acct balance Rs. ',self.bal)

B = Bank()
B.display_to_clerk()

