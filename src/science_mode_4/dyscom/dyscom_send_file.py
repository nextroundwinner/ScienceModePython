"""Provides packet classes for dyscom send file"""

import struct

from science_mode_4.protocol.commands import Commands
from science_mode_4.protocol.packet import Packet, PacketAck
from science_mode_4.utils.byte_builder import ByteBuilder


class PacketDyscomSendFile(PacketAck):
    """Packet for dyscom send file (this is technically not an acknowledge, but it is handled as such,
    because it is send automatically from device)"""


    _unpack_func = struct.Struct(">IH").unpack


    def __init__(self, data: bytes):
        super().__init__(data)
        self._command = Commands.DlSendFile
        self._block_number = 0
        self._block_size = 0
        self._data: bytes = bytes()

        if not data is None:
            self._block_number, self._block_size = PacketDyscomSendFile._unpack_func(">IH", data)
            self._data = data[6:self._block_size]


    @property
    def block_number(self) -> int:
        """Getter for block number"""
        return self._block_number


    @property
    def block_size(self) -> int:
        """Getter for block size"""
        return self._block_size


    @property
    def data(self) -> bytes:
        """Getter for data"""
        return self._data


class PacketDyscomSendFileAck(Packet):
    """Packet for dyscom send file acknowledge (this is technically not apacket, but it is handled as such,
    because it is send from PC to device)"""


    def __init__(self, block_number: int = 0):
        super().__init__()
        self._command = Commands.DlSendFileAck
        self._block_number = block_number


    def get_data(self) -> bytes:
        bb = ByteBuilder()
        bb.append_bytes(self._block_number)
        return bb.get_bytes()
