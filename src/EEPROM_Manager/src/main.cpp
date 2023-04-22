#include <Arduino.h>
#include <EEPROM.h>

#include <const.h>

uint16_t eeprom_size;

void send_command(command_t com){
	Serial.write(com);
}

void setup(){
	Serial.begin(SERIAL_SPEED);
	EEPROM.begin();

	// Get EEPROM size.
	eeprom_size = EEPROM.length();

	// Send sync data.
	send_command(SYNC_DATA);
}

void loop(){
	if(Serial.available()){
		switch(Serial.read()){
			case DEVICE_PING:
				send_command(DEVICE_ACK);
				break;

			case DEVICE_ACK:
				break;

			case EEPROM_DUMP:
				for(uint16_t i=0; i<eeprom_size; i++)
					Serial.write(EEPROM.read(i));
				break;

			case EEPROM_FLASH:
				for(uint16_t i=0; i<eeprom_size; i++)
					EEPROM.update(i, Serial.read());

				send_command(DEVICE_ACK);
				break;

			case EEPROM_CLEAR:
				for(uint16_t i=0; i<eeprom_size; i++)
					EEPROM.update(i, 0);

				send_command(DEVICE_ACK);
				break;

			case EEPROM_SIZE:
				Serial.write((uint8_t*) &eeprom_size, sizeof(eeprom_size));
				break;
		}
	}
}
