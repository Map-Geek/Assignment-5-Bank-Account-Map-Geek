"""
Python Development II Assignment 5: Bank Account
Geetha Ramesh

banking.py

This module defines two classes, `Transaction` and `Account`, to model a bank account that
handles the financial transactions and account balances.

Classes:
- `Transaction`: Represents financial transaction, including the amount and timestamp.
- `Account`: Represents a bank account that manages transactions, supports deposit,
             withdrawal operations and computes the account balance.
"""

import datetime as dt
from decimal import Decimal


class Transaction:
    """
    A transaction class to represent a financial transaction.

    Attributes:
        amount: The amount of money for the transaction.
        timestamp (datetime): The timestamp of the transaction. Defaults to the current date
                              and time if not provided.

    Methods:
        __repr__(): Returns a formal string representation of the object,
                    suitable for debugging and recreating the object in the interpreter.
        __str__(): Returns a user-friendly, formatted string that displays the Transaction
                   amount as currency and the corresponding timestamp.
    """

    def __init__(self, amount, timestamp=None):
        """
        Initialize a new Transaction object.

        :param amount: The amount involved in the transaction (int, float or Decimal).
        :param timestamp: Optional; The timestamp of the transaction (datetime object).
                          If not provided, the current datetime is used.
        :raises: Value Error: If the amount is not a valid number (int, float, or Decimal)
                              and if the timestamp is not a valid datetime object.
        """

        if not isinstance(amount, (int, float, Decimal)):
            raise ValueError("Amount must be a number.")

        # Bind the amount to the instance
        self.amount = amount

        # If no timestamp is provided, use the current datetime
        if timestamp is None:
            timestamp = dt.datetime.now()

        if not isinstance(timestamp, dt.datetime):
            raise ValueError("Timestamp must be a datetime object.")

        # Bind the timestamp to the instance
        self.timestamp = timestamp

    def __repr__(self):
        """
        Returns a detailed string representation of the Transaction object,
        useful for debugging, recreating the object in the interpreter.

        :return: str: A string representation of the Transaction object.
        """
        return f"Transaction(amount={str(self.amount)}, timestamp={repr(self.timestamp)})"

    def __str__(self):
        """
        Returns a formatted string representation of the Transaction object,
        with the amount as currency and timestamp.

        :return: str: A formatted string in the form of 'YYYY-MM-DD: +$amount'
                      or 'YYYY-MM-DD: -$amount'.
        """

        formatted_amount = f"{abs(self.amount):,.2f}"
        if self.amount >= 0:
            formatted_amount = f"+${formatted_amount}"
        else:
            formatted_amount = f"-${formatted_amount}"
        return f"{self.timestamp.date()}: {formatted_amount}"


class Account:
    """
    Represents a bank account that tracks transactions and calculates balance.

    Attributes:
        transactions (list): A list of Transaction objects representing
                             deposits and withdrawals.

    Methods:
        deposit(amount):
            Records a deposit transaction with a positive amount.

        withdraw(amount):
            Records a withdrawal transaction with a negative amount.

        get_balance():
            Calculates and returns the current balance by summing all
            transaction amounts.
    """

    def __init__(self):
        # Initialize with an empty list of transactions
        self.transactions = []

    def deposit(self, amount):
        """
        Creates a deposit transaction and adds it to the transaction list.
        :param amount: The amount to deposit.
        """
        amount = abs(amount)  # Convert to positive amount
        transaction = Transaction(amount)
        self.transactions.append(transaction)

    def withdraw(self, amount):
        """
        Creates a withdrawal transaction and adds it to the transaction list.
        :param amount: The amount to withdraw.
        """
        amount = -abs(amount)  # Convert to negative amount
        transaction = Transaction(amount)
        self.transactions.append(transaction)

    def get_balance(self):
        """
        Calculates and returns the balance by summing up all transaction amounts.
        :return: The sum of all transaction amounts. Returns 0 if no transactions exist.
        """
        return sum(transaction.amount for transaction in self.transactions)
