from src.apps.Processor import perform_transaction
from src.config.BillingConfig import BillingConfig

from fastapi import APIRouter, FastAPI, Query


app = FastAPI(title="Billing System")

router_perform_advance = APIRouter()

billing_config = BillingConfig()


@app.get('/', status_code=200, tags=['Health Check'])
def health_check():
    return "Billing System is up and running."


@router_perform_advance.get(billing_config.download_report_conf.prefix, status_code=200)
async def perform_advance(dst_account: str = Query(None, alias='dst_bank_account'),
                          amount: int = Query(None, alias='amount')):
    """
    Perform a new advance transaction - next 12 weeks will be debit if 12 amount once a week.
        :param dst_account: str
        :param amount: int
        :return: UUID
    """
    try:
        # TODO: use the Processor API perform_transaction() and run it one a week with 12 debits amount
        # TODO: get the src_account when login to the Billing System.

        await perform_transaction(src_account="", dst_account=dst_account, amount=amount, direction='debit')
    except Exception as el:
        logger.exception(f'Error occurred: {el}')


app.include_router(router_perform_advance, tags=["perform_advance"])


if __name__ == "__main__":
    """
    The main is creating logger,
    To login the swagger please go to - http://127.0.0.1:8002/docs#/
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

    try:
        uvicorn.run(app, port=8002, log_level="debug")
    except Exception as e:
        logger.exception(e)
