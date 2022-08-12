from typing import List

from pydantic import Field

from src.model.lease_info import LeaseInfo
from src.model.node_model import NodeModel


class StateChanges(NodeModel):
    data: List[DataEntry] = Field()
    transfers: List[ScriptTransfer] = Field()
    issues: List[IssueAction] = Field()
    reissues: List[ReissueAction] = Field()
    burns: List[BurnAction] = Field()
    sponsor_fees: List[SponsorFeeAction] = Field(alias='sponsorFees')
    leases: List[LeaseInfo] = Field()
    lease_cancels: List[LeaseInfo] = Field(alias='leaseCancels')
    invokes: List[InvokeAction] = Field()
    error: Error = Field()
