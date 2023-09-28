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

	@dbus_property('s')
	def version(self) -> str:
		"""NetworkManager version"""
		raise NotImplementedError
