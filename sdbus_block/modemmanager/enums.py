from enum import IntEnum, IntFlag


class MMModemState(IntEnum):
	"""Enumeration of possible modem states.

	* MM_MODEM_STATE_FAILED: The modem is unusable.
	* MM_MODEM_STATE_UNKNOWN: State unknown or not reportable.
	* MM_MODEM_STATE_INITIALIZING: The modem is currently being initialized.
	* MM_MODEM_STATE_LOCKED: The modem needs to be unlocked.
	* MM_MODEM_STATE_DISABLED: The modem is not enabled and is powered down.
	* MM_MODEM_STATE_DISABLING: The modem is currently transitioning to the MM_MODEM_STATE_DISABLED state.
	* MM_MODEM_STATE_ENABLING: The modem is currently transitioning to the MM_MODEM_STATE_ENABLED state.
	* MM_MODEM_STATE_ENABLED: The modem is enabled and powered on but not registered with a network provider and not available for data connections.
	* MM_MODEM_STATE_SEARCHING: The modem is searching for a network provider to register with.
	* MM_MODEM_STATE_REGISTERED: The modem is registered with a network provider, and data connections and messaging may be available for use.
	* MM_MODEM_STATE_DISCONNECTING: The modem is disconnecting and deactivating the last active packet data bearer. This state will not be entered if more than one packet data bearer is active and one of the active bearers is deactivated.
	* MM_MODEM_STATE_CONNECTING: The modem is activating and connecting the first packet data bearer. Subsequent bearer activations when another bearer is already active do not cause this state to be entered.
	* MM_MODEM_STATE_CONNECTED: One or more packet data bearers is active and connected.
	"""
	MM_MODEM_STATE_FAILED = -1
	MM_MODEM_STATE_UNKNOWN = 0
	MM_MODEM_STATE_INITIALIZING = 1
	MM_MODEM_STATE_LOCKED = 2
	MM_MODEM_STATE_DISABLED = 3
	MM_MODEM_STATE_DISABLING = 4
	MM_MODEM_STATE_ENABLING = 5
	MM_MODEM_STATE_ENABLED = 6
	MM_MODEM_STATE_SEARCHING = 7
	MM_MODEM_STATE_REGISTERED = 8
	MM_MODEM_STATE_DISCONNECTING = 9
	MM_MODEM_STATE_CONNECTING = 10
	MM_MODEM_STATE_CONNECTED = 11


class MMModemStateFailedReason(IntEnum):
	"""
	Enumeration of possible errors when the modem is in @MM_MODEM_STATE_FAILED

	* @MM_MODEM_STATE_FAILED_REASON_NONE: No error.
	* @MM_MODEM_STATE_FAILED_REASON_UNKNOWN: Unknown error.
	* @MM_MODEM_STATE_FAILED_REASON_SIM_MISSING: SIM is required but missing.
	* @MM_MODEM_STATE_FAILED_REASON_SIM_ERROR: SIM is available, but unusable (e.g. permanently locked).
	* @MM_MODEM_STATE_FAILED_REASON_UNKNOWN_CAPABILITIES: Unknown modem capabilities. Since 1.20.
	* @MM_MODEM_STATE_FAILED_REASON_ESIM_WITHOUT_PROFILES: eSIM is not initialized. Since 1.20.
	"""
	MM_MODEM_STATE_FAILED_REASON_NONE = 0
	MM_MODEM_STATE_FAILED_REASON_UNKNOWN = 1
	MM_MODEM_STATE_FAILED_REASON_SIM_MISSING = 2
	MM_MODEM_STATE_FAILED_REASON_SIM_ERROR = 3
	MM_MODEM_STATE_FAILED_REASON_UNKNOWN_CAPABILITIES = 4
	MM_MODEM_STATE_FAILED_REASON_ESIM_WITHOUT_PROFILES = 5


