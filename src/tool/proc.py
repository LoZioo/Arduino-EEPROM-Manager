import sys

def print_help() -> None:
	print("Usage:\n  %s port task [task parameters] [file]\n" % sys.argv[0])

	print("port:\t\t\t\t Select COM port.")
	print("file:\t\t\t\t binary file to read from or write to.")
	print()

	print("Tasks:")
	print("  help, --help, -h\t\t Show help.")
	print("  test\t\t\t\t Connection test.")
	print("  read base-address offset\t Read \"offset\" bytes starting from the \"base-address\" address and put the read content into the binary file.")
	print("  write base-address\t\t Write the binary file starting from the \"base-address\" address.")
	print("  dump\t\t\t\t Dump EEPROM content in the binary file.")
	print("  clear\t\t\t\t Fill the entire EEPROM with zeros.")
	print("  size\t\t\t\t Get the EEPROM size in bytes.")
