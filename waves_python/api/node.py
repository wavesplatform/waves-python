from typing import List, Any

import requests

from waves_python.api.profile import Profile
from waves_python.account.address import Address, AddressList, AddressBalance, AddressData, AddressKeys, AddressScriptInfo, \
    AddressScriptInfoMeta
from waves_python.common.alias import Alias
from waves_python.common.asset_id import AssetId, AssetIds
from waves_python.common.exceptions import NodeException
from waves_python.common.id import Id, Ids
from waves_python.transaction.transaction_info import TransactionInfo
from waves_python.transaction.transaction_with_status import TransactionWithStatus
from waves_python.model.asset_balance import AssetBalance, AssetDistribution
from waves_python.model.asset_details import AssetDetails
from waves_python.model.block import Block
from waves_python.model.block_headers import BlockHeaders
from waves_python.model.blockchain_rewards import BlockchainRewards
from waves_python.model.history_balance import HistoryBalance
from waves_python.model.lease_info import LeaseInfo
from waves_python.transaction.transaction import Transaction


class Node:

    def __init__(self, profile: Profile) -> None:
        self.uri = profile.value
        self.timeout = 60 * 1000
        self.headers = {'accept': 'application/json', 'content-type': 'application/json'}

    def get(self, url: str):
        response = requests.get(url=url, timeout=self.timeout, headers=self.headers)
        return response.json()

    def post(self, url: str, node_model: Any):
        response = requests.post(url=url,
                                 data=node_model.to_json(),
                                 timeout=self.timeout,
                                 headers=self.headers)
        return response.json()

    # ===============
    #    ADDRESSES
    # ===============

    def get_addresses(self) -> List[Address]:
        response_json = self.get(f'{self.uri}/addresses')
        return [Address(address_str) for address_str in response_json]

    def get_balance_for_indexes(self, idx_from: int, idx_to: int) -> List[Address]:
        response_json = self.get(f'{self.uri}/addresses/seq/{idx_from}/{idx_to}')
        return [Address(address_str) for address_str in response_json]

    def get_address_balance(self, address: Address) -> int:
        response_json = self.get(f'{self.uri}/addresses/balance/{address.base58_str}')
        return response_json.get('balance')

    def get_addresses_balances(self, addresses: List[Address], height: int) -> List[int]:
        response_json = self.post(url=f'{self.uri}/addresses/balance',
                                  node_model=AddressList(addresses=[address.base58_str for address in addresses],
                                                         height=height))
        if response_json.get('error'):
            return NodeException.from_dict(response_json)
        return response_json

    def get_address_balance_details(self, address: Address) -> AddressBalance:
        response_json = self.get(f'{self.uri}/addresses/balance/details/{address.base58_str}')
        if response_json.get('error'):
            return NodeException.from_dict(response_json)
        return AddressBalance.from_dict(response_json)

    def get_address_data(self, address: Address, matches: str = None) -> List[AddressData]:
        url = f'{self.uri}/addresses/data/{address.base58_str}'
        url += f'?matches={matches}' if matches else ''
        response_json = self.get(url)
        if response_json.get('error'):
            return NodeException.from_dict(response_json)
        return [AddressData.from_dict(resp) for resp in response_json]

    def get_address_data_by_keys(self, address: Address, keys: List[str] = None) -> List[AddressData]:
        response_json = self.post(f'{self.uri}/addresses/data/{address.base58_str}', AddressKeys(keys=keys))
        if response_json.get('error'):
            return NodeException.from_dict(response_json)
        return [AddressData.from_dict(resp) for resp in response_json]

    def get_address_data_by_key(self, address: Address, key: str) -> AddressData:
        response_json = self.get(f'{self.uri}/addresses/data/{address.base58_str}/{key}')
        return AddressData.from_dict(response_json)

    def get_address_script_info(self, address: Address) -> AddressScriptInfo:
        response_json = self.get(f'{self.uri}/addresses/scriptInfo/{address.base58_str}')
        return AddressScriptInfo.from_dict(response_json)

    def get_address_script_meta(self, address: Address) -> AddressScriptInfoMeta:
        response_json = self.get(f'{self.uri}/addresses/scriptInfo/{address.base58_str}/meta')
        return AddressScriptInfoMeta.from_dict(response_json)

    # ===============
    #    ALIAS
    # ===============

    def get_aliases_by_address(self, address: Address) -> List[Alias]:
        response_json = self.get(f'{self.uri}/alias/by-address/{address.base58_str}')
        if response_json.get('error'):
            return NodeException.from_dict(response_json)
        return [Alias(name=resp) for resp in response_json]

    def get_address_by_alias(self, alias: Alias) -> Address:
        response_json = self.get(f'{self.uri}/alias/by-alias/{alias.name}')
        if response_json.get('error'):
            return NodeException.from_dict(response_json)
        return Address(base58_str=response_json.get('address'))

    # ===============
    #    ASSETS
    # ===============

    def get_asset_distribution(self, asset_id: AssetId, height: int, limit: int = 100, after: str = None) -> AssetDistribution:
        url = f'{self.uri}/assets/{asset_id.base58_str}/distribution/{height}/limit/{limit}'
        url += f'?after={after}' if after else ''
        response_json = self.get(url)
        if response_json.get('error'):
            return NodeException.from_dict(response_json)
        return AssetDistribution.from_dict(response_json)

    def get_assets_balance(self, address: Address) -> List[AssetBalance]:
        response_json = self.get(f'{self.uri}/assets/balance/{address.base58_str}')
        return [AssetBalance.from_dict(resp) for resp in response_json.get('balances')]

    def get_asset_balance(self, address: Address, asset_id: AssetId) -> float:
        response_json = self.get(f'{self.uri}/assets/balance/{address.base58_str}/{asset_id.base58_str}')
        if response_json.get('error'):
            return NodeException.from_dict(response_json)
        return response_json.get('balance')

    def get_asset_details(self, asset_id: AssetId) -> AssetDetails:
        response_json = self.get(f'{self.uri}/assets/details/{asset_id.base58_str}?full=true')
        return AssetDetails.from_dict(response_json)

    def get_assets_details(self, asset_ids: AssetIds) -> List[AssetDetails]:
        response_json = self.post(f'{self.uri}/assets/details?full=true', asset_ids)
        if not isinstance(response_json, list) and response_json.get('error'):
            return NodeException.from_dict(response_json)
        return [AssetDetails.from_dict(resp) for resp in response_json]

    def get_nft(self, address: Address, limit: int = 100, after: AssetId = None) -> List[AssetDetails]:
        url = f'{self.uri}/assets/nft/{address.base58_str}/limit/{limit}'
        url += f'?after={after.base58_str}' if after else ''
        response_json = self.get(url)
        if not isinstance(response_json, list) and response_json.get('error'):
            return NodeException.from_dict(response_json)
        return [AssetDetails.from_dict(resp) for resp in response_json]

    # ===============
    #    BLOCKCHAIN
    # ===============

    def get_blockchain_rewards(self, height: int = None):
        url = f'{self.uri}/blockchain/rewards/'
        url += f'{height}' if height else ''
        response_json = self.get(url)
        return BlockchainRewards.from_dict(response_json)

    # ===============
    #    BLOCKS
    # ===============

    def get_blocks_height(self) -> int:
        response_json = self.get(f'{self.uri}/blocks/height')
        return response_json.get('height')

    def get_block_height_by_id(self, block_id: str) -> int:
        response_json = self.get(f'{self.uri}/blocks/height/{block_id}')
        if response_json.get('error'):
            return NodeException.from_dict(response_json)
        return response_json.get('height')

    def get_block_height_by_timestamp(self, timestamp: int) -> int:
        response_json = self.get(f'{self.uri}/blocks/heightByTimestamp/{timestamp}')
        return response_json.get('height')

    def get_blocks_delay(self, start_block_id: str, blocks_num: int) -> int:
        response_json = self.get(f'{self.uri}/blocks/delay/{start_block_id}/{blocks_num}')
        if response_json.get('error'):
            return NodeException.from_dict(response_json)
        return response_json.get('delay')

    def get_block_headers_by_height(self, height: int) -> BlockHeaders:
        response_json = self.get(f'{self.uri}/blocks/headers/at/{height}')
        if response_json.get('error'):
            return NodeException.from_dict(response_json)
        return BlockHeaders.from_dict(response_json)

    def get_block_headers_by_id(self, block_id: str) -> BlockHeaders:
        response_json = self.get(f'{self.uri}/blocks/headers/{block_id}')
        return BlockHeaders.from_dict(response_json)

    def get_blocks_headers(self, height_from: int, height_to: int) -> List[BlockHeaders]:
        response_json = self.get(f'{self.uri}/blocks/headers/seq/{height_from}/{height_to}')
        if response_json.get('error'):
            return NodeException.from_dict(response_json)
        return [BlockHeaders.from_dict(resp) for resp in response_json]

    def get_last_block_headers(self) -> BlockHeaders:
        response_json = self.get(f'{self.uri}/blocks/headers/last')
        return BlockHeaders.from_dict(response_json)

    def get_block_by_height(self, height: int) -> Block:
        response_json = self.get(f'{self.uri}/blocks/at/{height}')
        if response_json.get('error'):
            return NodeException.from_dict(response_json)
        return Block.from_dict(response_json)

    def get_block_by_id(self, block_id: str) -> Block:
        response_json = self.get(f'{self.uri}/blocks/{block_id}')
        if response_json.get('error'):
            return NodeException.from_dict(response_json)
        return Block.from_dict(response_json)

    def get_blocks(self, height_from: int, height_to: int) -> List[Block]:
        response_json = self.get(f'{self.uri}/blocks/seq/{height_from}/{height_to}')
        return [Block.from_dict(resp) for resp in response_json]

    def get_last_block(self) -> Block:
        response_json = self.get(f'{self.uri}/blocks/last')
        return Block.from_dict(response_json)

    def get_blocks_by_address(self, address: Address, height_from: int, height_to: int) -> List[Block]:
        response_json = self.get(f'{self.uri}/blocks/address/{address.base58_str}/{height_from}/{height_to}')
        if response_json.get('error'):
            return NodeException.from_dict(response_json)
        return [Block.from_dict(resp) for resp in response_json]

    # ===============
    #    NODE
    # ===============

    def get_version(self) -> str:
        response_json = self.get(f'{self.uri}/node/version')
        return response_json.get('version')

    # ===============
    #    DEBUG
    # ===============

    def get_balance_history(self, address: Address) -> List[HistoryBalance]:
        response_json = self.get(f'{self.uri}/debug/balances/history/{address.base58_str}')
        return [HistoryBalance.from_dict(resp) for resp in response_json]

    # ===============
    #    LEASING
    # ===============

    def get_active_leases(self, address: Address) -> List[LeaseInfo]:
        response_json = self.get(f'{self.uri}/leasing/active/{address.base58_str}')
        return [LeaseInfo.from_dict(resp) for resp in response_json]

    def get_lease_info_by_id(self, lease_id: Id) -> LeaseInfo:
        response_json = self.get(f'{self.uri}/leasing/info/{lease_id.base58_str}')
        return LeaseInfo.from_dict(response_json)

    def get_leases_info(self, lease_ids: Ids) -> List[LeaseInfo]:
        response_json = self.post(f'{self.uri}/leasing/info', lease_ids)
        if response_json.get('error'):
            return NodeException.from_dict(response_json)
        return [LeaseInfo.from_dict(resp) for resp in response_json]

    # ===============
    #  TRANSACTIONS
    # ===============

    def get_transaction_info(self, tx_id: Id):
        response_json = self.get(f'{self.uri}/transactions/info/{tx_id.base58_str}')
        if not isinstance(response_json, list) and response_json.get('error'):
            return NodeException.from_dict(response_json)
        return TransactionInfo.from_dict(response_json)

    def get_transactions_by_address(self, address: Address, limit: int = 100, after_id: Id = None) -> List[Transaction]:
        url = f'{self.uri}/transactions/address/{address.base58_str}/limit/{limit}'
        url += f'?after={after_id.base58_str}' if after_id else ''
        response_json = self.get(url)
        if isinstance(response_json, list):
            response_json = response_json[0]
        if not isinstance(response_json, list) and response_json.get('error'):
            return NodeException.from_dict(response_json)

        return [TransactionInfo.from_dict(resp) for resp in response_json]

    def get_transaction_status(self, tx_id: Id) -> TransactionWithStatus:
        response_json = self.get(f'{self.uri}/transactions/status?id={tx_id.base58_str}')
        if not isinstance(response_json, list) and response_json.get('error'):
            return NodeException.from_dict(response_json)
        return TransactionWithStatus.from_dict(response_json[0])

    def get_transactions_status(self, tx_ids: Ids):
        response_json = self.post(f'{self.uri}/transactions/status', tx_ids)
        return [TransactionWithStatus.from_dict(resp) for resp in response_json]

    def get_unconfirmed_transaction(self, tx_id: Id):
        response_json = self.get(f'{self.uri}/transactions/unconfirmed/info/{tx_id.base58_str}')
        if not isinstance(response_json, list) and response_json.get('error'):
            return NodeException.from_dict(response_json)
        return TransactionInfo.from_dict(response_json)

    def get_unconfirmed_transactions(self):
        response_json = self.get(f'{self.uri}/transactions/unconfirmed')
        return [TransactionInfo.from_dict(resp) for resp in response_json]

    def get_unconfirmed_transaction_size(self) -> int:
        response_json = self.get(f'{self.uri}/transactions/unconfirmed/size')
        return response_json.get('size')

    # ===============
    #     UTILS
    # ===============

    def generate_random_seed(self) -> str:
        response_json = self.get(f'{self.uri}/utils/seed')
        return response_json.get('seed')
