from typing import Any, Dict, List, Tuple

from sdbus import DbusInterfaceCommon, dbus_method, dbus_property


class MMBearerInterface(DbusInterfaceCommon, interface_name='org.freedesktop.ModemManager1.Bearer'):
	"""This interface provides access to specific actions that may be performed on available bearers."""

	@dbus_method()
	def connect(self) -> None:
		"""
		Requests activation of a packet data connection with the network using this bearer's properties.
		Upon successful activation, the modem can send and receive packet data and, depending on the addressing
		capability of the modem, a connection manager may need to start PPP, perform DHCP, or assign the IP address
		returned by the modem to the data interface. Upon successful return, the "Ip4Config" and/or "Ip6Config"
		properties become valid and may contain IP configuration information for the data interface associated with
		this bearer.
		"""
		raise NotImplementedError

	@dbus_method()
	def disconnect(self) -> None:
		"""
		Disconnect and deactivate this packet data connection.
		
		Any ongoing data session will be terminated and IP addresses become invalid when this method is called.
		"""
		raise NotImplementedError

	@dbus_property('s')
	def interface(self) -> str:
		"""
		The operating system name for the network data interface that provides packet data using this bearer.

		Connection managers must configure this interface depending on the IP "method" given by the "Ip4Config" or
		"Ip6Config" properties set by bearer activation.

		If MM_BEARER_IP_METHOD_STATIC or MM_BEARER_IP_METHOD_DHCP methods are given, the interface will be an
		ethernet-style interface suitable for DHCP or setting static IP configuration on, while if the
		MM_BEARER_IP_METHOD_PPP method is given, the interface will be a serial TTY which must then have PPP run
		over it.
		"""
		raise NotImplementedError

	@dbus_property('b')
	def connected(self) -> bool:
		"""
		Indicates whether or not the bearer is connected and thus whether packet data communication using this bearer
		is possible.
		"""
		raise NotImplementedError

	@dbus_property('b')
	def suspended(self) -> bool:
		"""
		In some devices, packet data service will be suspended while the device is handling other communication, like
		a voice call. If packet data service is suspended (but not deactivated) this property will be TRUE.
		"""
		raise NotImplementedError

	@dbus_property('a{sv}')
	def ip4_config(self) -> Tuple[str]:
		"""
		If the bearer was configured for IPv4 addressing, upon activation this property contains the addressing details for assignment to the data interface.
		
		Mandatory items include:
		
		"method"
			A MMBearerIpMethod, given as an unsigned integer value (signature "u").
			If the bearer specifies configuration via PPP or DHCP, only the "method" item will be present.
			Additional items which are only applicable when using the MM_BEARER_IP_METHOD_STATIC method are:
		"address"
			IP address, given as a string value (signature "s").
		"prefix"
			Numeric CIDR network prefix (ie, 24, 32, etc), given as an unsigned integer value (signature "u").
		"dns1"
			IP address of the first DNS server, given as a string value (signature "s").
		"dns2"
			IP address of the second DNS server, given as a string value (signature "s").
		"dns3"
			IP address of the third DNS server, given as a string value (signature "s").
		"gateway"
			IP address of the default gateway, given as a string value (signature "s").
			This property may also include the following items when such information is available:
		"mtu"
			Maximum transmission unit (MTU), given as an unsigned integer value (signature "u").
		"""
		raise NotImplementedError

	@dbus_property(property_signature='a{sv}')
	def stats(self) -> Dict[str, Tuple[str, Any]]:
		"""If the modem supports it, this property will show statistics associated to the bearer."""
		raise NotImplementedError
