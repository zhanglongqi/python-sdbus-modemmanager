from __future__ import annotations

from typing import Any, Dict, List, Tuple

from sdbus import (
	DbusDeprecatedFlag,
	DbusInterfaceCommon,
	DbusNoReplyFlag,
	DbusPropertyConstFlag,
	DbusPropertyEmitsChangeFlag,
	DbusPropertyEmitsInvalidationFlag,
	DbusPropertyExplicitFlag,
	DbusUnprivilegedFlag,
	dbus_method,
	dbus_property,
)


class MMModemTimeInterface(
	DbusInterfaceCommon,
	interface_name="org.freedesktop.ModemManager1.Modem.Time",
):
	"""
	Get local network time

	:returns: datetime string %Y-%m-%dT%H:%M:%S-%z ex.: '2025-01-22T11:42:37-05'
	"""
	@dbus_method(
		result_signature="s",
		flags=DbusUnprivilegedFlag,
	)
	def get_network_time(
		self,
	) -> str:
		raise NotImplementedError

	"""
	Get local timezone.

	:returns: à dict containing the offset represented in seconds ex.: {'offset': ('i', -300)}

	"""
	@dbus_property(
		property_signature="a{sv}",
		flags=DbusPropertyEmitsChangeFlag,
	)
	def network_timezone(self) -> Dict[str, Tuple[str, Any]]:
		raise NotImplementedError
