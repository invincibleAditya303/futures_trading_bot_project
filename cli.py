import argparse
from client import get_authenticated_client
from validators import validate_order_params
from orders import (place_futures_order, get_quantity_step_size, normalize_quantity)

def parse_args():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    return parser.parse_args()

def main():
    args = parse_args()

    try:
        validate_order_params(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        client = get_authenticated_client()

        step_size = get_quantity_step_size(client, args.symbol)
        normalize_qty = normalize_quantity(args.quantity, step_size)

        if normalize_qty != args.quantity:
            print(
                f"Qunatity adjusted from {args.quantity} -> {normalize_qty}"
                f" to match exchange precision rules"
            )

        order_params = {
            "symbol": args.symbol,
            "side": args.side,
            "type": args.type,
            "quantity": args.quantity
        }

        if args.type == "LIMIT":
            order_params.update({
                "price": args.price,
                "timeInForce": "GTC"
            })

        response = place_futures_order(client, order_params)

        if response:
            print("Order placed successfully")
            print(f"Order ID: {response['orderId']}")
            print(f"Status: {response['status']}")
        else:
            print("Order failed - check logs")

    except ValueError as e:
        print(f"Validation Error: {e}")

    except Exception as e:
        print(f"Fatal Error: {e}")


if __name__ == "__main__":
    main()