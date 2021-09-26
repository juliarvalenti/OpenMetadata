# generated by datamodel-codegen:
#   filename:  schema/api/services/updateMessagingService.json
#   timestamp: 2021-09-25T21:02:32+00:00

from __future__ import annotations

from typing import Optional

from pydantic import AnyUrl, BaseModel, Field

from ...entity.services import messagingService
from ...type import schedule


class UpdateMessagingServiceEntityRequest(BaseModel):
    description: Optional[str] = Field(
        None, description='Description of Messaging service entity.'
    )
    brokers: Optional[messagingService.Brokers] = None
    schemaRegistry: Optional[AnyUrl] = Field(None, description='Schema registry URL.')
    ingestionSchedule: Optional[schedule.Schedule] = Field(
        None, description='Schedule for running metadata ingestion jobs'
    )
