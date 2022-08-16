Python client library for interacting with Waves blockchain platform.  

## Package
waves-python [![PyPI version](https://badge.fury.io/py/waves-python.svg)](https://badge.fury.io/py/waves-python)

## Installation
```bash
pip install waves-python
```

## Usage

- Node basics:

```python
from waves_python.api.node import Node, Profile


node = Node(Profile.TESTNET)
print(f'Node version: {node.get_version()}')
```

- Addresses:

```python
from waves_python.api.node import Node, Profile
from waves_python.account.address import Address


address = Address(base58_str='3Mx3zmXrMcLFCafMuPtXAzR4ZPVeZYb6qLz')
node = Node(Profile.TESTNET)
balance = node.get_address_balance(address)
print(f'Balance: {balance}')
```

## Requirements
- [Python](https://www.python.org/) >= 3.9
