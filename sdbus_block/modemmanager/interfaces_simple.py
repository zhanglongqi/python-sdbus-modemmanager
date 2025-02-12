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


class MMModemSimpleInterface(
	DbusInterfaceCommon,
	interface_name="org.freedesktop.ModemManager1.Modem.Simple",
):
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

	:param properties: Dictionary of properties needed to get the modem connected. ex: {"apn": ("s", "yourAPN.isp"), "ip-type": ("s", "ipv4v6")}
	:returns: On successful connect, returns the object path of the connected packet data bearer used for the connection attempt.
	"""
	@dbus_method(
		input_signature="a{sv}",
		result_signature="o",
		flags=DbusUnprivilegedFlag,
	)
	def connect(
		self,
		properties: Dict[str, Tuple[str, Any]],
	) -> str:
		raise NotImplementedError

		"""
		data bearer, while if "/" (ie, no object given) this method will disconnect all active packet data bearers.
		Disconnect an active packet data connection.
		:param bearer: If given this method will disconnect the referenced packet
		"""
	@dbus_method(
		input_signature="o",
		flags=DbusUnprivilegedFlag,
	)
	def disconnect(
		self,
		bearer: str,
	) -> None:
		raise NotImplementedError

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
	@dbus_method(
		result_signature="a{sv}",
		flags=DbusUnprivilegedFlag,
	)
	def get_status(
		self,
	) -> Dict[str, Tuple[str, Any]]:
		raise NotImplementedError
