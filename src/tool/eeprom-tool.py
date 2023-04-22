import serial, struct, sys

from const import *
from packet import *
from proc import *

if __name__ == "__main__":
	# From bytes to int: int.from_bytes(val, "little", signed=False)
	# Unpack operator: *val

	argc = len(sys.argv)
	argv = sys.argv

	# Minimum args number.
	if argc >= 3:
		SERIAL_PORT = argv[2]
		ser = serial.Serial(SERIAL_PORT, SERIAL_SPEED)

		# Receve sync data.
		if int.from_bytes(ser.read(4), "little", signed=False) == SYNC_DATA:
			match argc:
				case 3:
					match argv[1]:
						case "size":
							ser.write(struct.pack(PACKET_T, EEPROM_SIZE, 0, 0))
							val = int.from_bytes(ser.read(2), "little", signed=False)

							print("EEPROM size: %s bytes." % val)

						case _:
							print_help()

				case _:
						print_help()

		ser.close()

	else:
		print_help()

	exit(0)

	print(val.hex())

	val = list(struct.unpack(PACKET_T, val))
	print(val)

	val[2] += 1

	val = struct.pack(PACKET_T, *val).hex()
	print(val)
