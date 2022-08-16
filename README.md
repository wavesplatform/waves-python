## Waves-python

Python client library for interacting with Waves blockchain platform. 

## Package
waves-python [![PyPI version](https://badge.fury.io/py/waves-python.svg)](https://badge.fury.io/py/waves-python)

## Requirements
- [Python](https://www.python.org/) >= 3.9


## Installation
```bash
pip install waves-python
```

## Usage

- Node basics:

```python
from waves_python.api.node import Node
from waves_python.api.profile import Profile

node = Node(Profile.TESTNET)
print(f'Node version: {node.get_version()}')
```

- Addresses:

Getting balance:
```python
from waves_python.account.address import Address
from waves_python.api.node import Node
from waves_python.api.profile import Profile


address = Address(base58_str="3Mx3zmXrMcLFCafMuPtXAzR4ZPVeZYb6qLz")
node = Node(Profile.TESTNET)
balance = node.get_address_balance(address)
print(f'Balance: {balance}')

```

Balance details:
```python
from waves_python.account.address import Address
from waves_python.api.node import Node
from waves_python.api.profile import Profile


address = Address(base58_str="3Mx3zmXrMcLFCafMuPtXAzR4ZPVeZYb6qLz")
node = Node(Profile.TESTNET)
address_balance_details = node.get_address_balance_details(address)

print(f"address: {address_balance_details.address}")
print(f"regular: {address_balance_details.regular}")
print(f"generating: {address_balance_details.address}")
print(f"available: {address_balance_details.available}")
print(f"effective: {address_balance_details.effective}")
```

Debug:
```python
from waves_python.account.address import Address
from waves_python.api.node import Node
from waves_python.api.profile import Profile


address = Address(base58_str="3Mx3zmXrMcLFCafMuPtXAzR4ZPVeZYb6qLz")
node = Node(Profile.TESTNET)
balance_history = node.get_balance_history(address)
for history in balance_history:
    print(f"Height: {history.height}, balance: {history.balance}")
```


- Reading transactions with limit:

```python
from waves_python.account.address import Address
from waves_python.api.node import Node
from waves_python.api.profile import Profile


address = Address(base58_str="3Mx3zmXrMcLFCafMuPtXAzR4ZPVeZYb6qLz")
node = Node(Profile.TESTNET)
transactions = node.get_transactions_by_address(address, limit=20)
for transaction in transactions:
    print(f"id: {transaction.id.base58_str}")
    print(f"public_key: {transaction.public_key}")
    print(f"chain_id: {transaction.chain_id}")
    print(f"version: {transaction.version}")
    print(f"fee: {transaction.fee}")
    print(f"timestamp: {transaction.timestamp}")
    print(f"sender: {transaction.sender}")
    print(f"type: {transaction.type}")
    print(f"application_status: {transaction.application_status.value}")
    print(f"height: {transaction.height}")
```
Getting transaction status by id:
```python
from waves_python.api.node import Node
from waves_python.api.profile import Profile
from waves_python.common.id import Id


node = Node(Profile.TESTNET)
tx_id = Id('C52dEQZukj4YMM8vuiruJB5uJk88YFdLwVci4869ytLd')
transaction_with_status = node.get_transaction_status(tx_id)
print(transaction_with_status.application_status.value)
```

- Getting assets:

```python
from waves_python.account.address import Address
from waves_python.api.node import Node
from waves_python.api.profile import Profile

address = Address(base58_str="3Mx3zmXrMcLFCafMuPtXAzR4ZPVeZYb6qLz")
node = Node(Profile.TESTNET)
assets = node.get_assets_balance(address)
for asset in assets:
    print(f"asset_id: {asset.asset_id}")
    print(f"balance: {asset.balance}")
    print(f"reissuable: {asset.reissuable}")
    print(f"min_sponsored_asset_fee: {asset.min_sponsored_asset_fee}")
    print(f"sponsor_balance: {asset.sponsor_balance}")
    print(f"quantity: {asset.quantity}")
```


- Working with Blocks:

```python
from waves_python.account.address import Address
from waves_python.api.node import Node
from waves_python.api.profile import Profile

address = Address(base58_str="3Mx3zmXrMcLFCafMuPtXAzR4ZPVeZYb6qLz")
node = Node(Profile.TESTNET)
last_block = node.get_last_block()
print(f"version: {last_block.version}")
print(f"timestamp: {last_block.timestamp}")
print(f"reference: {last_block.reference}")
print(f"nxt_consensus: {last_block.nxt_consensus}")
print(f"transactions_root: {last_block.transactions_root}")
print(f"id: {last_block.id}")
print(f"features: {last_block.features}")
print(f"desired_reward: {last_block.desired_reward}")
print(f"generator: {last_block.generator.base58_str}")
print(f"signature: {last_block.signature}")
print(f"size: {last_block.size}")
print(f"transaction_count: {last_block.transaction_count}")
print(f"height: {last_block.height}")
print(f"total_fee: {last_block.total_fee}")
```
