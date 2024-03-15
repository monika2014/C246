from web3 import Web3
# Connect to the Ethereum network using a provider (e.g., Infura)
web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/cded6e6690d04259b05137dd10b170c3'))
gas_prices = web3.eth.gas_price
# Calculate gas prices at different levels
safe_low_gas_price = int(gas_prices * 0.9)  # 90% of the current gas price
average_gas_price = int(gas_prices * 1.0)   # Same as the current gas price
fast_gas_price = int(gas_prices * 1.1)      # 110% of the current gas price
fastest_gas_price = int(gas_prices * 1.2)   # 120% of the current gas price
# Convert gas prices from Wei to Gwei
safe_low_gas_price_gwei = web3.from_wei(safe_low_gas_price, 'gwei')
average_gas_price_gwei = web3.from_wei(average_gas_price, 'gwei')
fast_gas_price_gwei = web3.from_wei(fast_gas_price, 'gwei')
fastest_gas_price_gwei = web3.from_wei(fastest_gas_price, 'gwei')
print("Safe Low Gas Price (Gwei):", safe_low_gas_price_gwei)
print(f"Average Gas Price (Gwei):", average_gas_price_gwei)
print(f"Fast Gas Price (Gwei):", fast_gas_price_gwei)
print(f"Fastest Gas Price (Gwei): {fastest_gas_price_gwei}")
# Conversion of gas price into ether and dollars
gas_price = web3.eth.gas_price
print("Gas Price in Gwei", gas_price)
gas_price_in_ether = (gas_price/10**18)
print(f'gas price in ether: {gas_price_in_ether:.22f}')
gas_price_in_dollar = gas_price_in_ether * 3105.35
print("gas price in dollar:",gas_price_in_dollar)