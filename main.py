import logging

from connectors.binance import BinanceClient
from connectors.bitmex import BitmexClient

from interface.root_component import Root


# Create and configure the logger object

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)  # Overall minimum logging level

stream_handler = logging.StreamHandler()  # Configure the logging messages displayed in the Terminal
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)  # Minimum logging level for the StreamHandler

file_handler = logging.FileHandler('info.log')  # Configure the logging messages written to a file
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)  # Minimum logging level for the FileHandler

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':  # Execute the following code only when executing main.py (not when importing it)

    binance = BinanceClient("3573578c3be8079ed167b03d4b5c91e111b16afc4ce78cc2910c120a7bd0eec9",
                            "4539860a34646c2718f77b17ff21902a750aac69f83ba3c1f921731df9702d57",
                            testnet=True, futures=True)
    bitmex = BitmexClient("8iX2d0dqM3_x24h77YEtO6t6", "RaYJ4c6FrG0usfyQ7PTrEXUy5ikWTjgPPmBS3e5i8ZQeHaCX", testnet=True)

    root = Root(binance,bitmex)
    root.mainloop()
