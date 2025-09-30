from typing import List

from sdbus import DbusInterfaceCommon, dbus_method, dbus_property


class MMModemLocationInterface(DbusInterfaceCommon, interface_name='org.freedesktop.ModemManager1.Modem.Location'):
    """
    The Location interface allows devices to provide location information to client applications. 
    Not all devices can provide this information, or even if they do, they may not be able to provide it while a data session is active.

    This interface will only be available once the modem is ready to be registered in the cellular network.
    3GPP devices will require a valid unlocked SIM card before any of the features in the interface can be used (including GNSS module management).
    """

    @dbus_method()
    def get_location(self) -> dict:
        """Return current location information, if any. If the modem supports multiple location types it may return more than one."""
        raise NotImplementedError

    @dbus_property(property_signature='a{sv}')
    def location(self) -> List[dict]:
        """
        Dictionary of available location information when location information gathering is enabled. 
        If the modem supports multiple location types it may return more than one here.
        """
        raise NotImplementedError

    @dbus_property(property_signature='u')
    def enabled(self) -> dict:
        """
        dict specifying which of the supported MMModemLocationSource location sources are enabled.
        """
        raise NotImplementedError

    @dbus_property(property_signature='b')
    def signals_location(self) -> bool:
        """
        True if location updates will be emitted via D-Bus signals, False if location updates will not be emitted.
        """
        raise NotImplementedError
