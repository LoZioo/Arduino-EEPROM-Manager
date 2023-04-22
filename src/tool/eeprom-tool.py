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
		SERIAL_PORT = argv[1]

		try:
			ser = serial.Serial(SERIAL_PORT, SERIAL_SPEED)

		except:
			print("Error in opening the serial port \"%s\"." % SERIAL_PORT)
			exit(1)

		# Receve sync data.
		if int.from_bytes(ser.read(SYNC_DATA_SIZE), "little", signed=False) == SYNC_DATA:

			# Get EEPROM size.
			ser.write(struct.pack(PACKET_T, EEPROM_SIZE, 0, 0))
			eeprom_size = int.from_bytes(ser.read(2), "little", signed=False)

			match argc:
				case 3:
					TASK = argv[2]

					match TASK:
						case "test":
							ser.write(struct.pack(PACKET_T, DEVICE_PING, 0, 0))
							check_ack(ser)

						case "clear":
							ser.write(struct.pack(PACKET_T, EEPROM_CLEAR, 0, 0))
							check_ack(ser, "EEPROM cleared.")

						case "dump":
							dump = get_dump(ser, eeprom_size)
							print_hex_dump(dump)

						case "size":
							print("EEPROM size: %d bytes." % eeprom_size)

						case _:
							print_help()
					
				case 4:
					dump = get_dump(ser, eeprom_size)
					print_hex_dump(dump)
					save_dump(argv[3], dump)

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
