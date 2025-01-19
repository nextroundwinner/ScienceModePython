
from src.utils.bit_vector import BitVector


class ByteBuilder():

    # each entry represent a bit
    data: BitVector


    def __init__(self, data = 0):
        self.data = BitVector(data)

    def getFromPosition(self, bit_position: int, bit_length: int) -> int:
        result = 0
        for x in range(bit_length):
            result |= (self.data[bit_position + x] << x) & 0x1


    def append(self, value: int | list[int]):
        if isinstance(value, int):
            self.appendIntern(value)
        else:
            for x in value:
                self.appendIntern(x)


    def extendBytes(self, value: bytes):
            self.data.extend(value)


    def extendByteBuilder(self, value: 'ByteBuilder'):
            self.data.extend(value.getBytes())


    def setToPosition(self, value: int, bit_position: int, bit_length: int):
        for x in range(bit_length):
            self.data[bit_position + x] = (value >> x) & 0x1


    def swap(self, start: int, count: int):
        tmp = self.getBytes()
        for x in range(count):
            self.setToPosition(tmp[start + x], (start + count - x - 1) * 8, 8)


    def getBytes(self) -> bytes:
        return self.data.getBytes()


    def clear(self):
        self.data = BitVector(0)


    def print(self):
        b = self.getBytes()
        print(len(b))
        print(b.hex(' ').upper())


    def appendIntern(self, value: int):
        start = len(self.data)

        for x in range(8):
            self.data[start + x] = (value >> x) & 0x1