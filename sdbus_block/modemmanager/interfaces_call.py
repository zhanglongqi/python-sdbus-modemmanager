from typing import Any, Dict

from sdbus import DbusInterfaceCommon, dbus_method, dbus_property


class MMCallInterface(DbusInterfaceCommon, interface_name='org.freedesktop.ModemManager1.Call'):

	@dbus_method()
	def start(self) -> None:
		"""If the outgoing call has not yet been started, start it."""
		raise NotImplementedError

	@dbus_method()
	def accept(self) -> None:
		"""Accept incoming call (answer)."""
		raise NotImplementedError

	@dbus_method(input_signature='s')
	def deflect(self, number: str) -> None:
		"""Deflect an incoming or waiting call to a new number.

		:param number: new number where the call will be deflected.
		"""
		raise NotImplementedError

	@dbus_method()
	def join_multiparty(self) -> None:
		"""
		Join the currently held call into a single multiparty call with another already active call.
		"""
		raise NotImplementedError

	@dbus_method()
	def leave_multiparty(self) -> None:
		"""
		If this call is part of an ongoing multiparty call, detach it from the multiparty call,
		put the multiparty call on hold, and activate this one alone.
		"""
		raise NotImplementedError

	@dbus_method()
	def hangup(self) -> None:
		"""Hangup the active call."""
		raise NotImplementedError

	@dbus_method(input_signature='s')
	def send_dtmf(self, dtmf: str) -> None:
		"""
		Send a DTMF tone (Dual Tone Multi-Frequency) (only on supported modem).

		:param dtmf: DTMF tone identifier [0-9A-D*#].
		"""
		raise NotImplementedError

	@dbus_property('i')
	def state(self) -> int:
		"""A MMCallState value, describing the state of the call."""
		raise NotImplementedError

	@dbus_property('i')
	def state_reason(self) -> int:
		"""A MMCallStateReason value, describing why the state is changed."""
		raise NotImplementedError

	@dbus_property('i')
	def direction(self) -> int:
		"""A MMCallDirection value, describing the direction of the call."""
		raise NotImplementedError

	@dbus_property('s')
	def number(self) -> str:
		"""The remote phone number."""
		raise NotImplementedError

	@dbus_property('b')
	def multiparty(self) -> bool:
		"""Whether the call is currently part of a multiparty conference call."""
		raise NotImplementedError

	@dbus_property('s')
	def audio_port(self) -> str:
		"""Name of the kernel device that provides the audio (if call audio is routed via the host)."""
		raise NotImplementedError

	@dbus_property('a{sv}')
	def audio_format(self) -> Dict[str, Any]:
		# TODO Add description and create data type.
		raise NotImplementedError
