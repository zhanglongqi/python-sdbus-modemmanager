from typing import Any, Dict, List, Tuple

from sdbus import DbusInterfaceCommonAsync, DbusObjectManagerInterfaceAsync, dbus_method_async, dbus_property_async, dbus_signal_async


class MMModemsInterfaceAsync(DbusObjectManagerInterfaceAsync):
	"""
	Modem objects are exported in DBus with the following path base: /org/freedesktop/ModemManager1/Modems/#, where # 
	indicates a unique unsigned integer which identifies the object.
	
	The Modem objects will export a generic Modem interface which includes common features and actions applicable to 
	most modem types. This interface, among other actions, allows the management (creation, listing, deletion) of B
	earer objects which can then be used to request the modem to get in connected state.
	
	Modem objects will also export the generic Simple interface. This interface provides an easy access to the most 
	simple and common operations that may be performed with the modem, including connection and disconnection. Users 
	of the Simple interface do not need to take care of getting the modem registered, and they also don't need to manage 
	the creation of bearers themselves. All the logic required to get the modem connected or disconnected is handled 
	by the Simple interface.

	Modems with specific 3GPP and/or CDMA capabilities will export modem type specific interfaces, like the 3GPP 
	interface or the CDMA interface.
	"""
	pass


class MMModemInterfaceAsync(DbusInterfaceCommonAsync, interface_name='org.freedesktop.ModemManager1.Modem'):
	"""Main modem manager interface"""

	@dbus_method_async(input_signature='b')
	async def enable(self, enable: bool) -> None:
		"""
		Enable or disable the modem.

		When enabled, the modem's radio is powered on and data sessions, voice calls, location services, and Short Message Service may be available.
		When disabled, the modem enters low-power state and no network-related operations are available.

		:param enable: True to enable the modem and False to disable it.
		"""
		raise NotImplementedError

	@dbus_method_async(result_signature='ao')
	async def list_bearers(self) -> List[str]:
		raise NotImplementedError

	@dbus_method_async(input_signature='a{sv}', result_signature='o')
	async def create_bearer(self, properties: Dict[str, Tuple[str, Any]]) -> str:
		raise NotImplementedError

	@dbus_method_async(input_signature='o')
	async def delete_bearer(self, bearer: str) -> None:
		raise NotImplementedError

	@dbus_method_async()
	async def reset(self) -> None:
		raise NotImplementedError

	@dbus_method_async(input_signature='s')
	async def factory_reset(self, code: str) -> None:
		raise NotImplementedError

	@dbus_method_async(input_signature='u')
	async def set_power_state(self, state: int) -> None:
		raise NotImplementedError

	@dbus_method_async(input_signature='u')
	async def set_current_capabilities(self, capabilities: int) -> None:
		raise NotImplementedError

	@dbus_method_async(input_signature='(uu)')
	async def set_current_modes(self, modes: Tuple[int, int]) -> None:
		raise NotImplementedError

	@dbus_method_async(input_signature='au')
	async def set_current_bands(self, bands: List[int]) -> None:
		raise NotImplementedError

	@dbus_method_async(input_signature='u')
	async def set_primary_sim_slot(self, sim_slot: int) -> None:
		raise NotImplementedError

	@dbus_method_async(result_signature='aa{sv}')
	async def get_cell_info(self) -> List[Dict[str, Tuple[str, Any]]]:
		raise NotImplementedError

	@dbus_method_async(input_signature='su', result_signature='s')
	async def command(self, cmd: str, timeout: int) -> str:
		raise NotImplementedError

	@dbus_property_async(property_signature='o', property_name='Sim')
	def sim_object_path(self) -> str:
		"""The path of the SIM object available in this device, if any."""
		raise NotImplementedError

	@dbus_property_async(property_signature='ao')
	def sim_slots(self) -> List[str]:
		raise NotImplementedError

	@dbus_property_async(property_signature='u')
	def primary_sim_slot(self) -> int:
		raise NotImplementedError

	@dbus_property_async(property_signature='ao', property_name='Bearers')
	def bearer_object_paths(self) -> List[str]:
		"""
		The list of bearer object paths (EPS Bearers, PDP Contexts, or CDMA2000 Packet Data Sessions) as requested by 
		the user.
		This list does not include the initial EPS bearer details (see "InitialEpsBearer").
		"""
		raise NotImplementedError

	@dbus_property_async(property_signature='au')
	def supported_capabilities(self) -> List[int]:
		raise NotImplementedError

	@dbus_property_async(property_signature='u')
	def current_capabilities(self) -> int:
		raise NotImplementedError

	@dbus_property_async(property_signature='u')
	def max_bearers(self) -> int:
		raise NotImplementedError

	@dbus_property_async(property_signature='u')
	def max_active_bearers(self) -> int:
		raise NotImplementedError

	@dbus_property_async(property_signature='u')
	def max_active_multiplexed_bearers(self) -> int:
		raise NotImplementedError

	@dbus_property_async(property_signature='s')
	def manufacturer(self) -> str:
		"""The equipment manufacturer, as reported by the modem."""
		raise NotImplementedError

	@dbus_property_async(property_signature='s')
	def model(self) -> str:
		"""The equipment model, as reported by the modem."""
		raise NotImplementedError

	@dbus_property_async(property_signature='s')
	def revision(self) -> str:
		"""The revision identification of the software, as reported by the modem."""
		raise NotImplementedError

	@dbus_property_async(property_signature='s')
	def carrier_configuration(self) -> str:
		raise NotImplementedError

	@dbus_property_async(property_signature='s')
	def carrier_configuration_revision(self) -> str:
		raise NotImplementedError

	@dbus_property_async(property_signature='s')
	def hardware_revision(self) -> str:
		"""The revision identification of the hardware, as reported by the modem."""
		raise NotImplementedError

	@dbus_property_async(property_signature='s')
	def device_identifier(self) -> str:
		"""
		A best-effort device identifier based on various device information like model name, firmware revision, 
		USB/PCI/PCMCIA IDs, and other properties.
		This ID is not guaranteed to be unique and may be shared between identical devices with the same firmware, but 
		is intended to be "unique enough" for use as a casual device identifier for various user experience operations.
		This is not the device's IMEI or ESN since those may not be available before unlocking the device via a PIN.
		"""
		raise NotImplementedError

	@dbus_property_async(property_signature='s')
	def device(self) -> str:
		raise NotImplementedError

	@dbus_property_async(property_signature='as')
	def drivers(self) -> List[str]:
		raise NotImplementedError

	@dbus_property_async(property_signature='s')
	def plugin(self) -> str:
		raise NotImplementedError

	@dbus_property_async(property_signature='s')
	def primary_port(self) -> str:
		"""The name of the primary port using to control the modem."""
		raise NotImplementedError

	@dbus_property_async(property_signature='a(su)')
	def ports(self) -> List[Tuple[str, int]]:
		raise NotImplementedError

	@dbus_property_async(property_signature='s')
	def equipment_identifier(self) -> str:
		"""
		The identity of the device.
		This will be the IMEI number for GSM devices and the hex-format ESN/MEID for CDMA devices.
		"""
		raise NotImplementedError

	@property
	def imei(self):
		return self.equipment_identifier

	@dbus_property_async(property_signature='u')
	def unlock_required(self) -> int:
		raise NotImplementedError

	@dbus_property_async(property_signature='a{uu}')
	def unlock_retries(self) -> Dict[int, int]:
		raise NotImplementedError

	@dbus_property_async(property_signature='i')
	def state(self) -> int:
		"""
		Overall state of the modem, given as a MMModemState value.
		If the device's state cannot be determined, MM_MODEM_STATE_UNKNOWN will be reported.
		"""
		raise NotImplementedError

	@dbus_property_async(property_signature='u')
	def state_failed_reason(self) -> int:
		"""
		Error specifying why the modem is in MM_MODEM_STATE_FAILED state,
		given as a MMModemStateFailedReason value.
		"""
		raise NotImplementedError

	@dbus_property_async(property_signature='u')
	def access_technologies(self) -> int:
		raise NotImplementedError

	@dbus_property_async(property_signature='(ub)')
	def signal_quality(self) -> Tuple[int, bool]:
		"""
		Signal quality in percent (0 - 100) of the dominant access technology the device is using to communicate with the network. Always 0 for POTS devices.
		The additional boolean value indicates if the quality value given was recently taken.		
		"""
		raise NotImplementedError

	@dbus_property_async(property_signature='as')
	def own_numbers(self) -> List[str]:
		"""List of numbers (e.g. MSISDN in 3GPP) being currently handled by this modem."""
		raise NotImplementedError

	@dbus_property_async(property_signature='u')
	def power_state(self) -> int:
		"""A MMModemPowerState value specifying the current power state of the modem."""
		raise NotImplementedError

	@dbus_property_async(property_signature='a(uu)')
	def supported_modes(self) -> List[Tuple[int, int]]:
		raise NotImplementedError

	@dbus_property_async(property_signature='(uu)')
	def current_modes(self) -> Tuple[int, int]:
		raise NotImplementedError

	@dbus_property_async(property_signature='au')
	def supported_bands(self) -> List[int]:
		raise NotImplementedError

	@dbus_property_async(property_signature='au')
	def current_bands(self) -> List[int]:
		raise NotImplementedError

	@dbus_property_async(property_signature='u')
	def supported_ip_families(self) -> int:
		raise NotImplementedError

	@dbus_signal_async(signal_signature='iiu')
	def state_changed(self) -> Tuple[int, int, int]:
		raise NotImplementedError


