extern packet_t packet;

void send_ack(){
	packet.command = DEVICE_ACK;
	packet.mem_address = packet.data_len = 0;

	Serial.write((uint8_t*) &packet, sizeof(packet));
}
