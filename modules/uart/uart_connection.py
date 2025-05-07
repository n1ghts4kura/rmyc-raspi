import typing
import serial

from ..utils.logger import get_logger

_logger = get_logger("[class UartConnection]")

class UartConnection:
    """
    实现基本的串口连接功能
    """

    def __init__(
        self,
        port:     str   = "/dev/ttyS0",
        baudrate: int   = 115200,
        bytesize: int   = 8,
        parity:   str   = serial.PARITY_NONE,
        stopbits: int   = serial.STOPBITS_ONE,
        timeout:  typing.Union[float, None] = None
    ):
        """
        Args:
            port (str): 串口端口
            baudrate (int): 串口波特率
            bytesize (int): 串口数据长度
            parity (str): 串口数据校验位
            stopbits (int): 串口数据停止位
            timeout (float | None): 串口超时
        """
        self.serial = serial.Serial(
            port,
            baudrate,
            bytesize,
            parity,
            stopbits,
            timeout,
        )
        if not self.serial.is_open:
            self.serial.open()

        _logger.info("Initialize serial successfully.")

    def write(self, content: str) -> typing.Union[int, None]:
        """
        往串口中写入数据
        Args:
            content (str): 数据内容
        Returns:
            int: 串口反应
            None: 不知道。
        """
        _logger.info(f"Writing data: {content}")
        return self.serial.write(content.encode("utf-8"))
    
    def writes(self, contents: tuple[str]) -> list[typing.Union[int, None]]:
        """
        往串口中连续写入数据
        Args:
            contents ( tuple [str] ): 一些数据内容
        Returns:
            int: 串口反应
            None: 不知道。
        """
        result = []
        for content in contents:
            result.append(self.write(content))
        return result

    def read(self) -> typing.Union[str, None]:
        """
        读取串口数据 以\\n结尾
        Returns:
            str: 数据
            None: 读取失败
        """
        try:
            content = self.serial.readline().decode("utf-8")
            _logger.info(f"Receiving data: {content}")
            return content
        except Exception as e:
            _logger.error("Failed to get data from serial.")
            _logger.error(str(e))
            return None