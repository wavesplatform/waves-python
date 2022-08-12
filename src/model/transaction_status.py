from pydantic import Field

from src.model.application_status import ApplicationStatus
from src.model.node_model import NodeModel
from src.model.status import Status


class TransactionStatus(NodeModel):
    id: int = Field(alias='Id')
    status: Status = Field()
    application_status: ApplicationStatus = Field(alias='applicationStatus')
    height: int = Field(default=0)
    confirmations: int = Field(default=0)
