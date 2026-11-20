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


class SavingsAccount(Account):
    def __init__(self, number, owner, balance = 0, rate = 0.05):
        super().__init__(number, owner, balance)
        self.rate = rate

    def add_interest(self):
        interest = self._balance * self.rate
        self._balance += interest

    def __repr__(self):
        return f"SavingsAccount('{self.number}', '{self.owner}', '{self._balance}', '{self.rate}')"


class CheckingAccount(Account):
    def __init__(self, number, owner, balance = 0, overdraft = 0):
        super().__init__(number, owner, balance)
        if overdraft < 0:
            raise ValueError("Лимит овердрафта не может быть отрицательным")
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if self._balance - amount < -self.overdraft:
            raise ValueError("Превышен лимит овердрафта")
        self._balance -= amount

    def __repr__(self):
        return f"CheckingAccount('{self.number}', '{self.owner}', '{self._balance}', '{self.overdraft}')"

if __name__ == "__main__":
    s = SavingsAccount("1", "Иван", 1000, rate=0.1)
    s.add_interest()
    print(s.balance)  # Ожидается: 1100.0
    try:
        s.withdraw(2000)  # ValueError
    except ValueError as e:
        print(f"ValueError: {e}")

    try:
        s.balance = 0  # AttributeError
    except AttributeError as e:
        print(f"AttributeError: {e}")

    # Тест расчетного счета с овердрафтом
    c = CheckingAccount("2", "Мария", 100, overdraft=500)
    c.withdraw(400)
    print(c.balance)  # Ожидается: -300
    try:
        c.withdraw(300)  # ValueError: превышен овердрафт
    except ValueError as e:
        print(f"ValueError: {e}")

    c.deposit(1000)
    print(c.balance)  # Ожидается: 700
    print(isinstance(c, Account))  # Ожидается: True
