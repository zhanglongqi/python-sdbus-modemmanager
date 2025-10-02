import sdbus
from sdbus_block.modemmanager import MMModems

if __name__ == "__main__":

    sdbus.set_default_bus(sdbus.sd_bus_open_system())
    modem = MMModems().get_first()

    if modem:
        loc = modem.location
        print('Supported Location Sources')
        print('-------------------------')
        for src in loc.enabled_list:
            print(f'\t{src.name}')
        print('Location Sources Enabled')
        print('-------------------------')
        for src in loc.enabled_list:
            print(f'\t{src.name}')
            
        print('Signals Location Enabled (true if location updates will be emitted via D-Bus signals)')
        print('-------------------------')
        print(f'\t{loc.signals_location}')
        
        print('GPS Refresh Rate')
        print('-------------------------')
        print(f'\t{loc.gps_refresh_rate}')

        print('Source Map (get_location() as a dictionary)')
        print('-------------------------')
        src_map = loc.source_map
        for k, v in src_map.items():
            print(f'\t{k.name}: {v}')
    else:
        print('no modem found')
