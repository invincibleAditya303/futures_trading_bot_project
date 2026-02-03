def validate_order_params(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float | None
) -> None:

    if not symbol.isupper():
        raise ValueError("Symbol must be uppercase")
    
    if not symbol.endswith("USDT"):
        raise ValueError("Only USDT-M futures supported")
    
    if side not in {"BUY", "SELL"}:
        raise ValueError("Side must be BUY or SELL")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")

    if order_type == "LIMIT" and price is None:
        raise ValueError("Price is required for LIMIT orders")