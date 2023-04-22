import sys

from serial import Serial
from const import *

def print_help() -> None:
	print("Usage:\n  %s port task [task parameters]\n" % sys.argv[0])

	print("port:\t\t\t\t\t Select serial port.")
	print()

	print("Tasks:")
	print("  help, --help, -h\t\t\t Print this help.")
	print("  test\t\t\t\t\t Connection test.")
	print("  dump [file.bin]\t\t\t Dump EEPROM content into the binary file \"file.bin\".")
	print("  flash file.bin\t\t\t Flash content of the binary file \"file.bin\" into the EEPROM.")
	print("  clear\t\t\t\t\t Fill the entire EEPROM with zeros.")
	print("  size\t\t\t\t\t Get the EEPROM size in bytes.")

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
	print()

def send_byte(ser: Serial, val: int) -> None:
	ser.write(val.to_bytes(1, "little", signed=False))

def receive_byte(ser: Serial) -> int:
	return int.from_bytes(ser.read(), "little", signed=False)

def wait_ack(ser: Serial, message: str = "ACK received.") -> bool:
	if receive_byte(ser) == DEVICE_ACK:
		print(message)
		return True

	print("Error receiving ACK.")
	return False

def dump_eeprom(ser: Serial, size: int) -> bytes:
	print("Dumping %d bytes from the EEPROM... " % size, end="")
	sys.stdout.flush()

	send_byte(ser, EEPROM_DUMP)
	dump = ser.read(size)

	print("Ok")
	return dump

def flash_eeprom(ser: Serial, content: bytes) -> None:
	print("Flashing %d bytes into the EEPROM... " % len(content), end="")
	sys.stdout.flush()

	send_byte(ser, EEPROM_FLASH)
	ser.write(content)

	wait_ack(ser, "Ok")

def clear_eeprom(ser: Serial) -> None:
	print("Clearing EEPROM... ", end="")
	sys.stdout.flush()

	send_byte(ser, EEPROM_CLEAR)
	wait_ack(ser, "Ok")

def read_file(filename: str) -> bytes:
	try:
		with open(filename, "rb") as file:
			return file.read()

	except IOError as e:
		print("Error in opening \"%s\": %s." % (filename, e))
		exit(1)

def write_file(content: bytes, filename: str) -> None:
	with open(filename, "wb") as file:
		file.write(content)

	print("Dump saved in \"%s\"." % filename)
