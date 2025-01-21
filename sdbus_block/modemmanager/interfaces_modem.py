from typing import Any, Dict, List, Optional, Tuple

from sdbus import DbusInterfaceCommon, DbusObjectManagerInterface, dbus_method, dbus_property

from .enums import MMModemPowerState, MMModemState, MMModemStateFailedReason, MMModemAccessTechnology, MMModemCapability


class MMModemsInterface(DbusObjectManagerInterface):
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


class MMModemInterface(DbusInterfaceCommon, interface_name='org.freedesktop.ModemManager1.Modem'):
	"""Main modem manager interface"""

	@dbus_method(input_signature='b')
	def enable(self, enable: bool = True) -> None:
		"""
		Enable or disable the modem.

		When enabled, the modem's radio is powered on and data sessions, voice calls, location services, and Short Message Service may be available.
		When disabled, the modem enters low-power state and no network-related operations are available.

		:param enable: True to enable the modem and False to disable it.
		"""
		raise NotImplementedError

	@dbus_property('o', property_name='Sim')
	def sim_object_path(self) -> str:
		"""The path of the SIM object available in this device, if any."""
		raise NotImplementedError

	@dbus_property('o', property_name='Bearers')
	def bearer_object_paths(self) -> List[str]:
		"""
		The list of bearer object paths (EPS Bearers, PDP Contexts, or CDMA2000 Packet Data Sessions) as requested by 
		the user.
		This list does not include the initial EPS bearer details (see "InitialEpsBearer").
		"""
		raise NotImplementedError

	@dbus_property('s')
	def manufacturer(self) -> str:
		"""The equipment manufacturer, as reported by the modem."""
		raise NotImplementedError

	@dbus_property('s')
	def model(self) -> str:
		"""The equipment model, as reported by the modem."""
		raise NotImplementedError

	@dbus_property('s', property_name='Revision')
	def revision(self) -> str:
		"""The revision identification of the software, as reported by the modem."""
		raise NotImplementedError

	@dbus_property('s')
	def hardware_revision(self) -> str:
		"""The revision identification of the hardware, as reported by the modem."""
		raise NotImplementedError

	@dbus_property('s')
	def device_identifier(self) -> str:
		"""
		A best-effort device identifier based on various device information like model name, firmware revision, 
		USB/PCI/PCMCIA IDs, and other properties.
		This ID is not guaranteed to be unique and may be shared between identical devices with the same firmware, but 
		is intended to be "unique enough" for use as a casual device identifier for various user experience operations.
		This is not the device's IMEI or ESN since those may not be available before unlocking the device via a PIN.
		"""
		raise NotImplementedError

	@dbus_property('s')
	def primary_port(self) -> str:
		"""The name of the primary port using to control the modem."""
		raise NotImplementedError

	@dbus_property('s')
	def equipment_identifier(self) -> str:
		"""
		The identity of the device.
		This will be the IMEI number for GSM devices and the hex-format ESN/MEID for CDMA devices.
		"""
		raise NotImplementedError

	@property
	def imei(self):
		return self.equipment_identifier

	@dbus_property('i')
	def state(self) -> int:
		"""
		Overall state of the modem, given as a MMModemState value.
		If the device's state cannot be determined, MM_MODEM_STATE_UNKNOWN will be reported.
		"""
		raise NotImplementedError

	@property
	def state_text(self) -> str:
		return MMModemState(self.state).name

	@dbus_property('u')
	def state_failed_reason(self):
		"""
		Error specifying why the modem is in MM_MODEM_STATE_FAILED state,
		given as a MMModemStateFailedReason value.
		"""
		raise NotImplementedError

	@property
	def state_failed_reason_text(self) -> str:
		return MMModemStateFailedReason(self.state_failed_reason).name

	@dbus_property('ub')
	def signal_quality(self):
		"""
		Signal quality in percent (0 - 100) of the dominant access technology the device is using to communicate with the network. Always 0 for POTS devices.
		The additional boolean value indicates if the quality value given was recently taken.		
		"""
		raise NotImplementedError

	@dbus_property('as')
	def own_numbers(self):
		"""List of numbers (e.g. MSISDN in 3GPP) being currently handled by this modem."""
		raise NotImplementedError

	@dbus_property('u')
	def power_state(self):
		"""A MMModemPowerState value specifying the current power state of the modem."""
		raise NotImplementedError

	@property
	def power_state_text(self):
		return MMModemPowerState(self.power_state).name

	@dbus_property('u')
	def access_technologies(self):
		"""
		A MMModemAccessTechnology bitfield that describes the various access technologies
		that device uses when registered with or connected to a network
		"""
		raise NotImplementedError

	@property
	def access_technologies_text(self) -> Optional[str]:
		return MMModemAccessTechnology(self.access_technologies).name

	@dbus_property('u', property_name='CurrentCapabilities')
	def current_capabilities(self) -> int:
		raise NotImplementedError

	@property
	def current_capabilities_text(self) -> Tuple[str]:
		return tuple(MMModemCapability.names(self.current_capabilities))

	@dbus_method(result_signature='aa{sv}')
	def get_cell_info(self) -> List[Dict[str, Tuple[str, Any]]]:
		raise NotImplementedError



