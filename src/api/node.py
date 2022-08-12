from typing import List

import requests

from src.api.profile import Profile
from src.account.address import Address, AddressList, AddressBalance, AddressData, AddressKeys, AddressScriptInfo, \
    AddressScriptInfoMeta
from src.common.alias import Alias
from src.common.asset_id import AssetId, AssetIds
from src.common.id import Id, Ids
from src.model.asset_balance import AssetBalance
from src.model.blockchain_rewards import BlockchainRewards
from src.model.history_balance import HistoryBalance
from src.model.node_model import NodeModel
from src.transaction.transaction import Transaction


class Node:

    def __init__(self, profile: Profile) -> None:
        self.uri = profile.value
        self.timeout = 60 * 1000
        self.headers = {'content-type': 'application/json'}

    def get(self, url: str):
        response = requests.get(url=url, timeout=self.timeout, headers=self.headers)
        return response.json()

    def post(self, url: str, node_model: NodeModel):
        response = requests.post(url=url,
                                 json=node_model.json(by_alias=True),
                                 timeout=self.timeout,
                                 headers=self.headers)
        return response.json()

    # ===============
    #    ADDRESSES
    # ===============

    def get_addresses(self) -> List[Address]:
        response_json = self.get(f'{self.uri}/addresses')
        return [Address.from_str(address_str) for address_str in response_json]

    def get_balance_for_indexes(self, idx_from: int, idx_to: int) -> List[Address]:
        response_json = self.get(f'{self.uri}/addresses/seq/{idx_from}/{idx_to}')
        return [Address.from_str(address_str) for address_str in response_json]

    def get_address_balance(self, address: Address) -> int:
        response_json = self.get(f'{self.uri}/addresses/balance/{address.to_str()}')
        return response_json.get('balance')

    def get_addresses_balances(self, addresses: List[Address], height: int) -> List[int]:
        response_json = self.post(url=f'{self.uri}/addresses/balance',
                                  node_model=AddressList(addresses=[address.to_str() for address in addresses], height=height))
        return response_json

    def get_address_balance_details(self, address: Address) -> AddressBalance:
        response_json = self.get(f'{self.uri}/addresses/balance/details/{address.to_str()}')
        return AddressBalance(**response_json)

    def get_address_data(self, address: Address, matches: str = None) -> List[AddressData]:
        url = f'{self.uri}/addresses/data/{address.to_str()}'
        url += f'?matches={matches}' if matches else ''
        response_json = self.get(url)
        return [AddressData(**resp) for resp in response_json]

    def get_address_data_by_keys(self, address: Address, keys: List[str] = None) -> List[AddressData]:
        response_json = self.post(f'{self.uri}/addresses/data/{address.to_str()}', AddressKeys(keys=keys))
        return [AddressData(**resp) for resp in response_json]

    def get_address_data_by_key(self, address: Address, key: str) -> AddressData:
        response_json = self.get(f'{self.uri}/addresses/data/{address.to_str()}/{key}')
        return AddressData(**response_json)

    def get_address_script_info(self, address: Address) -> AddressScriptInfo:
        response_json = self.get(f'{self.uri}/addresses/scriptInfo/{address.to_str()}')
        return AddressScriptInfo(**response_json)

    def get_address_script_meta(self, address: Address) -> AddressScriptInfoMeta:
        response_json = self.get(f'{self.uri}/addresses/scriptInfo/{address.to_str()}/meta')
        return AddressScriptInfoMeta(**response_json)

    # ===============
    #    ALIAS
    # ===============

    def get_aliases_by_address(self, address: Address) -> List[str]:
        response_json = self.get(f'{self.uri}/alias/by-address/{address.to_str()}')
        return response_json

    def get_address_by_alias(self, alias: Alias):
        response_json = self.get(f'{self.uri}/alias/by-alias/{alias.name}')
        return response_json

    # ===============
    #    ASSETS
    # ===============

    def get_asset_distribution(self, asset_id: AssetId, height: int, limit: int = 100, after: str = None):
        url = f'{self.uri}/assets/{asset_id.to_str()}/distribution/{height}/limit/{limit}'
        url += f'?after={after}' if after else ''
        response_json = self.get(url)
        return response_json

    def get_assets_balance(self, address: Address):
        response_json = self.get(f'{self.uri}/assets/balance/{address.to_str()}')
        return [AssetBalance(**resp) for resp in response_json.get('balances')]

    def get_asset_balance(self, address: Address, asset_id: AssetId):
        response_json = self.get(f'{self.uri}/assets/balance/{address.to_str()}/{asset_id.to_str()}')
        return response_json

    def get_assets_details(self, asset_id: AssetId):
        response_json = self.get(f'{self.uri}/assets/details/{asset_id.to_str()}?full=true')
        return response_json

    def get_asset_details(self, asset_ids: AssetIds):
        response_json = self.post(f'{self.uri}/assets/details?full=true', asset_ids)
        return response_json

    def get_nft(self, address: Address, limit: int = 100, after: AssetId = None):
        url = f'{self.uri}/assets/nft/{address.to_str()}/limit/{limit}'
        url += f'?after={after.to_str()}' if after else ''
        response_json = self.get(url)
        return response_json

    # ===============
    #    BLOCKCHAIN
    # ===============

    def get_blockchain_rewards(self, height: int = None):
        url = f'{self.uri}/blockchain/rewards/'
        url += f'{height}' if height else ''
        response_json = self.get(url)
        return BlockchainRewards(**response_json)

    # ===============
    #    BLOCKS
    # ===============

    def get_blocks_height(self) -> int:
        response_json = self.get(f'{self.uri}/blocks/height')
        return response_json.get('height')

    def get_block_height_by_id(self, block_id: str):
        response_json = self.get(f'{self.uri}/blocks/height/{block_id}')
        return response_json

    def get_block_height_by_timestamp(self, timestamp: int) -> int:
        response_json = self.get(f'{self.uri}/blocks/heightByTimestamp/{timestamp}')
        return response_json.get('height')

    def get_blocks_delay(self, start_block_id: str, blocks_num: int) -> int:
        response_json = self.get(f'{self.uri}/blocks/delay/{start_block_id}/{blocks_num}')
        return response_json.get('delay')

    def get_block_headers_by_height(self, height: int):
        response_json = self.get(f'{self.uri}/blocks/headers/at/{height}')
        return response_json

    def get_block_headers_by_id(self, block_id: str):
        response_json = self.get(f'{self.uri}/blocks/headers/{block_id}')
        return response_json

    def get_blocks_headers(self, height_from: int, height_to: int):
        response_json = self.get(f'{self.uri}/blocks/headers/seq/{height_from}/{height_to}')
        return response_json

    def get_last_block_headers(self):
        response_json = self.get(f'{self.uri}/blocks/headers/last')
        return response_json

    def get_block_by_height(self, height: int):
        response_json = self.get(f'{self.uri}/blocks/at/{height}')
        return response_json

    def get_block_by_id(self, id: Id):
        response_json = self.get(f'{self.uri}/blocks/{id.to_str()}')
        return response_json

    def get_blocks(self, height_from: int, height_to: int):
        response_json = self.get(f'{self.uri}/blocks/seq/{height_from}/{height_to}')
        return response_json

    def get_last_block(self):
        response_json = self.get(f'{self.uri}/blocks/last')
        return response_json

    def get_blocks_by_address(self, address: Address, height_from: int, height_to: int):
        response_json = self.get(f'{self.uri}/blocks/address/{address.to_str()}/{height_from}/{height_to}')
        return response_json

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
        response_json = self.get(f'{self.uri}/debug/balances/history/{address.to_str()}')
        return [HistoryBalance(**resp) for resp in response_json]

    # ===============
    #    LEASING
    # ===============

    def get_active_leases(self, address: Address):
        response_json = self.get(f'{self.uri}/leasing/active/{address.to_str()}')
        return response_json

    def get_lease_info_by_id(self, lease_id: Id):
        response_json = self.get(f'{self.uri}/leasing/info/{lease_id.to_str()}')
        return response_json

    def get_leases_info(self, lease_ids: Ids):
        response_json = self.post(f'{self.uri}/leasing/info', lease_ids)
        return response_json

    # ===============
    #  TRANSACTIONS
    # ===============

    def calculate_transaction_fee(self, transaction: Transaction):
        response_json = self.post(f'{self.uri}/transactions/calculateFee', transaction)
        return response_json

    def get_transaction_info(self, tx_id: Id):
        response_json = self.get(f'{self.uri}/transactions/info/{tx_id.to_str()}')
        return response_json

    def get_transactions_by_address(self, address: Address, limit: int = 100, after_id: Id = None):
        url = f'{self.uri}/transactions/address/{address.to_str()}/limit/{limit}'
        url += f'?after={after_id.to_str()}' if after_id else ''
        response_json = self.get(url)
        return response_json

    def get_transaction_status(self, tx_id: Id):
        response_json = self.get(f'{self.uri}/transactions/status?id={tx_id.to_str()}')
        return response_json

    def get_transactions_status(self, tx_ids: Ids):
        response_json = self.post(f'{self.uri}/transactions/status', tx_ids)
        return response_json

    def get_unconfirmed_transaction(self, tx_id: Id):
        response_json = self.get(f'{self.uri}/transactions/unconfirmed/info/{tx_id.to_str()}')
        return response_json

    def get_unconfirmed_transactions(self):
        response_json = self.get(f'{self.uri}/transactions/unconfirmed')
        return response_json

    def get_unconfirmed_transaction_size(self):
        response_json = self.get(f'{self.uri}/transactions/unconfirmed/size')
        return response_json

    # ===============
    #     UTILS
    # ===============

    def serialize_transaction(self, transaction: Transaction):
        response_json = self.post(f'{self.uri}/utils/transactionSerialize', transaction)
        return response_json

    def get_eth_to_waves_asset(self, asset: str):
        response_json = self.get(f'{self.uri}/eth/assets?id={asset}')
        return response_json
