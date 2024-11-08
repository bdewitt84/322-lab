import pytest
from bank import Account

""" working on pytest fixtures
@pytest.fixture
def myAccount():
    return myAccount.Account("user")
"""

def test_initial_balance():
    """makes sure initial balance is 0"""
    myAccount.Account("user")
    assert myAccount.get_balance() == 0

def test_deposit():
    """deposits must be positive into account"""
    myAccount = Account("user")
    myAccount.deposit(10)
    assert myAccount.get_balance() == 10
    with pytest.raises(ValueError):
        myAccount.deposit(-2)

def test_withdraw():
    """withrawals must be positive from account"""
    myAccount = Account("user")
    myAccount.deposit(10)
    myAccount.withdraw(3)
    assert myAccount.get_balance() == 7
    myAccount.withdraw(5)
    assert myAccount.get_balance() == 2
    with pytest.raises(ValueError):
        myAccount.withdraw(4)

def test_deposit_negative_amount():
    """cannot deposit negative amount"""
    myAccount = Account("user")
    with pytest.raises(ValueError):
        myAccount.deposit(-1)

def test_withdraw_more_than_balance():
    """cannot withdraw if balance reaches below 0"""
    myAccount = Account("user")
    with pytest.raises(ValueError):
        myAccount.withdraw(3)

def test_withdraw_negative_amount():
    """cannot withdraw negative amount"""
    myAccount = Account("user")
    with pytest.raises(ValueError):
        myAccount.withdraw(-2)
