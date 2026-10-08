#задание 1
class Student:
    def __init__(self, name, age, specialty):
        self.name = name
        self.age = age
        self.specialty = specialty

    def show_info(self):
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Специальность: {self.specialty}")

    def change_specialty(self, new_specialty):
        self.specialty = new_specialty


student1 = Student("Тимур", 19, "Информационные системы")
student2 = Student("Аян", 19, "Программная инженерия")
student3 = Student("Данияр", 20, "Информационные системы")

student1.change_specialty("Кибербезопасность")

student1.show_info()
print()
student2.show_info()
print()
student3.show_info()

#задание 7
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        return self.__balance

    def show_info(self):
        print(f"Владелец: {self.owner}")
        print(f"Баланс: {self.__balance} тг")


account1 = BankAccount("Тимур", 10000)
account2 = BankAccount("Аян", 15000)
account3 = BankAccount("Данияр", 5000)

account1.deposit(5000)
account1.withdraw(3000)

account2.deposit(2000)
account2.withdraw(7000)

account3.deposit(10000)
account3.withdraw(4000)

account1.show_info()
print()
account2.show_info()
print()
account3.show_info()

#задание 20
class ElectronicWallet:
    def __init__(self, owner, pin, balance=0):
        self.owner = owner
        self.__pin = str(pin)
        self.__balance = balance
        self.__history = []

    def check_pin(self, pin):
        return self.__pin == str(pin)

    def get_balance(self, pin):
        if not self.check_pin(pin):
            return None
        return self.__balance

    def deposit(self, amount, pin):
        if not self.check_pin(pin) or amount <= 0:
            return False

        self.__balance += amount
        self.__history.append(f"Пополнение: +{amount} тг")
        return True

    def pay(self, amount, pin):
        if not self.check_pin(pin) or amount <= 0 or amount > self.__balance:
            return False

        self.__balance -= amount
        self.__history.append(f"Оплата: -{amount} тг")
        return True

    def transfer(self, other_wallet, amount, pin):
        if not self.check_pin(pin) or amount <= 0 or amount > self.__balance:
            return False

        self.__balance -= amount
        other_wallet.__balance += amount

        self.__history.append(
            f"Перевод {other_wallet.owner}: -{amount} тг"
        )
        other_wallet.__history.append(
            f"Перевод от {self.owner}: +{amount} тг"
        )
        return True

    def get_history(self, pin):
        if not self.check_pin(pin):
            return []
        return self.__history.copy()


wallet1 = ElectronicWallet("Тимур", "1234", 20000)
wallet2 = ElectronicWallet("Аян", "5678", 10000)
wallet3 = ElectronicWallet("Данияр", "9999", 5000)

wallet1.deposit(5000, "1234")
wallet1.pay(3000, "1234")
wallet1.transfer(wallet2, 4000, "1234")

print("Кошелёк Тимура:", wallet1.get_balance("1234"), "тг")
print("Кошелёк Аяна:", wallet2.get_balance("5678"), "тг")
print("Кошелёк Данияра:", wallet3.get_balance("9999"), "тг")

print("\nИстория Тимура:")
for operation in wallet1.get_history("1234"):
    print("-", operation)

