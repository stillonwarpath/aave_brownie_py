from brownie import accounts, network, config

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local", "mainnet-fork"]
FORKER_LOCAL_ENVIRONMENT = ["mainnet-fork-dev"]


def get_account(index=None, id=None):
    # accounts[0] Ganache accounts
    # accounts.add("env")
    # accounts.load("id")
    if index:
        return accounts[index]

    if id:
        return accounts.load(id)

    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKER_LOCAL_ENVIRONMENT
    ):
        return accounts[0]

    return accounts.add(config["wallets"]["from_key"])