class MMModemMessagingInterface(DbusInterfaceCommon, interface_name='org.freedesktop.ModemManager1.Modem.Messaging'):
	"""The Messaging interface handles sending SMS messages and notification of new incoming messages."""

	@dbus_method(result_signature='ao')
	def list(self) -> List[str]:
		"""Retrieve all SMS messages."""
		raise NotImplementedError

	@dbus_method(input_signature='o')
	def delete(self, path: str) -> None:
		"""Delete an SMS message."""
		raise NotImplementedError

	@dbus_method(input_signature='a{sv}', result_signature='o')
	def create(self, properties: Dict[str, Tuple[str, Any]]) -> str:
		"""Creates a new message object."""
		raise NotImplementedError

	@dbus_property(property_signature='ao')
	def messages(self) -> List[str]:
		"""The list of SMS object paths."""
		raise NotImplementedError

	@dbus_property(property_signature='au')
	def supported_storages(self) -> List[int]:
		"""A list of MMSmsStorage values, specifying the storages supported by this modem for storing and receiving SMS."""
		raise NotImplementedError

	@dbus_property(property_signature='u')
	def default_storage(self) -> int:
		"""A MMSmsStorage value, specifying the storage to be used when receiving or storing SMS."""
		raise NotImplementedError


class MMModemSignalInterface(DbusInterfaceCommon, interface_name='org.freedesktop.ModemManager1.Modem.Signal'):

	@dbus_method('u')
	def setup(self, rate: int):
		"""Setup extended signal quality information retrieval.
		
		:param rate: Refresh rate to set, in seconds. 0 to disable retrieval.
		"""
		raise NotImplementedError

	@dbus_property('u')
	def rate(self) -> int:
		"""
		Refresh rate for the extended signal quality information updates, in seconds.
		A value of 0 disables the retrieval of the values.
		"""
		raise NotImplementedError

	@dbus_property('a{sv}')
	def cdma(self) -> Dict[str, Tuple[str, Any]]:
		"""
		Dictionary of available signal information for the CDMA1x access technology.
		"""
		raise NotImplementedError

	@dbus_property('a{sv}')
	def evdo(self) -> Dict[str, Tuple[str, Any]]:
		"""
		Dictionary of available signal information for the CDMA EV-DO access technology.
		"""
		raise NotImplementedError

	@dbus_property('a{sv}')
	def gsm(self) -> Dict[str, Tuple[str, Any]]:
		"""
		Dictionary of available signal information for the GSM/GPRS access technology.
		"""
		raise NotImplementedError

	@dbus_property('a{sv}')
	def umts(self) -> Dict[str, Tuple[str, Any]]:
		"""
		Dictionary of available signal information for the UMTS (WCDMA) access technology.
		"""
		raise NotImplementedError

	@dbus_property('a{sv}')
	def lte(self) -> Dict[str, Tuple[str, Any]]:
		"""
		Dictionary of available signal information for the LTE access technology.
		"""
		raise NotImplementedError

	@dbus_property('a{sv}')
	def nr5g(self) -> Dict[str, Tuple[str, Any]]:
		"""
		Dictionary of available signal information for the 5G access technology.
		"""
		raise NotImplementedError


class MMModemVoiceInterface(DbusInterfaceCommon, interface_name='org.freedesktop.ModemManager1.Modem.Voice'):

	@dbus_method(result_signature='ao')
	def list_calls(self) -> List[str]:
		"""
		Retrieve all Calls.

		:returns: The list of call object paths.
		"""
		raise NotImplementedError

	@dbus_method(input_signature='o')
	def delete_call(self, path: str) -> None:
		"""
		Delete a Call from the list of calls.
		The call will be hangup if it is still active.

		:param path: The object path of the Call to delete.
		"""
		raise NotImplementedError

	@dbus_method(input_signature='a{sv}')
	def create_call(self, properties: Dict[str, str]) -> str:
		"""
		Creates a new call object for a new outgoing call.
		The 'Number' is the only expected property to set by the user.

		:param properties: Call properties from the Call D-Bus interface.
		:returns: The object path of the new call object.
		"""
		raise NotImplementedError

	@dbus_method()
	def hold_and_accept(self) -> None:
		"""Place all active calls on hold, if any, and accept the next call."""
		raise NotImplementedError

	@dbus_method()
	def hangup_and_accept(self) -> None:
		"""Hangup all active calls, if any, and accept the next call."""
		raise NotImplementedError

	@dbus_method()
	def hangup_all(self) -> None:
		"""Hangup all active calls."""
		raise NotImplementedError

	@dbus_method()
	def transfer(self) -> None:
		"""
		Join the currently active and held calls together into a single multiparty call,
		but disconnects from them.
		"""
		raise NotImplementedError

	@dbus_method(input_signature='b')
	def call_waiting_setup(self, enable: bool) -> None:
		"""Activates or deactivates the call waiting network service, as per 3GPP TS 22.083."""
		raise NotImplementedError

	@dbus_method(result_signature='b')
	def call_waiting_query(self) -> bool:
		"""Queries the status of the call waiting network service, as per 3GPP TS 22.083."""
		raise NotImplementedError

	@dbus_property('o', property_name='Calls')
	def call_object_paths(self) -> List[str]:
		"""The list of calls object paths."""
		raise NotImplementedError

	@dbus_property('b')
	def emergency_only(self) -> bool:
		"""A flag indicating whether emergency calls are the only allowed ones."""
		raise NotImplementedError
