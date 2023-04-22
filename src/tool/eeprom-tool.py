import serial, sys

from const import *
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
		if receive_byte(ser) == SYNC_DATA:

			# Get EEPROM size.
			send_byte(ser, EEPROM_SIZE)
			eeprom_size = int.from_bytes(ser.read(2), "little", signed=False)

			match argc:
				case 3:
					task = argv[2]

					match task:
						case "test":
							send_byte(ser, DEVICE_PING)
							wait_ack(ser)

						case "dump":
							dump = dump_eeprom(ser, eeprom_size)
							print_hex_dump(dump)

						case "clear":
							clear_eeprom(ser)

						case "size":
							print("EEPROM size: %d bytes." % eeprom_size)

						case _:
							print_help()

				case 4:
					task = argv[2]
					filename = argv[3]

					match task:
						case "dump":
							dump = dump_eeprom(ser, eeprom_size)
							print_hex_dump(dump)
							write_file(dump, filename)

						case "flash":
							dump = read_file(filename)
							print_hex_dump(dump)
							flash_eeprom(ser, dump)

						case _:
							print_help()

				case _:
					print_help()

		ser.close()

	# argc < 3
	else:
		print_help()

	exit(0)
