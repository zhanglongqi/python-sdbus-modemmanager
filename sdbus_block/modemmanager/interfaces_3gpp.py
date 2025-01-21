from typing import Any, Dict, List, Optional, Tuple

from sdbus import DbusInterfaceCommon, DbusObjectManagerInterface, dbus_method, dbus_property


class MMModem3gppInterface(DbusInterfaceCommon, interface_name="org.freedesktop.ModemManager1.Modem.Modem3gpp"):
	"""Set initial EPS Bearer setting
	List of properties to use when requesting the LTE attach procedure.

	Updates the default settings to be used in the initial default EPS bearer when registering to the LTE network.

	The allowed properties in this method are all the 3GPP-specific ones specified in the bearer properties.
	i.e.: "apn", "ip-type", "allowed-auth", "user" and "password".
	
	param properties: Dictionary of properties needed initiate a connexion ex: {"apn": ("s", "yourAPN.isp"), "ip-type": ("s", "ipv4v6")}
	"""
	@dbus_method(input_signature="a{sv}")
	def set_initial_eps_bearer_settings(
		self,
		settings: Dict[str, Tuple[str, Any]],
	) -> None:
		raise NotImplementedError

