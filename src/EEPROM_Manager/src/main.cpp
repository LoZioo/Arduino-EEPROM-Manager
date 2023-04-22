#include <Arduino.h>
#include <EEPROM.h>

#include <const.h>
#include <packet.h>
#include <proc.h>

packet_t packet;

uint8_t buf;
uint16_t eeprom_size;

void setup(){
	Serial.begin(SERIAL_SPEED);
	EEPROM.begin();

	// Get EEPROM size.
	eeprom_size = EEPROM.length();

	// Send sync data.
	Serial.write((uint8_t*) &SYNC_DATA, sizeof(SYNC_DATA));
}

void loop(){
	if(Serial.available()){
		Serial.readBytes((uint8_t*) &packet, sizeof(packet));

		switch(packet.command){
			case DEVICE_PING:
				send_ack();
				break;

			case DEVICE_ACK:
				break;

			case EEPROM_READ:
				for(uint16_t i=packet.mem_address; i<packet.mem_address+packet.data_len; i++){
					buf = EEPROM.read(i);
					Serial.write(buf);
				}
				break;

			case EEPROM_WRITE:
				for(uint16_t i=packet.mem_address; i<packet.mem_address+packet.data_len; i++)
					EEPROM.update(i, Serial.read());

				send_ack();
				break;

			case EEPROM_DUMP:
				for(uint16_t i=0; i<eeprom_size; i++)
					Serial.write(EEPROM.read(i));
				break;

			case EEPROM_CLEAR:
				for(uint16_t i=0; i<eeprom_size; i++)
					EEPROM.update(i, 0);

				send_ack();
				break;

			case EEPROM_SIZE:
				Serial.write((uint8_t*) &eeprom_size, sizeof(eeprom_size));
				break;
		}
	}
}
