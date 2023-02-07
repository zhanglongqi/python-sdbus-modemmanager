from enum import Enum, IntEnum, IntFlag


class MMModemState(IntEnum):
	
	"""Enumeration of possible modem states.
	/*< underscore_name=mm_modem_state >*/
	* MMModemState:
	* @MM_MODEM_STATE_FAILED: The modem is unusable.
	* @MM_MODEM_STATE_UNKNOWN: State unknown or not reportable.
	* @MM_MODEM_STATE_INITIALIZING: The modem is currently being initialized.
	* @MM_MODEM_STATE_LOCKED: The modem needs to be unlocked.
	* @MM_MODEM_STATE_DISABLED: The modem is not enabled and is powered down.
	* @MM_MODEM_STATE_DISABLING: The modem is currently transitioning to the @MM_MODEM_STATE_DISABLED state.
	* @MM_MODEM_STATE_ENABLING: The modem is currently transitioning to the @MM_MODEM_STATE_ENABLED state.
	* @MM_MODEM_STATE_ENABLED: The modem is enabled and powered on but not registered with a network provider and not available for data connections.
	* @MM_MODEM_STATE_SEARCHING: The modem is searching for a network provider to register with.
	* @MM_MODEM_STATE_REGISTERED: The modem is registered with a network provider, and data connections and messaging may be available for use.
	* @MM_MODEM_STATE_DISCONNECTING: The modem is disconnecting and deactivating the last active packet data bearer. This state will not be entered if more than one packet data bearer is active and one of the active bearers is deactivated.
	* @MM_MODEM_STATE_CONNECTING: The modem is activating and connecting the first packet data bearer. Subsequent bearer activations when another bearer is already active do not cause this state to be entered.
	* @MM_MODEM_STATE_CONNECTED: One or more packet data bearers is active and connected.
	*
	"""
	MM_MODEM_STATE_FAILED        = -1,
	MM_MODEM_STATE_UNKNOWN       = 0,
	MM_MODEM_STATE_INITIALIZING  = 1,
	MM_MODEM_STATE_LOCKED        = 2,
	MM_MODEM_STATE_DISABLED      = 3,
	MM_MODEM_STATE_DISABLING     = 4,
	MM_MODEM_STATE_ENABLING      = 5,
	MM_MODEM_STATE_ENABLED       = 6,
	MM_MODEM_STATE_SEARCHING     = 7,
	MM_MODEM_STATE_REGISTERED    = 8,
	MM_MODEM_STATE_DISCONNECTING = 9,
	MM_MODEM_STATE_CONNECTING    = 10,
	MM_MODEM_STATE_CONNECTED     = 11

class MMModemMode(IntEnum): 
	"""
	/*< underscore_name=mm_modem_mode >*/

	* @MM_MODEM_MODE_NONE: None.
	* @MM_MODEM_MODE_CS: CSD, GSM, and other circuit-switched technologies.
	* @MM_MODEM_MODE_2G: GPRS, EDGE.
	* @MM_MODEM_MODE_3G: UMTS, HSxPA.
	* @MM_MODEM_MODE_4G: LTE.
	* @MM_MODEM_MODE_5G: 5GNR. Since 1.14.
	* @MM_MODEM_MODE_ANY: Any mode can be used (only this value allowed for POTS modems).
	"""
	MM_MODEM_MODE_NONE = 0,
	MM_MODEM_MODE_CS   = 1 << 0,
	MM_MODEM_MODE_2G   = 1 << 1,
	MM_MODEM_MODE_3G   = 1 << 2,
	MM_MODEM_MODE_4G   = 1 << 3,
	MM_MODEM_MODE_ANY  = 0xFFFFFFFF

class MMModemPowerState(IntEnum):
	"""_summary_
	/*< underscore_name=mm_modem_power_state >*/
	Power state of the modem.

	MM_MODEM_POWER_STATE_UNKNOWN	Unknown power state.
	MM_MODEM_POWER_STATE_OFF		Off.
	MM_MODEM_POWER_STATE_LOW		Low-power mode.
	MM_MODEM_POWER_STATE_ON			Full power mode.
	Args:
		IntEnum (_type_): _description_
	"""
	MM_MODEM_POWER_STATE_UNKNOWN = 0,
	MM_MODEM_POWER_STATE_OFF     = 1,
	MM_MODEM_POWER_STATE_LOW     = 2,
	MM_MODEM_POWER_STATE_ON      = 3
