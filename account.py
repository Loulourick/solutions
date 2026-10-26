class  Account:
    def __init__(self, number, owner, balance):
        if balance < 0: raise ValueError("Счёт не может быть отрицательным")
        self.number = number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        if self.balance - amount < 0: raise ValueError("недостаточно средств")
        self.balance -= amount
        return self.balance
    def __repr__(self, amount):
        return f"Account('{self.number}', '{self.owner}', {self.balance})"

acc = Account(number="1", owner="Иван", balance=1000)
print(acc.deposit(500))
print(acc.balance)          # 1500
print(acc.withdraw(200))
print(acc.balance)          # 1300
print(acc.withdraw(5000))   # ValueError: недостаточно средств
print(acc.balance)          # 1300 - неудачная операция ничего не испортила
print(acc)                  # Account('40817', 'Иван', 1300)
