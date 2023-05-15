from dataclasses import dataclass
from pydantic import BaseModel, validator
from uuid import UUID

import uuid


@dataclass
class Account(BaseModel):

    uuid: UUID
    balance: float

    def __init__(self, balance: float) -> None:
        super().__init__(balance=balance, transaction=[], uuid=uuid.uuid4())

    @validator('balance', pre=True, check_fields=False)
    def balance(cls, value):
        if not isinstance(value, float):
            raise ValueError('Balance must be a float')
        return value
