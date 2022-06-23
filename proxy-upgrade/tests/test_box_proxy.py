from brownie import Box, TransparentUpgradeableProxy, Contract
from scripts.helpful_scripts import (
    get_account,
)
from scripts.deploy import main as deploy_box_and_proxy


def test_proxy_delegates_calls():
    account = get_account()
    deploy_box_and_proxy()
    proxy = TransparentUpgradeableProxy[-1]
    proxy_box = Contract.from_abi("Box", proxy.address, Box.abi)
    assert proxy_box.retrieve() == 0
    tx = proxy_box.store(1, {"from": account})
    tx.wait(1)
    assert proxy_box.retrieve() == 1
