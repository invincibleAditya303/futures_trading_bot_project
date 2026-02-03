import logging

LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

def setup_logger():
    logging.basicConfig(
        filename="trading.log",
        level=logging.INFO,
        format=LOG_FORMAT
    )

    return logging.getLogger("TradingBot")