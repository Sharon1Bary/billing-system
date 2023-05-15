from dataclasses import dataclass
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

import uuid


@dataclass
class Report(BaseModel):

    uuid: UUID
    transaction: list

    def __init__(self) -> None:
        super().__init__(transaction=[], uuid=uuid.uuid4())

    def download_report(self, fake_db) -> str:
        # TODO: replace fake_db with orm.
        # TODO: Query to the database to get the last 5 days report. (transaction_id, success/fail)

        return str([x for x in fake_db.transaction if datetime.timestamp(datetime.now()) - x.timestamp])
