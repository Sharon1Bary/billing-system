from src.lib.domains.Bank import Bank

from sqlalchemy.orm import Session
from sqlalchemy import create_engine, MetaData, Table, Column, String, Float, Boolean
from datetime import datetime

import sqlalchemy as db
import psycopg2
import uuid

engine = create_engine("postgresql://postgres:12345@localhost/postgres")
connection = engine.connect()
metadata = MetaData()

bank = Table('bank', metadata,
             Column('id', String(255), primary_key=True))

customer = Table('customer', metadata,
                 Column('id', String(255), primary_key=True),
                 Column('bank_id', String(255)),
                 Column('account_id', String(255)))

account = Table('account', metadata,
                Column('id', String(255), primary_key=True),
                Column('balance', Float))

transaction = Table('transaction', metadata,
                    Column('id', String(255)),
                    Column('time', String(255)),
                    Column('src_account_id', String(255)),
                    Column('dst_account_id', String(255)),
                    Column('direction', String(255)),
                    Column('amount', Float),
                    Column('success', Boolean))

metadata.create_all(engine)

# Inserting record one by one

with Session(create_engine("postgresql://postgres:12345@localhost/postgres")) as session:
    session.add(Bank)
    session.commit()

# connection.execute(db.insert(customer).values(id=customer_id_1, bank_id=bank_id, account_id=account_id_1))
# connection.execute(db.insert(customer).values(id=customer_id_2, bank_id=bank_id, account_id=account_id_2))
# connection.execute(db.insert(account).values(id=account_id_1, balance=60000.00))
# connection.execute(db.insert(account).values(id=account_id_2, balance=50000.00))
# connection.execute(db.insert(transaction).values(id=transaction_id, time=str(datetime.timestamp(datetime.now())),
#                                                  src_account_id=account_id_1,
#                                                  dst_account_id=account_id_2,
#                                                  direction='credit',
#                                                  amount=10.0,
#                                                  success=True))
