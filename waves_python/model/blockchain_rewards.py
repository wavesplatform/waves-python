from dataclasses import dataclass

from dataclasses_json import dataclass_json, LetterCase

from waves_python.model.node_model import NodeModel
from waves_python.model.votes import Votes


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class BlockchainRewards(NodeModel):
    height: int
    total_waves_amount: float
    current_reward: float
    min_increment: float
    term: int
    next_check: int
    voting_interval_start: int
    voting_interval: int
    voting_threshold: int
    votes: Votes

