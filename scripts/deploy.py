from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import (
    getAccount,
    deployMocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
from web3 import Web3


def deploy_fund_me():
    account = getAccount()
    print(account)

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pricefeed_address = config["networks"][network.show_active()].get(
            "eth_usd_price_feed"
        )

    else:
        deployMocks()
        pricefeed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        pricefeed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print("contracts deployed")
    return fund_me

def main():
    deploy_fund_me()
