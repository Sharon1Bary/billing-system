from src.lib.domains.Account import Account
from dataclasses import dataclass
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

import uuid


@dataclass
class Transaction(BaseModel):
    uuid: UUID
    timestamp: float
    amount: float
    direction: str
    src_account_uuid: str
    dst_account_uuid: str
    success: bool

    def __init__(self, amount: float, direction: str, src_account_uuid: str, dst_account_uuid: str) -> None:
        super().__init__(timestamp=get_current_timestamp(), amount=amount, uuid=uuid.uuid4(),
                         direction=direction, src_account_uuid=src_account_uuid, dst_account_uuid=dst_account_uuid,
                         success=self.perform_transaction())

    def perform_transaction(self, fake_db) -> bool:
        # TODO: replace fake_db with orm.
        # TODO: Query to database to check if the src_account have the balance.
        # TODO: Then, update the database with the transaction changes.

        if float(fake_db.account[self.src_account_uuid]['balance']) > self.amount:
            fake_db.account[self.dst_account_uuid]['balance'] = \
                float(fake_db.account[self.src_account_uuid]['balance']) + self.amount
            fake_db.account[self.src_account_uuid]['balance'] = \
                float(fake_db.account[self.src_account_uuid]['balance']) - self.amount
            fake_db.transaction[self.uuid] = self
            return True
        return False


def get_current_timestamp() -> float:
    return datetime.timestamp(datetime.now())
