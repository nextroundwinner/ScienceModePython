from src.commands import Commands, ResultAndError
from src.packet import Packet, PacketAck

class PacketGeneralGetDeviceId(Packet):

    def __init__(self):
        self.command = Commands.GetDeviceId


class PacketGeneralGetDeviceIdAck(PacketAck):

    resultError: ResultAndError
    deviceId: str


    def __init__(self, data: bytes):
        self.command = Commands.GetDeviceIdAck

        if (data):
            self.resultError = ResultAndError(data[0])
            self.deviceId = data[1:11].decode()

        
