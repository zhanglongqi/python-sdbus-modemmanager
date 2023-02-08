from sdbus_block.modemmanager import MM, MMModems

if __name__ == "__main__":
	import sdbus

	sdbus.set_default_bus(sdbus.sd_bus_open_system())
	mm = MM()
	print(f'{mm.version=}')

	mms = MMModems()
	modem = mms.get_first()
	if modem:
		print(f'{modem.state_text=}, {modem.imei=}, {modem.manufacturer=}, {modem.model=}, {modem.hardware_revision=}, '
				f'{modem.own_numbers=}, {modem.power_state_text=}, {modem.signal_quality=}')

		if modem.sim_object_path is not None:
			modem.set_sim(modem.sim_object_path)
			if modem.sim:
				print(f'{modem.sim.imsi=}, {modem.sim.sim_identifier=}, {modem.sim.operator_name=}, '
						f'{modem.sim.operator_identifier=}')
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
