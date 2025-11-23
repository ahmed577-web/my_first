class Bank:
    def __init__(self):
        self.users = []

    def add_user(self, name, acc, balance, passw):
        self.users.append({
            "name": name,
            "acc": str(acc),
            "balance": balance,
            "passw": str(passw)
        })

    def login(self, account, password):

        for user in self.users:
            if user['acc'] == account and user['passw'] == password:
                print(f"Welcome {user['name']}")
                return user
        print("Login unsuccessful")
        return None

    def bank_users(self):
        print('Bank Users:')
        for user in self.users:
            print(f"Name: {user['name']}\nAccount: {user['acc']}\nBalance: {user['balance']}\n")

    def deposit(self, current_user):
        if not current_user:
            print("No user logged in.")
            return
        amount = int(input("Enter an amount to deposit: "))
        current_user['balance'] += amount
        print(f"Your new balance is {current_user['balance']}")

    def withdraw(self, current_user):
        if not current_user:
            print("No user logged in.")
            return
        amount = int(input("Enter an amount to withdraw: "))
        if amount > current_user['balance']:
            print("Not enough balance")
        else:
            current_user['balance'] -= amount
            print(f"Your new balance is {current_user['balance']}")

    def show_balance(self, current_user):
        if not current_user:
            print("No user logged in.")
            return
        print(f"Your current balance is {current_user['balance']}")

    def find(self, find_user):
        filter = [user for user in self.users if find_user == user["acc"]]
        if filter:
            for user in filter:
                print(f"{user['name']}")


users = Bank()
users.add_user("ahmed", "12334", 500, '444')
users.add_user("bali", "34455", 50000, '333')

acc = input(str("Enter your account: "))
password = input(str("Enter your password: "))

current_user = users.login(acc, password)

if current_user:
    while True:
        print('\n1. Show Balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. find user')
        print('5.add user')

        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            users.show_balance(current_user)
        elif choice == 2:
            users.deposit(current_user)
        elif choice == 3:

            users.withdraw(current_user)
        elif choice == 4:
            find_user = (input("Enter account no to find user"))
            users.find(find_user)

        else:
         print('Invalid choice')