class MMModemMessagingInterfaceAsync(DbusInterfaceCommonAsync, interface_name='org.freedesktop.ModemManager1.Modem.Messaging'):
	"""The Messaging interface handles sending SMS messages and notification of new incoming messages."""

	@dbus_method_async(result_signature='ao')
	async def list(self) -> List[str]:
		"""Retrieve all SMS messages."""
		raise NotImplementedError

	@dbus_method_async(input_signature='o')
	async def delete(self, path: str) -> None:
		"""Delete an SMS message."""
		raise NotImplementedError

	@dbus_method_async(input_signature='a{sv}', result_signature='o')
	async def create(self, properties: Dict[str, Tuple[str, Any]]) -> str:
		"""Creates a new message object."""
		raise NotImplementedError

	@dbus_property_async(property_signature='ao')
	def messages(self) -> List[str]:
		"""The list of SMS object paths."""
		raise NotImplementedError

	@dbus_property_async(property_signature='au')
	def supported_storages(self) -> List[int]:
		"""A list of MMSmsStorage values, specifying the storages supported by this modem for storing and receiving SMS."""
		raise NotImplementedError

	@dbus_property_async(property_signature='u')
	def default_storage(self) -> int:
		"""A MMSmsStorage value, specifying the storage to be used when receiving or storing SMS."""
		raise NotImplementedError

	@dbus_signal_async(signal_signature='ob')
	def added(self) -> Tuple[str, bool]:
		"""Emitted when any part of a new SMS has been received or added (but not for subsequent parts, if any)."""
		raise NotImplementedError

	@dbus_signal_async(signal_signature='o')
	def deleted(self) -> str:
		"""Emitted when a message has been deleted."""
		raise NotImplementedError


