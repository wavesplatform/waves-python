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
node = Node(Profile.TESTNET)
print(f'Node version: {node.get_version()}')
```

- Addresses:

```python
address = Address.from_str('your_encoded_address')
balance = node.get_balance(address)
print(f'Balance: {balance}')
```

## Requirements
- [Python](https://www.python.org/) >= 3.9
