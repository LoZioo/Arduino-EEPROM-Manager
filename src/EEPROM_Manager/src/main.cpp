#include <Arduino.h>
#include <EEPROM.h>

#include <const.h>

uint8_t *buf;
uint16_t eeprom_size;

void send_byte(command_t val){
	Serial.write(val);
}

void setup(){
	Serial.begin(SERIAL_SPEED);
	EEPROM.begin();

	// Get EEPROM size.
	eeprom_size = EEPROM.length();
	buf = new uint8_t[eeprom_size];

	// Send sync data.
	send_byte(SYNC_DATA);
}

void loop(){
	if(Serial.available()){
		switch(Serial.read()){
			case DEVICE_PING:
				send_byte(DEVICE_ACK);
				break;

			case DEVICE_ACK:
				break;

			case EEPROM_DUMP:
				for(uint16_t i=0; i<eeprom_size; i++)
					Serial.write(EEPROM.read(i));
				break;

			case EEPROM_FLASH:
				Serial.readBytes(buf, eeprom_size);

				for(uint16_t i=0; i<eeprom_size; i++)
					EEPROM.update(i, buf[i]);

				send_byte(DEVICE_ACK);
				break;

			case EEPROM_CLEAR:
				for(uint16_t i=0; i<eeprom_size; i++)
					EEPROM.update(i, 0);

				send_byte(DEVICE_ACK);
				break;

			case EEPROM_SIZE:
				Serial.write((uint8_t*) &eeprom_size, sizeof(eeprom_size));
				break;
		}
	}
}