class MMModemSimpleInterfaceAsync(DbusInterfaceCommonAsync, interface_name='org.freedesktop.ModemManager1.Modem.Simple'):

	@dbus_method_async(input_signature='a{sv}', result_signature='o')
	async def connect(self, properties: Dict[str, Tuple[str, Any]]) -> str:
		"""
		Allowed key/value pairs in properties are:

		"pin"
			SIM-PIN unlock code, given as a string value (signature "s").
		"operator-id"
			ETSI MCC-MNC of a network to force registration with, given as a string value (signature "s").
		"apn"
			For GSM/UMTS and LTE devices the APN to use, given as a string value (signature "s").
		"ip-type"
			For GSM/UMTS and LTE devices the IP addressing type to use, given as a MMBearerIpFamily value (signature "u").
		"allowed-auth"
			The authentication method to use, given as a MMBearerAllowedAuth value (signature "u"). Optional in 3GPP.
		"user"
			User name (if any) required by the network, given as a string value (signature "s"). Optional in 3GPP.
		"password"
			Password (if any) required by the network, given as a string value (signature "s"). Optional in 3GPP.
		"number"
			For POTS devices the number to dial, given as a string value (signature "s").
		"allow-roaming"
			False to allow only connections to home networks, given as a boolean value (signature "b").
		"rm-protocol"
			For CDMA devices, the protocol of the Rm interface, given as a MMModemCdmaRmProtocol value (signature "u").

		:param properties: Dictionary of properties needed to get the modem connected.
		:returns: On successful connect, returns the object path of the connected packet data bearer used for the connection attempt.
		"""
		raise NotImplementedError

	@dbus_method_async(input_signature='o')
	async def disconnect(self, bearer: str) -> None:
		"""
		data bearer, while if "/" (ie, no object given) this method will disconnect all active packet data bearers.
		Disconnect an active packet data connection.
		:param bearer: If given this method will disconnect the referenced packet
		"""
		raise NotImplementedError

	@dbus_method_async(result_signature='a{sv}')
	async def get_status(self) -> Dict[str, Tuple[str, Any]]:
		"""
		Get the general modem status.

		The predefined common properties returned are:

		"state"
			A MMModemState value specifying the overall state of the modem, given as an unsigned integer value (signature "u").
		"signal-quality"
			Signal quality value, given only when registered, as an unsigned integer value (signature "u").
		"current-bands"
			List of MMModemBand values, given only when registered, as a list of unsigned integer values (signature "au").
		"access-technology"
			A MMModemAccessTechnology value, given only when registered, as an unsigned integer value (signature "u").
		"m3gpp-registration-state"
			A MMModem3gppRegistrationState value specifying the state of the registration, given only when registered in a 3GPP network, as an unsigned integer value (signature "u").
		"m3gpp-operator-code"
			Operator MCC-MNC, given only when registered in a 3GPP network, as a string value (signature "s").
		"m3gpp-operator-name"
			Operator name, given only when registered in a 3GPP network, as a string value (signature "s").
		"cdma-cdma1x-registration-state"
			A MMModemCdmaRegistrationState value specifying the state of the registration, given only when registered in a CDMA1x network, as an unsigned integer value (signature "u").
		"cdma-evdo-registration-state"
			A MMModemCdmaRegistrationState value specifying the state of the registration, given only when registered in a EV-DO network, as an unsigned integer value (signature "u").
		"cdma-sid"
			The System Identifier of the serving network, if registered in a CDMA1x network and if known. Given as an unsigned integer value (signature "u").
		"cdma-nid"
			The Network Identifier of the serving network, if registered in a CDMA1x network and if known. Given as an unsigned integer value (signature "u").
		
		:returns: Dictionary of properties.
		"""
		raise NotImplementedError


