"""Helper class for dyscom"""

import datetime
from ..utils.byte_builder import ByteBuilder

class DyscomHelper:
    """Provides some helper functions"""

    @staticmethod
    def datetime_to_bytes(dt: datetime.datetime) -> bytes:
        """Converts a datetime into dyscom compatible bytes"""
        bb = ByteBuilder()
        bb.append_byte(dt.hour)
        dst = dt.dst()
        bb.append_byte(0 if dst is None or dst == 0 else 1)
        bb.append_byte(dt.day)
        bb.append_byte(dt.minute)
        bb.append_byte(dt.month)
        bb.append_byte(dt.second)
        bb.append_byte((dt.weekday() + 1) % 7)
        bb.append_value(dt.timetuple().tm_yday - 1, 2, True)
        bb.append_value(dt.year - 1900, 2, True)

        return bb.get_bytes()


    @staticmethod
    def str_to_bytes(value: str, byte_count: int) -> bytes:
        """Converts value to bytes with byte_count bytes, last byte will always be 0"""
        temp = bytearray(value.zfill(byte_count), "ascii")
        for x in range(len(value), byte_count):
            temp[x] = 0
        temp[byte_count-1] = 0
        return bytes(temp)


    @staticmethod
    def bytes_to_str(value: bytes, byte_count: int) -> str:
        """Converts bytes to str with byte_count bytes"""
        end = value.find(bytes([0]))
        if end == -1:
            end = byte_count
        return value[0:end].decode()
