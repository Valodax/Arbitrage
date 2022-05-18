from brownie import (
    Box,
    TransparentUpgradeableProxy,
    ProxyAdmin,
    config,
    network,
    Contract,
)
from scripts.helpful_scripts import encode_function_data, get_account


def main():
    account = get_account()
    print(f"Deploying to {network.show_active()}")

    # deploys box
    box = Box.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    proxy_admin = ProxyAdmin.deploy(
        {"from": account},
    )
    # initializer = box.store, 1
    box_encoded_initializer_function = encode_function_data()
    proxy = TransparentUpgradeableProxy.deploy(
        box.address,
        proxy_admin.address,
        box_encoded_initializer_function,
        {"from": account, "gas_limit": 1000000},
    )
    print(f"Proxy deployed to {proxy}. You can now upgrade it to BoxV2")
    proxy_box = Contract.from_abi("Box", proxy.address, Box.abi)
    print(f"The initial value in the box is: {proxy_box.retrieve()}")
