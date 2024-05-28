#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.last_transaction_amount = price * quantity
        self.items.extend([title] * quantity)

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total -= self.total * (self.discount / 100)
            print(f"After the discount, the total comes to ${self.total:.0f}.")

    def void_last_transaction(self):
        self.total -= self.last_transaction_amount
        if self.total < 0:
            self.total = 0
        self.last_transaction_amount = 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()

