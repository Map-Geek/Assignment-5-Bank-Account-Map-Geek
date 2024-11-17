"""
Python Development II Assignment 5: Bank Account
Geetha Ramesh

test_banking.py

Unit tests for Transaction and Account classes.

This module contains test cases to verify the functionality of the Transaction
and Account classes, including their initialization, behavior, and string representations.
"""

from datetime import datetime as dt
import pytest
from banking import Transaction, Account


def test_transaction_invalid_amount():
    """
    Test that an exception is raised when an invalid amount is passed
    :raises: Value Error
    """
    with pytest.raises(ValueError):
        Transaction(amount="fifty", timestamp=dt(2024, 11, 14, 12, 30))


def test_initialization_with_amount_timestamp():
    """
    Test to check that a Transaction instance is correctly created
    when both an amount and a timestamp are passed to the constructor
    """
    timestamp = dt(2024, 11, 14, 12, 30)
    transaction = Transaction(amount=100.50, timestamp=timestamp)

    assert transaction.amount == 100.50
    assert transaction.timestamp == timestamp


def test_transaction_with_default_timestamp():
    """
    Test that when no timestamp is provided, it should default to
    the current datetime
    """
    transaction = Transaction(amount=200.75)

    assert transaction.amount == 200.75
    assert isinstance(transaction.timestamp, dt)


def test_transaction_timestamp():
    """
    Test to verify that when a Transaction instance is created with a date only,
    the timestamp is set correctly with the time defaulting to midnight (00:00:00).
    """
    transaction = Transaction(amount=10, timestamp=dt(2002, 1, 10))
    expected_timestamp = dt(2002, 1, 10, 0, 0, 0)
    assert transaction.timestamp == expected_timestamp


def test_transaction_repr():
    """
    Test the __repr__ method to ensure it gives the expected string output
    """
    transaction = Transaction(amount=150.51, timestamp=dt(2024, 11, 14, 12, 30))
    expected_repr = "Transaction(amount=150.51, timestamp=datetime.datetime(2024, 11, 14, 12, 30))"
    assert repr(transaction) == expected_repr


def test_transaction_str():
    """
    Test the __str__ method to ensure it formats the amount and timestamp correctly
    """
    transaction = Transaction(amount=-370.00, timestamp=dt(2024, 11, 14, 12, 30))
    expected_str = "2024-11-14: -$370.00"
    assert str(transaction) == expected_str


def test_account_initialization():
    """
    Test that the transactions attribute is initialized as an empty list
    """
    account = Account()

    assert isinstance(account.transactions, list)
    assert len(account.transactions) == 0
