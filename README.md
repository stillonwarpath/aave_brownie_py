1. Swap our ETH for WETH
2. Deposit some ETH into Aave
3. Borrow some asset with the ETH collateral
   1. Sell that borrowed asset. (Short selling)
4. Repay everything back

Testing:

Default Testing Network:
Development with Mocking (For instance Mock for oracles and their responses)

If you have no oracles:
You can use mainnet-fork for testing

Integration test: Kovan
Unit tests: Mainnet-fork
