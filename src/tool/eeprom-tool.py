import serial
import numpy as np
# import numpy.typing as npt

SERIAL_SPEED = 115200

if __name__ == "__main__":
	# a = np.array([1, 2, 3], dtype=np.uint8)

	ser = serial.Serial("/dev/ttyUSB0", SERIAL_SPEED)

	c = 0
	while c<10:
		print(int.from_bytes(ser.read(), "little", signed=False))
		c += 1

	ser.close()
