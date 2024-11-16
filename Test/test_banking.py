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
from banking import Transaction


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
