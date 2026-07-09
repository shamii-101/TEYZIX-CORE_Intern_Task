import logging

logging.basicConfig(
    filename="invoice_system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)


def log_info(message):
    logging.info(message)


def log_error(message):
    logging.error(message)