from pydantic import Field

from src.model.node_model import NodeModel
from src.model.votes import Votes


class BlockchainRewards(NodeModel):
    height: int = Field()
    total_waves_amount: float = Field(alias='totalWavesAmount')
    current_reward: float = Field(alias='currentReward')
    min_increment: float = Field(alias='minIncrement')
    term: int = Field()
    next_check: int = Field(alias='nextCheck')
    voting_interval_start: int = Field(alias='votingIntervalStart')
    voting_interval: int = Field(alias='votingInterval')
    voting_threshold: int = Field(alias='votingThreshold')
    votes: Votes = Field()

