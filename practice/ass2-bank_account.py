# Imagine you are responsible for developing an app to manage people's bank accounts and their entire lives' savings (no pressure ^^'). Your project manager asks you to write two classes in Python:

# - one to keep track of all the money the client has in the bank
# - one for every subaccount the client opened at the bank i.e. salary, rent...


class BankAccount:
    """General bank account class.
    It keeps track of all the transactions a user makes in their subaccounts.
    """

    # Keeps track of the balances throughout all the sub-accounts
    _overall_balance = 0.0

    # Whether any subacccount is blocked
    _blocked = False

    def __init__(self, account_num, name, balance=0.0, pin='0000'):
        """Constructor for BankAccount objects.

        Attributes:
        - account_num(str): number of the (sub)account
        - name(str): name of the account owner
        - _balance(float): current amount deposited. Cannot be negative. Default: 0.0.
        - _pin(str): 4-character numerical string for the PIN code. Default: '0000'.

        Note that whenever a new subaccount is opened, the constructor adds the new deposit 
        to the overall balance.
        """

        # Your code here
        self.account_num = account_num
        self.name = name
        self.balance = balance
        BankAccount._overall_balance += balance
        self.pin = pin

    def check_pin(self):
        """Auxiliary method that asks the user to insert the PIN.

        Returns True, if the user introduced the right PIN in at most 3 tries, otherwise False.
        """

        # Your code here
        if (BankAccount._blocked):
            print('Sorry, your accounts are blocked!')
            return False
        correct_pin = False
        for i in range(0, 3):
            user_pin = input('Please insert your PIN: ')
            if (user_pin == self.pin):
                correct_pin = True
                break
        if (correct_pin == False):
            BankAccount._blocked = True
            print(
                'Your account is now blocked because of too many failed trials to enter the PIN!')
        return correct_pin

    def deposit(self, amount):
        """Method to add more money to the account, if no accounts are blocked and if the user introduces the correct PIN.
        If the user introduces a wrong PIN 3 times, all their (sub)accounts are blocked. 

        Parameters:
        - amount(float): new amount to add to the current deposit. Cannot be negative.

        After successful transaction, the overall balance will be adjusted.
        """

        # Your code here
        verified = self.check_pin()
        if verified == True:
            if amount < 0:
                print(f'{amount} is a negative value')
                return
            BankAccount._overall_balance += amount
            self.balance += amount
            print(f'{amount} was added to your account.')

    def withdraw(self, amount):
        """Method to remove money from the account, if no accounts are blocked and if the user introduces the correct PIN.
        If the user introduces a wrong PIN 3 times, all their (sub)accounts are blocked. 

        Parameters:
        - amount(float): amount to remove from the current deposit. Cannot be greater than the current balance.

        After successful transaction, the overall balance will be adjusted.
        """

        # Your code here
        verified = self.check_pin()
        if verified == True:
            if (amount > self.balance):
                print(f'{amount} is greater than the current balance.')
                return
            BankAccount._overall_balance -= amount
            self.balance -= amount
            print(f'{amount} was deducted from your account.')


class SubAccount(BankAccount):
    """Class for a specific subaccount derived from BankAccount.
    """

    def __init__(self, account_num, name, balance, pin, account_type):
        """Constructor for SubAccount objects.

        Attributes (additional to BankAccount attributes):
        - account_type(str): what the account is used for i.e. salary, rent etc.
        """

        # Your code here
        super().__init__(account_num, name, balance, pin)
        self.account_type = account_type

    def __str__(self):
        """Prints infos for the current subaccount (account number, owner name, account type, balance), as well as
        the total balance from all accounts, if and only if none of the account were blocked and if the user introduces 
        the right PIN in maximum 3 tries. Otherwise, blocks all accounts.
        """

        # Your code here
        verified = self.check_pin()
        if verified == True:
            print('Account number:', self.account_num)
            print('Account owner:', self.name)
            print('Total type:', self.account_type)
            print('Balance:', self.balance)
            print('Total balance:', self._overall_balance)
        return ''


# Create 2 subaccounts for client Max Mustermann (don't change these lines)
acc1 = SubAccount("1234", "Max Mustermann", 500, "3333", "Salary")
acc2 = SubAccount("5678", "Max Mustermann", 1000, "7777", "Mortgage")

print(acc1)

print(acc2)

acc1.deposit(2000)
print(acc1)

acc2.withdraw(200)
print(acc2)

print(acc1)

print(acc1)
print(acc2)
acc1.deposit(10)
acc2.withdraw(10)
