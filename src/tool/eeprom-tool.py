import serial, struct, sys

from const import *
from packet import *
from proc import *

if __name__ == "__main__":
	# From bytes to int: int.from_bytes(val, "little", signed=False)
	# Unpack operator: *val

	match len(sys.argv):
		case 3:
			match sys.argv[1]:
				case "size":
					SERIAL_PORT = sys.argv[2]

					ser = serial.Serial(SERIAL_PORT, SERIAL_SPEED)
					ser.write(struct.pack(PACKET_T, EEPROM_SIZE, 0, 0))
					print("1")
					val = hex(int.from_bytes(ser.read(2), "little", signed=False))
					print("2")
					ser.close()

					print("EEPROM size: %s bytes." % val)

				case _:
					display_help()

		case _:
			display_help()

	exit(0)

	

	print(val.hex())

	val = list(struct.unpack(PACKET_T, val))
	print(val)

	val[2] += 1

	val = struct.pack(PACKET_T, *val).hex()
	print(val)
