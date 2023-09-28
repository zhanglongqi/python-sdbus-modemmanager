from typing import Any, Dict, List, Tuple

from sdbus import DbusInterfaceCommon, dbus_method, dbus_property


class MMInterface(DbusInterfaceCommon, interface_name='org.freedesktop.ModemManager1'):
	"""Main modem manager interface"""

	@dbus_method()
	def scan_devices(self) -> None:
		"""Start a new scan for connected modem devices."""
		raise NotImplementedError

	@dbus_method(input_signature='s')
	def set_logging(self, level: str) -> None:
		"""Set logging verbosity.

		:param level: One of "ERR", "WARN", "INFO", "DEBUG".
		"""
		raise NotImplementedError

	@dbus_method(input_signature='a{sv}')
	def report_kernel_event(self, properties: Dict[str, Tuple[str, Any]]) -> None:
		"""Reports a kernel event to ModemManager."""
		raise NotImplementedError

	@dbus_method(input_signature='sb')
	def inhibit_device(self, uid: str, inhibit: bool) -> None:
		"""Inhibit or uninhibit the device.

		:param uid: The unique ID of the physical device
		:param inhibit: True to inhibit the modem and False to uninhibit it
		"""
		raise NotImplementedError

	@dbus_property('s')
	def version(self) -> str:
		"""NetworkManager version"""
		raise NotImplementedError
