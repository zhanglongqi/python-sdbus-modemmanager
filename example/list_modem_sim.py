from sdbus_block.modemmanager import MM, MMModems

if __name__ == "__main__":
	import sdbus

	sdbus.set_default_bus(sdbus.sd_bus_open_system())
	mm = MM()
	print(f'{mm.version=}')

	mms = MMModems()
	modem = mms.get_first()
	if modem:
		print('-------------------------')
		print(f'{modem.state_text=}\n'
				f'{modem.imei=}\n'
				f'{modem.manufacturer=}\n'
				f'{modem.model=}\n'
				f'{modem.hardware_revision=}\n'
				f'{modem.own_numbers=}\n'
				f'{modem.power_state_text=}\n'
				f'{modem.signal_quality=}\n'
				f'{modem.access_technologies_text=}\n'
				f'{modem.current_capabilities=}\n'
				f'{modem.current_capabilities_text=}\n')

		if modem.sim_object_path is not None and modem.sim_object_path != '/':
			modem.set_sim(modem.sim_object_path)
			if modem.sim:
				print('-------------------------')
				print(f'{modem.sim.imsi=}\n'
						f'{modem.sim.sim_identifier=}\n'
						f'{modem.sim.operator_name=}\n'
						f'{modem.sim.operator_identifier=}\n')
			else:
				print(f'failed to get sim object {modem.sim_object_path=}')
		else:
			print('no sim card found')
		if len(modem.bearer_object_paths) > 0:
			modem.set_bearers(modem.bearer_object_paths)
			for b in modem.bearers:
				print(f'{b.connected=}')
		else:
			print('no bearer found')
	else:
		print('no modem found')
