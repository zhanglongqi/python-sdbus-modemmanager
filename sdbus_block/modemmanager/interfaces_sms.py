from typing import Any, Tuple

from sdbus import DbusInterfaceCommon, dbus_method, dbus_property


class MMSmsInterface(DbusInterfaceCommon, interface_name='org.freedesktop.ModemManager1.Sms'):
	"""The SMS interface defines operations and properties of a single SMS message."""

	@dbus_method()
	def send(self) -> None:
		"""If the message has not yet been sent, queue it for delivery."""
		raise NotImplementedError

	@dbus_method(input_signature='u')
	def store(self, storage: int) -> None:
		"""Store the message in the device if not already done."""
		raise NotImplementedError

	@dbus_property(property_signature='u')
	def state(self) -> int:
		"""A MMSmsState value, describing the state of the message."""
		raise NotImplementedError

	@dbus_property(property_signature='u')
	def pdu_type(self) -> int:
		"""A MMSmsPduType value, describing the type of PDUs used in the SMS message."""
		raise NotImplementedError

	@dbus_property(property_signature='s')
	def number(self) -> str:
		"""Number to which the message is addressed."""
		raise NotImplementedError

	@dbus_property(property_signature='s')
	def text(self) -> str:
		"""Message text, in UTF-8."""
		raise NotImplementedError

	@dbus_property(property_signature='ay')
	def data(self) -> bytes:
		"""Message data."""
		raise NotImplementedError

	@dbus_property(property_signature='s')
	def s_m_s_c(self) -> str:
		"""Indicates the SMS service center number."""
		raise NotImplementedError

	@dbus_property(property_signature='(uv)')
	def validity(self) -> Tuple[int, Tuple[str, Any]]:
		"""Indicates when the SMS expires in the SMSC."""
		raise NotImplementedError

	@dbus_property(property_signature='i')
	def Class(self) -> int:
		"""3GPP message class (-1..3)."""
		raise NotImplementedError

	@dbus_property(property_signature='u')
	def teleservice_id(self) -> int:
		"""A MMSmsCdmaTeleserviceId value."""
		raise NotImplementedError

	@dbus_property(property_signature='u')
	def service_category(self) -> int:
		"""A MMSmsCdmaServiceCategory value."""
		raise NotImplementedError

	@dbus_property(property_signature='b')
	def delivery_report_request(self) -> bool:
		"""True if delivery report request is required, False otherwise."""
		raise NotImplementedError

	@dbus_property(property_signature='u')
	def message_reference(self) -> int:
		"""Message Reference of the last PDU sent/received within this SMS."""
		raise NotImplementedError

	@dbus_property(property_signature='s')
	def timestamp(self) -> str:
		"""Time when the first PDU of the SMS message arrived the SMSC, in ISO8601 format."""
		raise NotImplementedError

	@dbus_property(property_signature='s')
	def discharge_timestamp(self) -> str:
		"""Time when the first PDU of the SMS message left the SMSC, in ISO8601 format."""
		raise NotImplementedError

	@dbus_property(property_signature='u')
	def delivery_state(self) -> int:
		"""A MMSmsDeliveryState value, describing the state of the delivery reported in the Status Report message."""
		raise NotImplementedError

	@dbus_property(property_signature='u')
	def storage(self) -> int:
		"""A MMSmsStorage value, describing the storage where this message is kept."""
		raise NotImplementedError
