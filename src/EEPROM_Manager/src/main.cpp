#include <Arduino.h>
#include <EEPROM.h>

#include <const.h>
#include <packet.h>
#include <proc.h>

packet_t packet;

uint8_t buf;
uint16_t eeprom_len;

void setup(){
	Serial.begin(SERIAL_SPEED);
	EEPROM.begin();

	eeprom_len = EEPROM.length();

	packet.command = EEPROM_DUMP;
	packet.mem_address = 10;
	packet.data_len = 25;

	while(true){
		Serial.write((uint8_t*) &packet, sizeof(packet));
		delay(1000);
	}
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
				for(uint16_t i=0; i<eeprom_len; i++)
					Serial.write(EEPROM.read(i));
				break;

			case EEPROM_CLEAR:
				for(uint16_t i=0; i<eeprom_len; i++)
					EEPROM.update(i, 0);

				send_ack();
				break;

			case EEPROM_LEN:
				Serial.write((uint8_t*) &eeprom_len, sizeof(eeprom_len));
				break;
		}
	}
}
