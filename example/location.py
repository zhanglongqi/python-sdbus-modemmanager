import sdbus
from sdbus_block.modemmanager import MMModems

if __name__ == "__main__":

    sdbus.set_default_bus(sdbus.sd_bus_open_system())
    modem = MMModems().get_first()

    if modem:
        loc = modem.location
        print('Supported Location Sources')
        print('--------------------------')
        capable_sources = ", ".join(i.name for i in loc.capabilities_list)
        print(f'\t{capable_sources}')
        
        print('')
        print('Location Sources Enabled')
        print('------------------------')
        enabled_sources = ", ".join(i.name for i in loc.enabled_list)
        print(f'\t{enabled_sources}')
            
        print('')
        print('Signals Location Enabled')
        print('------------------------')
        print('(true if location updates will be emitted via D-Bus signals)')
        print(f'\t{loc.signals_location}')
        
        print('GPS Refresh Rate')
        print('----------------')
        print(f'\t{loc.gps_refresh_rate} seconds')

        print('Source Map')
        print('----------')
        src_map = loc.source_map
        for k, v in src_map.items():
            print(f'\t{k.name}: {str(v)}')
            
    else:
        print('no modem found')
