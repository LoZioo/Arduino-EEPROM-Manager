import serial, struct
from const import *

if __name__ == "__main__":
	# From bytes to int: int.from_bytes(val, "little", signed=False)
	# Unpack operator: *val

	ser = serial.Serial("/dev/ttyUSB0", SERIAL_SPEED)
	val = ser.read(PACKET_SIZE)
	ser.close()

	print(val.hex())

	val = list(struct.unpack(PACKET_T, val))
	print(val)

	val[2] += 1

	val = struct.pack(PACKET_T, *val).hex()
	print(val)
