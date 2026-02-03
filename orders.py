import math
from binance.exceptions import BinanceAPIException, BinanceRequestException
from logging_config import setup_logger

logger = setup_logger()

def get_quantity_step_size(client, symbol: str) -> float:
    exchnage_info = client.futures_exchange_info()

    for s in exchnage_info["symbols"]:
        if s["symbol"] == symbol:
            for f in s["filters"]:
                if f["filterType"] == "LOT_SIZE":
                    return float(f["stepSize"])
    
    raise RuntimeError("Step size not found for symbol")

def normalize_quantity(quantity: float, step_size: float) -> float:
    precision = abs(int(round(-math.log10(step_size), 0)))
    return round(quantity // step_size * step_size, precision)

def place_futures_order(client, params: dict) -> dict | None:
    logger.info(f"SENT: {params}")

    try:
        response = client.futures_create_order(**params)
        logger.info(f"RECEIVED: {response}")
        return response
    
    except BinanceAPIException as e:
        logger.error(f"APIERROR: {e.message}")

    except BinanceRequestException as e:
        logger.error(f"NETWORKERROR: {str(e)}")

    except Exception as e:
        logger.error(f"UNKNOWNERROR: {str(e)}")

    return None