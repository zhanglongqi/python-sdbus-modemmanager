from enum import Enum, IntEnum, IntFlag


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
	MM_MODEM_STATE_FAILED = -1,
	MM_MODEM_STATE_UNKNOWN = 0,
	MM_MODEM_STATE_INITIALIZING = 1,
	MM_MODEM_STATE_LOCKED = 2,
	MM_MODEM_STATE_DISABLED = 3,
	MM_MODEM_STATE_DISABLING = 4,
	MM_MODEM_STATE_ENABLING = 5,
	MM_MODEM_STATE_ENABLED = 6,
	MM_MODEM_STATE_SEARCHING = 7,
	MM_MODEM_STATE_REGISTERED = 8,
	MM_MODEM_STATE_DISCONNECTING = 9,
	MM_MODEM_STATE_CONNECTING = 10,
	MM_MODEM_STATE_CONNECTED = 11


class MMModemMode(IntEnum):
	"""Bitfield to indicate which access modes are supported, allowed or preferred in a given device.

	* MM_MODEM_MODE_NONE: None.
	* MM_MODEM_MODE_CS: CSD, GSM, and other circuit-switched technologies.
	* MM_MODEM_MODE_2G: GPRS, EDGE.
	* MM_MODEM_MODE_3G: UMTS, HSxPA.
	* MM_MODEM_MODE_4G: LTE.
	* MM_MODEM_MODE_5G: 5GNR. Since 1.14.
	* MM_MODEM_MODE_ANY: Any mode can be used (only this value allowed for POTS modems).
	"""
	MM_MODEM_MODE_NONE = 0,
	MM_MODEM_MODE_CS = 1 << 0,
	MM_MODEM_MODE_2G = 1 << 1,
	MM_MODEM_MODE_3G = 1 << 2,
	MM_MODEM_MODE_4G = 1 << 3,
	MM_MODEM_MODE_ANY = 0xFFFFFFFF


class MMModemPowerState(IntEnum):
	"""Power state of the modem.

	* MM_MODEM_POWER_STATE_UNKNOWN		Unknown power state.
	* MM_MODEM_POWER_STATE_OFF		Off.
	* MM_MODEM_POWER_STATE_LOW		Low-power mode.
	* MM_MODEM_POWER_STATE_ON		Full power mode.
	"""
	MM_MODEM_POWER_STATE_UNKNOWN = 0,
	MM_MODEM_POWER_STATE_OFF = 1,
	MM_MODEM_POWER_STATE_LOW = 2,
	MM_MODEM_POWER_STATE_ON = 3


class MMCallDirection(IntEnum):
	"""Direction of the call.

	* MM_CALL_DIRECTION_UNKNOWN	Unknown.
	* MM_CALL_DIRECTION_INCOMING	Call from network.
	* MM_CALL_DIRECTION_OUTGOING	Call to network.
	"""
	MM_CALL_DIRECTION_UNKNOWN = 0,
	MM_CALL_DIRECTION_INCOMING = 1,
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
	MM_CALL_STATE_UNKNOWN = 0,
	MM_CALL_STATE_DIALING = 1,
	MM_CALL_STATE_RINGING_OUT = 2,
	MM_CALL_STATE_RINGING_IN = 3,
	MM_CALL_STATE_ACTIVE = 4,
	MM_CALL_STATE_HELD = 5,
	MM_CALL_STATE_WAITING = 6,
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
	MM_CALL_STATE_REASON_UNKNOWN = 0,
	MM_CALL_STATE_REASON_OUTGOING_STARTED = 1,
	MM_CALL_STATE_REASON_INCOMING_NEW = 2,
	MM_CALL_STATE_REASON_ACCEPTED = 3,
	MM_CALL_STATE_REASON_TERMINATED = 4,
	MM_CALL_STATE_REASON_REFUSED_OR_BUSY = 5,
	MM_CALL_STATE_REASON_ERROR = 6,
	MM_CALL_STATE_REASON_AUDIO_SETUP_FAILED = 7,
	MM_CALL_STATE_REASON_TRANSFERRED = 8,
	MM_CALL_STATE_REASON_DEFLECTED = 9