class MMModemMode(IntFlag):
	"""Bitfield to indicate which access modes are supported, allowed or preferred in a given device.

	* MM_MODEM_MODE_NONE: None.
	* MM_MODEM_MODE_CS: CSD, GSM, and other circuit-switched technologies.
	* MM_MODEM_MODE_2G: GPRS, EDGE.
	* MM_MODEM_MODE_3G: UMTS, HSxPA.
	* MM_MODEM_MODE_4G: LTE.
	* MM_MODEM_MODE_5G: 5GNR. Since 1.14.
	* MM_MODEM_MODE_ANY: Any mode can be used (only this value allowed for POTS modems).
	"""
	MM_MODEM_MODE_NONE = 0
	MM_MODEM_MODE_CS = 1 << 0
	MM_MODEM_MODE_2G = 1 << 1
	MM_MODEM_MODE_3G = 1 << 2
	MM_MODEM_MODE_4G = 1 << 3
	MM_MODEM_MODE_ANY = 0xFFFFFFFF


class MMModemAccessTechnology(IntFlag):
	"""
	Describes various access technologies that a device uses when registered with or connected to a network.

	* @MM_MODEM_ACCESS_TECHNOLOGY_UNKNOWN: The access technology used is unknown.
	* @MM_MODEM_ACCESS_TECHNOLOGY_POTS: Analog wireline telephone.
	* @MM_MODEM_ACCESS_TECHNOLOGY_GSM: GSM.
	* @MM_MODEM_ACCESS_TECHNOLOGY_GSM_COMPACT: Compact GSM.
	* @MM_MODEM_ACCESS_TECHNOLOGY_GPRS: GPRS.
	* @MM_MODEM_ACCESS_TECHNOLOGY_EDGE: EDGE (ETSI 27.007: "GSM w/EGPRS").
	* @MM_MODEM_ACCESS_TECHNOLOGY_UMTS: UMTS (ETSI 27.007: "UTRAN").
	* @MM_MODEM_ACCESS_TECHNOLOGY_HSDPA: HSDPA (ETSI 27.007: "UTRAN w/HSDPA").
	* @MM_MODEM_ACCESS_TECHNOLOGY_HSUPA: HSUPA (ETSI 27.007: "UTRAN w/HSUPA").
	* @MM_MODEM_ACCESS_TECHNOLOGY_HSPA: HSPA (ETSI 27.007: "UTRAN w/HSDPA and HSUPA").
	* @MM_MODEM_ACCESS_TECHNOLOGY_HSPA_PLUS: HSPA+ (ETSI 27.007: "UTRAN w/HSPA+").
	* @MM_MODEM_ACCESS_TECHNOLOGY_1XRTT: CDMA2000 1xRTT.
	* @MM_MODEM_ACCESS_TECHNOLOGY_EVDO0: CDMA2000 EVDO revision 0.
	* @MM_MODEM_ACCESS_TECHNOLOGY_EVDOA: CDMA2000 EVDO revision A.
	* @MM_MODEM_ACCESS_TECHNOLOGY_EVDOB: CDMA2000 EVDO revision B.
	* @MM_MODEM_ACCESS_TECHNOLOGY_LTE: LTE (ETSI 27.007: "E-UTRAN")
	* @MM_MODEM_ACCESS_TECHNOLOGY_5GNR: 5GNR (ETSI 27.007: "NG-RAN"). Since 1.14.
	* @MM_MODEM_ACCESS_TECHNOLOGY_LTE_CAT_M: Cat-M (ETSI 23.401: LTE Category M1/M2). Since 1.20.
	* @MM_MODEM_ACCESS_TECHNOLOGY_LTE_NB_IOT: NB IoT (ETSI 23.401: LTE Category NB1/NB2). Since 1.20.
	* @MM_MODEM_ACCESS_TECHNOLOGY_ANY: Mask specifying all access technologies.
	"""
	MM_MODEM_ACCESS_TECHNOLOGY_UNKNOWN = 0
	MM_MODEM_ACCESS_TECHNOLOGY_POTS = 1 << 0
	MM_MODEM_ACCESS_TECHNOLOGY_GSM = 1 << 1
	MM_MODEM_ACCESS_TECHNOLOGY_GSM_COMPACT = 1 << 2
	MM_MODEM_ACCESS_TECHNOLOGY_GPRS = 1 << 3
	MM_MODEM_ACCESS_TECHNOLOGY_EDGE = 1 << 4
	MM_MODEM_ACCESS_TECHNOLOGY_UMTS = 1 << 5
	MM_MODEM_ACCESS_TECHNOLOGY_HSDPA = 1 << 6
	MM_MODEM_ACCESS_TECHNOLOGY_HSUPA = 1 << 7
	MM_MODEM_ACCESS_TECHNOLOGY_HSPA = 1 << 8
	MM_MODEM_ACCESS_TECHNOLOGY_HSPA_PLUS = 1 << 9
	MM_MODEM_ACCESS_TECHNOLOGY_1XRTT = 1 << 10
	MM_MODEM_ACCESS_TECHNOLOGY_EVDO0 = 1 << 11
	MM_MODEM_ACCESS_TECHNOLOGY_EVDOA = 1 << 12
	MM_MODEM_ACCESS_TECHNOLOGY_EVDOB = 1 << 13
	MM_MODEM_ACCESS_TECHNOLOGY_LTE = 1 << 14
	MM_MODEM_ACCESS_TECHNOLOGY_5GNR = 1 << 15
	MM_MODEM_ACCESS_TECHNOLOGY_LTE_CAT_M = 1 << 16
	MM_MODEM_ACCESS_TECHNOLOGY_LTE_NB_IOT = 1 << 17
	MM_MODEM_ACCESS_TECHNOLOGY_ANY = 0xFFFFFFFF


