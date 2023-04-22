import sys

from serial import Serial
from packet import *

def print_help() -> None:
	print("Usage:\n  %s port task [task parameters]\n" % sys.argv[0])

	print("port:\t\t\t\t\t Select COM port.")
	print()

	print("Tasks:")
	print("  help, --help, -h\t\t\t Show help.")
	print("  test\t\t\t\t\t Connection test.")
	print("  read base-address offset file.bin\t Read \"offset\" bytes starting from the \"base-address\" address of the EEPROM and put the read content into the binary file \"file.bin\".")
	print("  write base-address file.bin\t\t Write the binary file \"file.bin\" starting from the \"base-address\" address of the EEPROM.")
	print("  dump [file.bin]\t\t\t Dump EEPROM content in the binary file \"file.bin\".")
	print("  clear\t\t\t\t\t Fill the entire EEPROM with zeros.")
	print("  size\t\t\t\t\t Get the EEPROM size in bytes.")

def check_ack(ser: Serial, message: str = "ACK received.") -> bool:
	ack = struct.unpack(PACKET_T, ser.read(PACKET_SIZE))

	if ack == (DEVICE_ACK, 0, 0):
		print(message)
		return True

	print("Error: wrong ACK packet.")
	return False

def get_dump(ser: Serial, size: int) -> bytes:
	print("Dumping %d bytes from the EEPROM... " % size, end="")
	ser.write(struct.pack(PACKET_T, EEPROM_DUMP, 0, 0))
	dump = ser.read(size)
	print("Ok")

	return dump

def print_hex_dump(dump: bytes) -> None:
	print("Hex dump:\n")
	print("   Address", end="")
	for i in range(0, 16):
		print("  %02X" % i, end="")
	print("\n")

	for i in range(0, int(len(dump) / 16)):
		print("  %08X" % (16 * i), end="")

		for j in range(0, 16):
			print("  %02X" % dump[16 * i + j], end="")
		print()

def save_dump(filename: str, dump: bytes) -> None:
	with open(filename, "wb") as file:
		file.write(dump)
	
	print("\nDump saved in \"%s\"." % filename)
