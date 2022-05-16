from brownie import accounts, config, OurToken, network
from scripts.helpful_scripts import get_account
from web3 import Web3

inital_supply = Web3.toWei(1000, "ether")


def deploy_our_token(supply):
    account = get_account()
    our_token = OurToken.deploy(supply, {"from": account}, publish_source=True)
    print(our_token.name())


def main():
    deploy_our_token(inital_supply)
