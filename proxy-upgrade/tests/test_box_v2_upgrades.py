from scripts.helpful_scripts import (
    get_account,
    upgrade,
)
from brownie import (
    BoxV2,
    Contract,
    exceptions,
    TransparentUpgradeableProxy,
    ProxyAdmin,
)
import pytest
from scripts.deploy import main as deploy_box_and_proxy


def test_proxy_upgrades():
    account = get_account()
    deploy_box_and_proxy()
    proxy = TransparentUpgradeableProxy[-1]
    proxy_admin = ProxyAdmin[-1]
    # deploy boxV2
    box_v2 = BoxV2.deploy({"from": account})
    proxy_box = Contract.from_abi("BoxV2", proxy.address, BoxV2.abi)
    # tries to call increment (should fail)
    with pytest.raises(exceptions.VirtualMachineError):
        tx = proxy_box.increment({"from": account})
        tx.wait(1)
    # upgrades
    upgrade(account, proxy, box_v2, proxy_admin)
    assert proxy_box.retrieve() == 0
    # increments
    tx2 = proxy_box.increment({"from": account})
    tx2.wait(1)
    assert proxy_box.retrieve() == 1
