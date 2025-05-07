from modules.utils.logger import get_logger
_logger = get_logger("[main.py]")

from modules.uart.uart_connection import UartConnection

def main():
    _logger.info("Start running.")

    uart_conn = UartConnection()

    uart_conn.writes((
        "command;",
        "blaster fire;",
        "quit;"
    ))

    _logger.info("Stop running.")


if __name__ == "__main__":
    main()