class MMModem3gppRegistrationState(IntEnum):
	"""
	GSM registration code as defined in 3GPP TS 27.007.

	* MMModem3gppRegistrationState:
	* @MM_MODEM_3GPP_REGISTRATION_STATE_IDLE: Not registered, not searching for new operator to register.
	* @MM_MODEM_3GPP_REGISTRATION_STATE_HOME: Registered on home network.
	* @MM_MODEM_3GPP_REGISTRATION_STATE_SEARCHING: Not registered, searching for new operator to register with.
	* @MM_MODEM_3GPP_REGISTRATION_STATE_DENIED: Registration denied.
	* @MM_MODEM_3GPP_REGISTRATION_STATE_UNKNOWN: Unknown registration status.
	* @MM_MODEM_3GPP_REGISTRATION_STATE_ROAMING: Registered on a roaming network.
	* @MM_MODEM_3GPP_REGISTRATION_STATE_HOME_SMS_ONLY: Registered for "SMS only", home network (applicable only when on LTE). Since 1.8.
	* @MM_MODEM_3GPP_REGISTRATION_STATE_ROAMING_SMS_ONLY: Registered for "SMS only", roaming network (applicable only when on LTE). Since 1.8.
	* @MM_MODEM_3GPP_REGISTRATION_STATE_EMERGENCY_ONLY: Emergency services only. Since 1.8.
	* @MM_MODEM_3GPP_REGISTRATION_STATE_HOME_CSFB_NOT_PREFERRED: Registered for "CSFB not preferred", home network (applicable only when on LTE). Since 1.8.
	* @MM_MODEM_3GPP_REGISTRATION_STATE_ROAMING_CSFB_NOT_PREFERRED: Registered for "CSFB not preferred", roaming network (applicable only when on LTE). Since 1.8.
	* @MM_MODEM_3GPP_REGISTRATION_STATE_ATTACHED_RLOS: Attached for access to Restricted Local Operator Services (applicable only when on LTE). Since 1.14.
	"""
	MM_MODEM_3GPP_REGISTRATION_STATE_IDLE = 0
	MM_MODEM_3GPP_REGISTRATION_STATE_HOME = 1
	MM_MODEM_3GPP_REGISTRATION_STATE_SEARCHING = 2
	MM_MODEM_3GPP_REGISTRATION_STATE_DENIED = 3
	MM_MODEM_3GPP_REGISTRATION_STATE_UNKNOWN = 4
	MM_MODEM_3GPP_REGISTRATION_STATE_ROAMING = 5
	MM_MODEM_3GPP_REGISTRATION_STATE_HOME_SMS_ONLY = 6
	MM_MODEM_3GPP_REGISTRATION_STATE_ROAMING_SMS_ONLY = 7
	MM_MODEM_3GPP_REGISTRATION_STATE_EMERGENCY_ONLY = 8
	MM_MODEM_3GPP_REGISTRATION_STATE_HOME_CSFB_NOT_PREFERRED = 9
	MM_MODEM_3GPP_REGISTRATION_STATE_ROAMING_CSFB_NOT_PREFERRED = 10
	MM_MODEM_3GPP_REGISTRATION_STATE_ATTACHED_RLOS = 11


