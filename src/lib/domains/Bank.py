from dataclasses import dataclass
from pydantic import BaseModel
from uuid import UUID

import uuid


@dataclass
class Bank(BaseModel):

    uuid: UUID

    def __init__(self) -> None:
        super().__init__(uuid=uuid.uuid4())
