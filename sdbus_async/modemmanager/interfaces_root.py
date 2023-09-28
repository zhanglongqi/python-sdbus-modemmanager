from typing import Any, Dict, List, Tuple

from sdbus import DbusInterfaceCommonAsync, dbus_method_async, dbus_property_async


class MMInterfaceAsync(DbusInterfaceCommonAsync, interface_name='org.freedesktop.ModemManager1'):
	"""Main modem manager interface"""

	@dbus_method_async()
	async def scan_devices(self) -> None:
		"""Start a new scan for connected modem devices."""
		raise NotImplementedError

	@dbus_method_async(input_signature='s')
	async def set_logging(self, level: str) -> None:
		"""Set logging verbosity.

		:param level: One of "ERR", "WARN", "INFO", "DEBUG".
		"""
		raise NotImplementedError

	@dbus_method_async(input_signature='a{sv}')
	async def report_kernel_event(self, properties: Dict[str, Tuple[str, Any]]) -> None:
		"""Reports a kernel event to ModemManager."""
		raise NotImplementedError

	@dbus_method_async(input_signature='sb')
	async def inhibit_device(self, uid: str, inhibit: bool) -> None:
		"""Inhibit or uninhibit the device.

		:param uid: The unique ID of the physical device
		:param inhibit: True to inhibit the modem and False to uninhibit it
		"""
		raise NotImplementedError

	@dbus_property_async(property_signature='s')
	def version(self) -> str:
		"""NetworkManager version"""
		raise NotImplementedError
