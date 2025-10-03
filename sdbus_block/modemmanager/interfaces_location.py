from typing import Any, List, Tuple

from sdbus import DbusInterfaceCommon, dbus_method, dbus_property


class MMModemLocationInterface(DbusInterfaceCommon, interface_name='org.freedesktop.ModemManager1.Modem.Location'):
	"""
    The Location interface allows devices to provide location information to client applications. 
    Not all devices can provide this information, or even if they do, they may not be able to provide it while a data session is active.

    This interface will only be available once the modem is ready to be registered in the cellular network.
    3GPP devices will require a valid unlocked SIM card before any of the features in the interface can be used (including GNSS module management).
    """

	@dbus_method(input_signature='ub')
	def setup(self, sources: int, signal_location: bool) -> None:
		"""
        Configure the location sources to use when gathering location information.

        When location signaling is enabled by the user, any client application (including malicious ones!) 
        would be able to use the "Location" property to receive location updates.

        sources         -   Bitmask of MMModemLocationSource flags, specifying which sources should get enabled or disabled. 
                            MM_MODEM_LOCATION_SOURCE_NONE will disable all location gathering.
                  
        signal_location -   Flag to control whether the device emits signals with the new location information. 
                            This argument is ignored when disabling location information gathering.
        """
		raise NotImplementedError

	@dbus_method()
	def get_location(self) -> dict[int, Tuple[str, Any]]:
		"""Return current location information, if any. If the modem supports multiple location types it may return more than one."""
		raise NotImplementedError

	@dbus_method(input_signature='s')
	def set_supl_server(self, supl: str) -> None:
		"""
        Configure the SUPL server for A-GPS.
        supl - SUPL server configuration, given either as IP:PORT or as FQDN:PORT.
        """
		raise NotImplementedError

	@dbus_method(input_signature='ay')
	def inject_assistance_data(self, data: bytes) -> None:
		"""
        Inject assistance data to the GNSS module, which will allow it to have a more accurate positioning information.
        """
		raise NotImplementedError

	@dbus_method(input_signature='u')
	def set_gps_refresh_rate(self, rate: int) -> None:
		"""
        Set the refresh rate of the GPS information in the API. If not explicitly set, a default of 30s will be used.
        The refresh rate can be set to 0 to disable it, so that every update reported by the modem is published in the interface.
        
        rate - Rate, in seconds
        """
		raise NotImplementedError

	@dbus_property(property_signature='u')
	def capabilities(self) -> int:
		"""
        Bitmask of MMModemLocationSource values, specifiying the supported location sources.
        """
		raise NotImplementedError

	@dbus_property(property_signature='u')
	def supported_assistance_data(self) -> int:
		"""
        Bitmask of MMModemLocationAssistanceDataType values, specifying the supported types of assistance data.
        """
		raise NotImplementedError

	@dbus_property(property_signature='u')
	def enabled(self) -> int:
		"""
        Bitmask specifying which of the supported MMModemLocationSource location sources are enabled.
        """
		raise NotImplementedError

	@dbus_property(property_signature='b')
	def signals_location(self) -> bool:
		"""
        True if location updates will be emitted via D-Bus signals, False if location updates will not be emitted.
        """
		raise NotImplementedError

	@dbus_property(property_signature='a{sv}')
	def location(self) -> List[dict]:
		"""
        Dictionary of available location information when location information gathering is enabled. 
        If the modem supports multiple location types it may return more than one here.

        For security reasons, the location information updates via this property are disabled by default. 
        Users can use this property to monitor location updates only if the location signals are enabled with Setup(),
        but considering that enabling the location signals would allow all users to receive property updates as well,
        not just the process that enabled them. For a finer grained access control, the user can use the GetLocation()
        method instead, which may require the client to authenticate itself on every call.
        """
		raise NotImplementedError

	@dbus_property(property_signature='s')
	def supl_server(self) -> str:
		"""
        SUPL server configuration for A-GPS, given either as IP:PORT or FQDN:PORT.
        """
		raise NotImplementedError

	@dbus_property(property_signature='as')
	def assistance_data_servers(self) -> List[str]:
		"""
        URLs from where the user can download assistance data files to inject with InjectAssistanceData().
        """
		raise NotImplementedError

	@dbus_property(property_signature='u')
	def gps_refresh_rate(self) -> int:
		"""
        Rate of refresh of the GPS information in the interface.
        """
		raise NotImplementedError
