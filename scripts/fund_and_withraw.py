from brownie import FundMe
from scripts.helpful_scripts import getAccount


def fund():
    fund_me = FundMe[-1]
    account = getAccount()
    entrance_fee = fund_me.getEntranceFee()
    print(f"Entrance fee: {entrance_fee}")
    fund_me.fund({"from": account, "value": entrance_fee})


def withraw():
    fund_me = FundMe[-1]
    account = getAccount()
    fund_me.withdraw({"from": account})


def main():
    withraw()
