from dataclasses import dataclass


@dataclass
class PerformAdvanceConfig:
    prefix: str = '/api/v1/perform_advance'


class BillingConfig:
    download_report_conf: PerformAdvanceConfig = PerformAdvanceConfig()

