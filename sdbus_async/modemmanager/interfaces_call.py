from typing import Any, Dict, Tuple

from sdbus import DbusInterfaceCommonAsync, dbus_method_async, dbus_property_async, dbus_signal_async


class MMCallInterfaceAsync(DbusInterfaceCommonAsync, interface_name='org.freedesktop.ModemManager1.Call'):

	@dbus_method_async()
	async def start(self) -> None:
		"""If the outgoing call has not yet been started, start it."""
		raise NotImplementedError

	@dbus_method_async()
	async def accept(self) -> None:
		"""Accept incoming call (answer)."""
		raise NotImplementedError

	@dbus_method_async(input_signature='s')
	async def deflect(self, number: str) -> None:
		"""Deflect an incoming or waiting call to a new number.

		:param number: new number where the call will be deflected.
		"""
		raise NotImplementedError

	@dbus_method_async()
	async def join_multiparty(self) -> None:
		"""
		Join the currently held call into a single multiparty call with another already active call.
		"""
		raise NotImplementedError

	@dbus_method_async()
	async def leave_multiparty(self) -> None:
		"""
		If this call is part of an ongoing multiparty call, detach it from the multiparty call,
		put the multiparty call on hold, and activate this one alone.
		"""
		raise NotImplementedError

	@dbus_method_async()
	async def hangup(self) -> None:
		"""Hangup the active call."""
		raise NotImplementedError

	@dbus_method_async(input_signature='s')
	async def send_dtmf(self, dtmf: str) -> None:
		"""
		Send a DTMF tone (Dual Tone Multi-Frequency) (only on supported modem).

		:param dtmf: DTMF tone identifier [0-9A-D*#].
		"""
		raise NotImplementedError

	@dbus_property_async(property_signature='i')
	def state(self) -> int:
		"""A MMCallState value, describing the state of the call."""
		raise NotImplementedError

	@dbus_property_async(property_signature='i')
	def state_reason(self) -> int:
		"""A MMCallStateReason value, describing why the state is changed."""
		raise NotImplementedError

	@dbus_property_async(property_signature='i')
	def direction(self) -> int:
		"""A MMCallDirection value, describing the direction of the call."""
		raise NotImplementedError

	@dbus_property_async(property_signature='s')
	def number(self) -> str:
		"""The remote phone number."""
		raise NotImplementedError

	@dbus_property_async(property_signature='b')
	def multiparty(self) -> bool:
		"""Whether the call is currently part of a multiparty conference call."""
		raise NotImplementedError

	@dbus_property_async(property_signature='s')
	def audio_port(self) -> str:
		"""Name of the kernel device that provides the audio (if call audio is routed via the host)."""
		raise NotImplementedError

	@dbus_property_async(property_signature='a{sv}')
	def audio_format(self) -> Dict[str, Tuple[str, Any]]:
		raise NotImplementedError

	@dbus_signal_async(signal_signature='s')
	def dtmf_received(self) -> str:
		raise NotImplementedError

	@dbus_signal_async(signal_signature='iiu')
	def state_changed(self) -> Tuple[int, int, int]:
		raise NotImplementedError