class MMModemSignalInterfaceAsync(DbusInterfaceCommonAsync, interface_name='org.freedesktop.ModemManager1.Modem.Signal'):

	@dbus_method_async(input_signature='u')
	async def setup(self, rate: int) -> None:
		"""Setup extended signal quality information retrieval.
		
		:param rate: Refresh rate to set, in seconds. 0 to disable retrieval.
		"""
		raise NotImplementedError

	@dbus_method_async(input_signature='a{sv}')
	async def setup_thresholds(self, settings: Dict[str, Tuple[str, Any]]) -> None:
		raise NotImplementedError

	@dbus_property_async(property_signature='u')
	def rate(self) -> int:
		"""
		Refresh rate for the extended signal quality information updates, in seconds.
		A value of 0 disables the retrieval of the values.
		"""
		raise NotImplementedError

	@dbus_property_async(property_signature='u')
	def rssi_threshold(self) -> int:
		raise NotImplementedError

	@dbus_property_async(property_signature='b')
	def error_rate_threshold(self) -> bool:
		raise NotImplementedError

	@dbus_property_async(property_signature='a{sv}')
	def cdma(self) -> Dict[str, Tuple[str, Any]]:
		"""
		Dictionary of available signal information for the CDMA1x access technology.
		"""
		raise NotImplementedError

	@dbus_property_async(property_signature='a{sv}')
	def evdo(self) -> Dict[str, Tuple[str, Any]]:
		"""
		Dictionary of available signal information for the CDMA EV-DO access technology.
		"""
		raise NotImplementedError

	@dbus_property_async(property_signature='a{sv}')
	def gsm(self) -> Dict[str, Tuple[str, Any]]:
		"""
		Dictionary of available signal information for the GSM/GPRS access technology.
		"""
		raise NotImplementedError

	@dbus_property_async(property_signature='a{sv}')
	def umts(self) -> Dict[str, Tuple[str, Any]]:
		"""
		Dictionary of available signal information for the UMTS (WCDMA) access technology.
		"""
		raise NotImplementedError

	@dbus_property_async(property_signature='a{sv}')
	def lte(self) -> Dict[str, Tuple[str, Any]]:
		"""
		Dictionary of available signal information for the LTE access technology.
		"""
		raise NotImplementedError

	@dbus_property_async(property_signature='a{sv}')
	def nr5g(self) -> Dict[str, Tuple[str, Any]]:
		"""
		Dictionary of available signal information for the 5G access technology.
		"""
		raise NotImplementedError


