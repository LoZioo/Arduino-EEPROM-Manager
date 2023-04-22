import sys

from packet import *

def print_help() -> None:
	print("Usage:\n  %s port task [task parameters]\n" % sys.argv[0])

	print("port:\t\t\t\t Select COM port.")
	print()

	print("Tasks:")
	print("  help, --help, -h\t\t\t Show help.")
	print("  test\t\t\t\t\t Connection test.")
	print("  read base-address offset file.bin\t Read \"offset\" bytes starting from the \"base-address\" address of the EEPROM and put the read content into the binary file \"file.bin\".")
	print("  write base-address file.bin\t\t Write the binary file \"file.bin\" starting from the \"base-address\" address of the EEPROM.")
	print("  dump file.bin\t\t\t\t Dump EEPROM content in the binary file \"file.bin\".")
	print("  clear\t\t\t\t\t Fill the entire EEPROM with zeros.")
	print("  size\t\t\t\t\t Get the EEPROM size in bytes.")

def check_ack(packet: bytes, message: str = "ACK received.") -> bool:
	ack = struct.unpack(PACKET_T, packet)

	if ack == (DEVICE_ACK, 0, 0):
		print(message)
		return True
	
	print("Error: wrong ACK packet.")
	return False
