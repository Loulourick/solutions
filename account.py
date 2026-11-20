class Account:
    def __init__(self, number, owner, balance = 0):
        if balance < 0: raise ValueError("Начальный остаток отрицательный")
        self._number = number
        self._owner = owner
        self._balance = balance

    @property
    def number(self):
        return self._number

    @property
    def owner(self):
        return self._owner

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self._balance:
            raise ValueError("Недостаточно средств")
        self._balance -= amount

    def __repr__(self):
        return f"Account('{self.number}', '{self.owner}', {self.balance})"

if __name__ == "__main__":
    acc = Account("40817", "Иван", 1000)
    acc.deposit(500)
    print(acc.balance)  # 1500
    acc.withdraw(200)
    print(acc.balance)  # 1300

    try:
        acc.withdraw(5000)  # Ошибка: недостаточно средств
    except ValueError as e:
        print(f"ValueError: {e}")

    print(acc.balance)  # 1300 - операция ничего не испортила
    print(acc)  # Account('40817', 'Иван', 1300)
