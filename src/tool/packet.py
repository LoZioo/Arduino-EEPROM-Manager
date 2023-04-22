import struct

# Packet struct info.
PACKET_T = "<BHH"	# https://docs.python.org/3/library/struct.html#byte-order-size-and-alignment
PACKET_SIZE = struct.calcsize(PACKET_T)	# bytes

SYNC_DATA = 0xAABBCCDD
SYNC_DATA_SIZE = 4

# Available commands
DEVICE_PING = 0
DEVICE_ACK = 1

EEPROM_READ = 2
EEPROM_WRITE = 3
EEPROM_DUMP = 4
EEPROM_CLEAR = 5

EEPROM_SIZE = 6