class MMModemPowerState(IntEnum):
	"""Power state of the modem.

	* MM_MODEM_POWER_STATE_UNKNOWN		Unknown power state.
	* MM_MODEM_POWER_STATE_OFF		Off.
	* MM_MODEM_POWER_STATE_LOW		Low-power mode.
	* MM_MODEM_POWER_STATE_ON		Full power mode.
	"""
	MM_MODEM_POWER_STATE_UNKNOWN = 0
	MM_MODEM_POWER_STATE_OFF = 1
	MM_MODEM_POWER_STATE_LOW = 2
	MM_MODEM_POWER_STATE_ON = 3


class MMCallDirection(IntEnum):
	"""Direction of the call.

	* MM_CALL_DIRECTION_UNKNOWN	Unknown.
	* MM_CALL_DIRECTION_INCOMING	Call from network.
	* MM_CALL_DIRECTION_OUTGOING	Call to network.
	"""
	MM_CALL_DIRECTION_UNKNOWN = 0
	MM_CALL_DIRECTION_INCOMING = 1
	MM_CALL_DIRECTION_OUTGOING = 2


class MMCallState(IntEnum):
	"""State of Call.

	* MM_CALL_STATE_UNKNOWN			Default state for a new outgoing call.
	* MM_CALL_STATE_DIALING			Outgoing call started. Wait for free channel.
	* MM_CALL_STATE_RINGING_OUT		Outgoing call attached to GSM network, waiting for an answer.
	* MM_CALL_STATE_RINGING_IN		Incoming call is waiting for an answer.
	* MM_CALL_STATE_ACTIVE			Call is active between two peers.
	* MM_CALL_STATE_HELD			Held call (by +CHLD AT command).
	* MM_CALL_STATE_WAITING			Waiting call (by +CCWA AT command).
	* MM_CALL_STATE_TERMINATED		Call is terminated.
	"""
	MM_CALL_STATE_UNKNOWN = 0
	MM_CALL_STATE_DIALING = 1
	MM_CALL_STATE_RINGING_OUT = 2
	MM_CALL_STATE_RINGING_IN = 3
	MM_CALL_STATE_ACTIVE = 4
	MM_CALL_STATE_HELD = 5
	MM_CALL_STATE_WAITING = 6
	MM_CALL_STATE_TERMINATED = 7


class MMCallStateReason(IntEnum):
	"""Reason for the state change in the call.

	* MM_CALL_STATE_REASON_UNKNOWN		Default value for a new outgoing call.
	* MM_CALL_STATE_REASON_OUTGOING_STARTED	Outgoing call is started.
	* MM_CALL_STATE_REASON_INCOMING_NEW	Received a new incoming call.
	* MM_CALL_STATE_REASON_ACCEPTED		Dialing or Ringing call is accepted.
	* MM_CALL_STATE_REASON_TERMINATED	Call is correctly terminated.
	* MM_CALL_STATE_REASON_REFUSED_OR_BUSY	Remote peer is busy or refused call.
	* MM_CALL_STATE_REASON_ERROR		Wrong number or generic network error.
	* MM_CALL_STATE_REASON_AUDIO_SETUP_FAILED	Error setting up audio channel. Since 1.10.
	* MM_CALL_STATE_REASON_TRANSFERRED	Call has been transferred. Since 1.12.
	* MM_CALL_STATE_REASON_DEFLECTED	Call has been deflected to a new number. Since 1.12.
	"""
	MM_CALL_STATE_REASON_UNKNOWN = 0
	MM_CALL_STATE_REASON_OUTGOING_STARTED = 1
	MM_CALL_STATE_REASON_INCOMING_NEW = 2
	MM_CALL_STATE_REASON_ACCEPTED = 3
	MM_CALL_STATE_REASON_TERMINATED = 4
	MM_CALL_STATE_REASON_REFUSED_OR_BUSY = 5
	MM_CALL_STATE_REASON_ERROR = 6
	MM_CALL_STATE_REASON_AUDIO_SETUP_FAILED = 7
	MM_CALL_STATE_REASON_TRANSFERRED = 8
	MM_CALL_STATE_REASON_DEFLECTED = 9


