import time

import sdbus

from sdbus_block.modemmanager import MMCall, MMModems

# Enter your phone number here.
phone_number = '*************'


def main():
	sdbus.set_default_bus(sdbus.sd_bus_open_system())
	mms = MMModems()
	modem = mms.get_first()
	if modem is None:
		print('no modem found')
		return

	print(f'Exist calls: {modem.voice.list_calls()}')

	properties = {'number': ('s', phone_number)}
	call_path = modem.voice.create_call(properties)
	print(f'Call list after create: {modem.voice.list_calls()}')

	call = MMCall(call_path)
	print('--- Call properties ---')
	print(f'State value: {call.state}, name: {call.state_text}')
	print(f'State reason value: {call.state_reason}, name: {call.state_reason_text}')
	print(f'Direction value: {call.direction}, name: {call.direction_text}')
	print(f'Multiparty: {call.multiparty}')
	print(f'Number: {call.number}')
	print(f'Audio port: {call.audio_port}')
	print(f'Audio format: {call.audio_format}')

	print('--- Start call ---')
	call.start()
	while True:
		time.sleep(1)
		current_state = call.state_text
		print(f'Current call state: {current_state}')
		if current_state == 'MM_CALL_STATE_TERMINATED':
			break
	print('--- Stop call ---')

	modem.voice.delete_call(call_path)
	print(f'Call list after delete: {modem.voice.list_calls()}')


if __name__ == '__main__':
	main()
