import struct

SERIAL_SPEED = 115200

PACKET_T = "<BHH"	# https://docs.python.org/3/library/struct.html#byte-order-size-and-alignment
PACKET_SIZE = struct.calcsize(PACKET_T)	# bytes
