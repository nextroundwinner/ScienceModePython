"""Provides classes for general Reset"""

from src.commands import Commands, ResultAndError
from src.packet import Packet, PacketAck

class PacketGeneralReset(Packet):
    """Packet for general Reset"""


    def __init__(self):
        super().__init__()
        self._command = Commands.Reset


class PacketGeneralResetAck(PacketAck):
    """Packet for general Reset acknowledge"""


    def __init__(self, data: bytes):
        super().__init__(data)
        self._command = Commands.ResetAck
        self._result_error = ResultAndError.NO_ERROR

        if data:
            self._result_error = ResultAndError(data[0])


    def get_result_error(self) -> ResultAndError:
        """Getter for ResultError"""
        return self._result_error


    result_error = property(get_result_error)
