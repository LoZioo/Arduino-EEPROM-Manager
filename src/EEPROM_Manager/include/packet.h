#include <Arduino.h>

const uint32_t SYNC_DATA = 0xAABBCCDD;

typedef enum : uint8_t {
	DEVICE_PING,
	DEVICE_ACK,

	EEPROM_READ,
	EEPROM_WRITE,
	EEPROM_DUMP,
	EEPROM_CLEAR,

	EEPROM_SIZE,
} packet_command_t;

struct __attribute((__packed__)) packet_t {
	packet_command_t command;

	uint16_t	mem_address;
	uint16_t	data_len;
};
