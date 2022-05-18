from brownie import (
    accounts,
    network,
    config,
)
import eth_utils

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "hardhat", "local-ganache"]


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])


def encode_function_data(initializer=None, *args):
    # initializer=box.store, 1,2,3,4,5,6,7 etc (for any optional args to pass to initializer function)
    # returns the encoded bytes or an empty hex string if no args
    if len(args) == 0 or not initializer:
        return eth_utils.to_bytes(hexstr="0x")
    return initializer.encode_input(*args)
