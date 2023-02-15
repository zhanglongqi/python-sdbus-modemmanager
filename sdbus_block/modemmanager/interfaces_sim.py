from sdbus import DbusInterfaceCommon, dbus_method, dbus_property


class MMSimInterface(DbusInterfaceCommon, interface_name='org.freedesktop.ModemManager1.Sim'):
	"""The SIM interface handles communication with SIM, USIM, and RUIM (CDMA SIM) cards."""

	@dbus_method(input_signature='s')
	def send_pin(self, pin: str = '') -> None:
		"""
        Send the PIN to unlock the SIM card.
			IN s pin:
			A string containing the PIN code.
        Raises:
            NotImplementedError: _description_
        """
		raise NotImplementedError

	@dbus_method(input_signature='ss')
	def send_puk(self, puk: str = '', pin: str = '') -> None:
		"""
        Send the PUK and a new PIN to unlock the SIM card.
			IN s puk:
			A string containing the PUK code.
			IN s pin:
			A string containing the PIN code.
        Raises:
            NotImplementedError: _description_
        """
		raise NotImplementedError

	@dbus_method(input_signature='sb')
	def enable_pin(self, pin: str = '', enable: bool = False) -> None:
		"""
        Enable or disable the PIN checking.
			IN s pin:
			A string containing the PIN code.
			IN b enabled:
			TRUE to enable PIN checking, FALSE otherwise.
        Raises:
            NotImplementedError: _description_
        """
		raise NotImplementedError

	@dbus_method(input_signature='ss')
	def change_pin(self, old_pin: str = '', new_pin: str = '') -> None:
		"""
        Change the PIN code.
			IN s old_pin:
			A string containing the current PIN code.
			IN s new_pin:
			A string containing the new PIN code.
        Raises:
            NotImplementedError: _description_
        """
		raise NotImplementedError

	@dbus_property('s')
	def sim_identifier(self) -> str:
		"""The ICCID of the SIM card.
		This may be available before the PIN has been entered depending on the device itself.
		"""
		raise NotImplementedError

	@dbus_property('s')
	def imsi(self) -> str:
		"""
		The IMSI of the SIM card, if any.
		"""
		raise NotImplementedError

	@dbus_property('s')
	def operator_identifier(self) -> str:
		raise NotImplementedError

	@dbus_property('s')
	def operator_name(self) -> str:
		"""
		The name of the network operator, as given by the SIM card, if known.
		"""
		raise NotImplementedError
