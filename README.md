#Binance Futures Trading Bot (Testnet)

## Overview 
A command-line Binance USDT-M Futures trading bot built using Python.
The project demonstrates clean software architecture, input validation,
exchange constraint handling and full request/response logging.

## Features
- Binance Futures Testnet support
- Market and Limit orders
- Qunatity and price precision normalization
- Input validation before API calls
- File-based trade logging (`trading.log`)
- Secure API key mangement using environmental variables

## Tech Stack
- Python 3.8+
- python-binance
- argparse
- logging
- python-dotenv

##Setup Instructions
- Clone the repository
- Create a virtual environment (optional but recommended)
- Install dependencies:
    ```bash
    pip install -r requirements.txt
- Create a .env file
- Add Binance Futures Testnet API keys