class MMModemVoiceInterfaceAsync(DbusInterfaceCommonAsync, interface_name='org.freedesktop.ModemManager1.Modem.Voice'):

	@dbus_method_async(result_signature='ao')
	async def list_calls(self) -> List[str]:
		"""
		Retrieve all Calls.

		:returns: The list of call object paths.
		"""
		raise NotImplementedError

	@dbus_method_async(input_signature='o')
	async def delete_call(self, path: str) -> None:
		"""
		Delete a Call from the list of calls.
		The call will be hangup if it is still active.

		:param path: The object path of the Call to delete.
		"""
		raise NotImplementedError

	@dbus_method_async(input_signature='a{sv}', result_signature='o')
	async def create_call(self, properties: Dict[str, Tuple[str, Any]]) -> str:
		"""
		Creates a new call object for a new outgoing call.
		The 'Number' is the only expected property to set by the user.

		:param properties: Call properties from the Call D-Bus interface.
		:returns: The object path of the new call object.
		"""
		raise NotImplementedError

	@dbus_method_async()
	async def hold_and_accept(self) -> None:
		"""Place all active calls on hold, if any, and accept the next call."""
		raise NotImplementedError

	@dbus_method_async()
	async def hangup_and_accept(self) -> None:
		"""Hangup all active calls, if any, and accept the next call."""
		raise NotImplementedError

	@dbus_method_async()
	async def hangup_all(self) -> None:
		"""Hangup all active calls."""
		raise NotImplementedError

	@dbus_method_async()
	async def transfer(self) -> None:
		"""
		Join the currently active and held calls together into a single multiparty call,
		but disconnects from them.
		"""
		raise NotImplementedError

	@dbus_method_async(input_signature='b')
	async def call_waiting_setup(self, enable: bool) -> None:
		"""Activates or deactivates the call waiting network service, as per 3GPP TS 22.083."""
		raise NotImplementedError

	@dbus_method_async(result_signature='b')
	async def call_waiting_query(self) -> bool:
		"""Queries the status of the call waiting network service, as per 3GPP TS 22.083."""
		raise NotImplementedError

	@dbus_property_async(property_signature='ao', property_name='Calls')
	def call_object_paths(self) -> List[str]:
		"""The list of calls object paths."""
		raise NotImplementedError

	@dbus_property_async(property_signature='b')
	def emergency_only(self) -> bool:
		"""A flag indicating whether emergency calls are the only allowed ones."""
		raise NotImplementedError

	@dbus_signal_async(signal_signature='o')
	def call_added(self) -> str:
		"""Emitted when a call has been added."""
		raise NotImplementedError

	@dbus_signal_async(signal_signature='o')
	def call_deleted(self) -> str:
		"""Emitted when a call has been deleted."""
		raise NotImplementedError