class MMModemCapability(IntEnum):
	MM_MODEM_CAPABILITY_NONE = 0
	MM_MODEM_CAPABILITY_POTS = 1 << 0
	MM_MODEM_CAPABILITY_CDMA_EVDO = 1 << 1
	MM_MODEM_CAPABILITY_GSM_UMTS = 1 << 2
	MM_MODEM_CAPABILITY_LTE = 1 << 3
	MM_MODEM_CAPABILITY_IRIDIUM = 1 << 5
	MM_MODEM_CAPABILITY_5GNR = 1 << 6
	MM_MODEM_CAPABILITY_TDS = 1 << 7
	MM_MODEM_CAPABILITY_ANY = 0xFFFFFFFF

	@staticmethod
	def names(value) -> list:
		names = []
		if MMModemCapability.MM_MODEM_CAPABILITY_ANY != value:
			for capability in MMModemCapability:
				if capability & value and capability != MMModemCapability.MM_MODEM_CAPABILITY_ANY:
					names.append(capability.name)
		else:
			names.append(MMModemCapability.MM_MODEM_CAPABILITY_ANY.name)
		return names


class MMModemLocationSource(IntEnum):
	"""Sources of location information supported by the modem.
   	* MM_MODEM_LOCATION_SOURCE_NONE 			None.
	* MM_MODEM_LOCATION_SOURCE_3GPP_LAC_CI 		Location Area Code and Cell ID.
	* MM_MODEM_LOCATION_SOURCE_GPS_RAW 			GPS location given by predefined keys.
	* MM_MODEM_LOCATION_SOURCE_GPS_NMEA 		GPS location given as NMEA traces.
	* MM_MODEM_LOCATION_SOURCE_CDMA_BS 			CDMA base station position.
	* MM_MODEM_LOCATION_SOURCE_GPS_UNMANAGED 	No location given, just GPS module setup. Since 1.4.
	* MM_MODEM_LOCATION_SOURCE_AGPS_MSA 		Mobile Station Assisted A-GPS location requested. 
												In MSA A-GPS, the position fix is computed by a server online.
												The modem must have a valid SIM card inserted and be enabled 
												for this mode to be allowed. Since 1.12.
	* MM_MODEM_LOCATION_SOURCE_AGPS_MSB 		Mobile Station Based A-GPS location requested. 
												In MSB A-GPS, the position fix is computed by the modem, 
												but it first gathers information from an online server to 
												facilitate the process (e.g. ephemeris).
												The modem must have a valid SIM card inserted and be enabled 
												for this mode to be allowed. Since 1.12. 
	"""
	MM_MODEM_LOCATION_SOURCE_NONE = 0
	MM_MODEM_LOCATION_SOURCE_3GPP_LAC_CI = 1 << 0
	MM_MODEM_LOCATION_SOURCE_GPS_RAW = 1 << 1
	MM_MODEM_LOCATION_SOURCE_GPS_NMEA = 1 << 2
	MM_MODEM_LOCATION_SOURCE_CDMA_BS = 1 << 3
	MM_MODEM_LOCATION_SOURCE_GPS_UNMANAGED = 1 << 4
	MM_MODEM_LOCATION_SOURCE_AGPS_MSA = 1 << 5
	MM_MODEM_LOCATION_SOURCE_AGPS_MSB = 1 << 6


class MMModemLocationAssistanceDataType(IntEnum):
	"""Type of assistance data that may be injected to the GNSS module.
    * MM_MODEM_LOCATION_ASSISTANCE_DATA_TYPE_NONE   None.
    * MM_MODEM_LOCATION_ASSISTANCE_DATA_TYPE_XTRA   Qualcomm gpsOneXTRA.
    """
	MM_MODEM_LOCATION_ASSISTANCE_DATA_TYPE_NONE = 0
	MM_MODEM_LOCATION_ASSISTANCE_DATA_TYPE_XTRA = 1 << 0
