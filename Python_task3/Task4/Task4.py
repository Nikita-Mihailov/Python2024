class Wallet:
    payment_system = "Visa"

    def __init__(self, balance, currency, name):
        self.name = name
        self.balance = balance
        self.currency = currency

    def deposit(self, amount):
        self.balance += amount
        return f"Пополнение выполнено успешно: {amount} {self.currency}"

    def pay(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Оплата прошла успешно: {amount} {self.currency}"
        else:
            return "Недостаточно средств"

    def get_balance(self):
        return f"Текущий баланс: {self.balance} {self.currency}"

    def delete_wallet(self):
        del self.balance
        del self.currency
        del self.name
        return "Кошелек удален"


class CryptoWallet(Wallet):
    def __init__(self, balance, currency, name, coins):
        super().__init__(balance, currency, name)
        self.coins = coins

    def get_balance(self):
        return f"Баланс: {self.coins} {self.currency}"

    def convert_to(self):
        if self.currency == "BTC":
            coin_price = 72000
            self.balance = self.coins * coin_price
        elif self.currency == "ETH":
            coin_price = 3500
            self.balance = self.coins * coin_price
        else:
            self.balance = 0
        return f"Баланс: {self.balance} USD"


def wallet_operation():
    my_wallet = Wallet(0, "USD", "Wallet 1")
    if not my_wallet.currency in ["USD", "EUR", "RUB"]:
        raise ValueError("Unsupported currency")
    crypto_wallet1 = CryptoWallet(0, "BTC", "CryptoWallet1", 3)

    while True:
        print("1. Баланс\n2. Пополнение\n3. Оплата\n4. Удаление счета\n5. Действия с крипто-кошельком")
        try:
            choice = input()
            if choice == "1":
                print(my_wallet.get_balance())
            elif choice == "2":
                amount = int(input("Введите сумму пополнения: "))
                if not isinstance(amount, int):
                    raise ValueError()
                print(my_wallet.deposit(amount))
            elif choice == "3":
                amount = int(input("Введите сумму оплаты: "))
                if not isinstance(amount, int):
                    raise ValueError()
                print(my_wallet.pay(amount))
            elif choice == "4":
                print(my_wallet.delete_wallet())
                break
            elif choice == "5":
                while True:
                    print("Выберите действие с крипто-кошельком: ")
                    print("1. Баланс, 2. Конвертация, 3. Назад")
                    Choice = input()
                    if Choice == "1":
                        print(crypto_wallet1.get_balance())
                    elif Choice == "2":
                        print("Напоминаем что текущий курс равен: 1 BTC = 72000 USD, 1 ETH = 3500 USD")
                        print(crypto_wallet1.convert_to())
                    elif Choice == "3":
                        print("Возврат в начальное меню")
                        break

            else:
                print("Ошибка: Такая операция с кошельком не найдена")
        except ValueError:
            print("Ошибка: значение введено не верно")


wallet_operation()