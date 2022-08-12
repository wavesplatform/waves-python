from src.api.node import Node
from src.api.profile import Profile
from src.account.address import Address, AddressList

node = Node(Profile.TESTNET)
# test
address = Address.from_str("3Mx3zmXrMcLFCafMuPtXAzR4ZPVeZYb6qLz")
# stage
# address = Address.from_str("3Mi63XiwniEj6mTC557pxdRDddtpj7fZMMw")
# balance = node.get_balance(address)
# add = node.get_addresses()
# al = node.get_aliases_by_address(address)
# ver = node.get_version()
# lease = node.get_active_leases(address)
# print(f"Balance: {balance}")
# print(f"addresses: {add}")
# print(f"aliases: {al}")
# print(f"lease: {lease}")

# print(node.get_address_balance(address))
# print(node.get_address_balance_details(address))
# print(node.get_address_data_by_key(address, "test"))
# print(node.get_address_script_info(address))
# print(node.get_address_script_meta(address))
# print(node.get_aliases_by_address(address))

# print(node.get_blockchain_rewards())
#
#
# print(node.get_version())


# print(node.get_balance_history(address))


# print(node.get_blocks_height())

# print(node.get_last_block())
# print(node.get_block_height_by_timestamp(1000))

asset_id = 'BjV9C4wfZmtBMfAPMHyZGqPGTrNpx6ZHAryfHij7grT'

print(node.get_assets_balance(address))

