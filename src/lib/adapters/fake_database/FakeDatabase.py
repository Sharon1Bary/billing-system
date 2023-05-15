from src.lib.domains.Transaction import Transaction
from src.lib.domains.Account import Account
from src.lib.domains.Bank import Bank
from src.lib.domains.Report import Report

from dataclasses import dataclass

import uuid


@dataclass
class FakeDatabase:
    def __init__(self):
        self.uuid: uuid = uuid.uuid4()
        self.transaction: {Transaction} = {}
        self.account: {Account} = {}
        self.bank: {Bank} = {}
        self.report: {Report} = {}

