from dataclasses import dataclass


@dataclass
class PerformTransactionConfig:
    prefix: str = '/api/v1/perform_transaction'


@dataclass
class DownloadReportConfig:
    prefix: str = '/api/v1/download_report'


class ProcessorConfig:
    download_report_conf: PerformTransactionConfig = PerformTransactionConfig()
    perform_transaction_conf: DownloadReportConfig = DownloadReportConfig()

