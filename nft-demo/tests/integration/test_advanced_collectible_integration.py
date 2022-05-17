from brownie import network, AdvancedCollectible
import pytest
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.advanced_collectible.deploy_and_create import deploy_and_create
import time


def test_can_create_advanced_collectible_integration():
    # Arrange
    # deploy the contract, create an NFT and get a random breed back
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for integration local testing")
    # Act
    advanced_collectible, creation_transaction = deploy_and_create()
    time.sleep(180)
    # Assert
    assert advanced_collectible.tokenCounter() == 1
