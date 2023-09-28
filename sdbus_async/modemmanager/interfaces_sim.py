from typing import List, Tuple

from sdbus import DbusInterfaceCommonAsync, dbus_method_async, dbus_property_async


class MMSimInterfaceAsync(DbusInterfaceCommonAsync, interface_name='org.freedesktop.ModemManager1.Sim'):
	"""The SIM interface handles communication with SIM, USIM, and RUIM (CDMA SIM) cards."""

	@dbus_method_async(input_signature='s')
	async def send_pin(self, pin: str) -> None:
		"""
		Send the PIN to unlock the SIM card.

		:param pin: A string containing the PIN code.
		"""
		raise NotImplementedError

	@dbus_method_async(input_signature='ss')
	async def send_puk(self, puk: str, pin: str) -> None:
		"""
		Send the PUK and a new PIN to unlock the SIM card.

		:param puk: A string containing the PUK code.
		:param pin: A string containing the PIN code.
		"""
		raise NotImplementedError

	@dbus_method_async(input_signature='sb')
	async def enable_pin(self, pin: str, enable: bool) -> None:
		"""
		Enable or disable the PIN checking.

		:param pin: A string containing the PIN code.
		:param enable: TRUE to enable PIN checking, FALSE otherwise.
		"""
		raise NotImplementedError

	@dbus_method_async(input_signature='ss')
	async def change_pin(self, old_pin: str, new_pin: str) -> None:
		"""
		Change the PIN code.

		:param old_pin: A string containing the current PIN code.
		:param new_pin: A string containing the new PIN code.
		"""
		raise NotImplementedError

	@dbus_method_async(input_signature='a(su)')
	async def set_preferred_networks(self, preferred_networks: List[Tuple[str, int]]) -> None:
		"""
		Stores the provided preferred network list to the SIM card.

		Each entry contains an operator id string ("MCCMNC") consisting of 5 or 6 digits,
		and an MMModemAccessTechnology mask to store to SIM card if supported.

		:param preferred_networks: Operator id string and MMModemAccessTechnology mask.
		"""
		raise NotImplementedError

	@dbus_property_async(property_signature='b')
	def active(self) -> bool:
		"""Boolean indicating whether the SIM is currently active."""
		raise NotImplementedError

	@dbus_property_async(property_signature='s')
	def sim_identifier(self) -> str:
		"""
		The ICCID of the SIM card.
		This may be available before the PIN has been entered depending on the device itself.
		"""
		raise NotImplementedError

	@dbus_property_async(property_signature='s')
	def imsi(self) -> str:
		"""The IMSI of the SIM card, if any."""
		raise NotImplementedError

	@dbus_property_async(property_signature='s')
	def eid(self) -> str:
		"""The EID of the SIM card, if any."""
		raise NotImplementedError

	@dbus_property_async(property_signature='s')
	def operator_identifier(self) -> str:
		raise NotImplementedError

	@dbus_property_async(property_signature='s')
	def operator_name(self) -> str:
		"""The name of the network operator, as given by the SIM card, if known."""
		raise NotImplementedError

	@dbus_property_async(property_signature='as')
	def emergency_numbers(self) -> List[str]:
		"""List of emergency numbers programmed in the SIM card."""
		raise NotImplementedError

	@dbus_property_async(property_signature='a(su)')
	def preferred_networks(self) -> List[Tuple[str, int]]:
		"""
		List of preferred networks with access technologies configured in the SIM card.

		Each entry contains an operator id string ("MCCMNC") consisting of 5 or 6 digits,
		and an MMModemAccessTechnology mask to store to SIM card if supported.
		"""
		raise NotImplementedError

	@dbus_property_async(property_signature='ay')
	def gid1(self) -> bytes:
		"""Group identifier level 1."""
		raise NotImplementedError

	@dbus_property_async(property_signature='ay')
	def gid2(self) -> bytes:
		"""Group identifier level 2."""
		raise NotImplementedError

	@dbus_property_async(property_signature='u')
	def sim_type(self) -> int:
		"""Indicates whether the current primary SIM is a ESIM or a physical SIM, given as MMSimType value."""
		raise NotImplementedError

	@dbus_property_async(property_signature='u')
	def esim_status(self) -> int:
		"""If current SIM is ESIM then this indicates whether there is a profile or not, given as MMSimEsimStatus value."""
		raise NotImplementedError

	@dbus_property_async(property_signature='u')
	def removability(self) -> int:
		"""Indicates whether the current SIM is a removable SIM or not, given as a MMSimRemovability value."""
		raise NotImplementedError
