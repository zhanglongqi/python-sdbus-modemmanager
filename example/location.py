import sdbus
from sdbus_block.modemmanager import MMModems

if __name__ == "__main__":

    sdbus.set_default_bus(sdbus.sd_bus_open_system())
    modem = MMModems().get_first()

    if modem:
        print('-------------------------')
        print(f'{modem.location.capabilities=}\n'
              f'{modem.location.capabilities_list=}\n\n'
              f'{modem.location.enabled=}\n'
              f'{modem.location.enabled_list=}\n\n'
              f'{modem.location.signals_location=}\n'
              f'{modem.location.gps_refresh_rate=}\n\n'
              f'{modem.location.location=}\n'
              f'{modem.location.get_location()=}\n'
              f'{modem.location.source_map=}\n')
    else:
        print('no modem found')
