from scripts.helpful_scripts import (
    get_account,
    upgrade,
)
from brownie import (
    network,
    BoxV2,
    Contract,
    TransparentUpgradeableProxy,
    ProxyAdmin,
    config,
)


def main():
    account = get_account()
    print(f"Deploying to {network.show_active()}")

    # Upgrades the box contract to BoxV2
    box_v2 = BoxV2.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    proxy = TransparentUpgradeableProxy[-1]
    proxy_admin = ProxyAdmin[-1]

    upgrade_transaction = upgrade(account, proxy, box_v2.address, proxy_admin)
    upgrade_transaction.wait(1)
    print("Proxy has been upgraded")

    proxy_box = Contract.from_abi("BoxV2", proxy.address, BoxV2.abi)
    tx = proxy_box.increment({"from": account})
    tx.wait(1)
    print(proxy_box.retrieve())
