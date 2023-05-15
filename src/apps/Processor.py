from src.config.ProcessorConfig import ProcessorConfig
from src.lib.domains.Transaction import Transaction
from src.lib.domains.Report import Report
from src.lib.adapters.fake_database.FakeDatabase import FakeDatabase

from fastapi import APIRouter, FastAPI, Query, BackgroundTasks
from uuid import UUID

app = FastAPI(title="Processor")

router_perform_transaction = APIRouter()
router_download_report = APIRouter()

processor_config = ProcessorConfig()


@app.get('/', status_code=200, tags=['Health Check'])
def health_check():
    return "Processor is up and running."


@router_perform_transaction.get(processor_config.perform_transaction_conf.prefix, status_code=200)
async def perform_transaction(background_tasks: BackgroundTasks,
                              src_account: str = Query(None, alias='src_bank_account'),
                              dst_account: str = Query(None, alias='dst_bank_account'),
                              amount: int = Query(None, alias='amount'),
                              direction: str = Query(None, alias='amount')) -> UUID:
    """
    Perform a new transaction from src_bank_account to dst_bank_account.
        :param background_tasks:
        :param src_account: str
        :param dst_account: str
        :param amount: int
        :param direction: str
        :return: UUID
    """
    try:
        transaction = Transaction(amount=amount,
                                  direction=direction,
                                  src_account_uuid=src_account,
                                  dst_account_uuid=dst_account)
        background_tasks.add_task(transaction.perform_transaction(fake_db))
        return transaction.uuid
    except Exception as el:
        logger.exception(f'Error occurred: {el}')


@router_download_report.get(processor_config.download_report_conf.prefix, status_code=200)
async def download_report() -> list:
    """
    Returns a report of the transaction results.
        :return: repo
    """
    try:
        report = Report()
        report.download_report(fake_db)
        return []
    except Exception as el:
        logger.exception(f'Error occurred: {el}')


app.include_router(router_perform_transaction, tags=["perform_transaction"])
app.include_router(router_download_report, tags=["download_report"])

if __name__ == "__main__":
    """
    The main is creating logger, core and activation the fast-api using uvicorn.
    To login the swagger please go to - http://127.0.0.1:8001/docs#/
    """

    import uvicorn
    import logging
    import sys

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)

    fake_db = FakeDatabase()
    try:
        uvicorn.run(app, port=8001, log_level="debug")
    except Exception as e:
        logger.exception(e)
