from typing import Dict, List, Optional, Any

from sdbus.sd_bus_internals import SdBus

from .enums import MMCallDirection, MMCallState, MMCallStateReason, MMModemLocationSource
from .interfaces_bearer import MMBearerInterface
from .interfaces_call import MMCallInterface
from .interfaces_modem import MMModemInterface, MMModemMessagingInterface, MMModemSignalInterface, MMModemsInterface, MMModemVoiceInterface
from .interfaces_root import MMInterface
from .interfaces_sim import MMSimInterface
from .interfaces_sms import MMSmsInterface
from .interfaces_3gpp import MMModem3gppInterface
from .interfaces_simple import MMModemSimpleInterface
from .interfaces_time import MMModemTimeInterface
from .interfaces_location import MMModemLocationInterface

MODEM_MANAGER_SERVICE_NAME = 'org.freedesktop.ModemManager1'


class MM(MMInterface):
	"""Modem Manger main object

	Implements :py:class:`ModemManagerInterface`

	Service name ``'org.freedesktop.ModemManager1'``
	and object path ``/org/freedesktop/ModemManager1`` is predetermined.
	"""

	def __init__(self, bus: Optional[SdBus] = None) -> None:
		"""
		:param bus: You probably want to set default bus to system bus \
			or pass system bus directly.
		"""
		super().__init__(MODEM_MANAGER_SERVICE_NAME, '/org/freedesktop/ModemManager1', bus)


class MMSms(MMSmsInterface):

	def __init__(
		self,
		object_path: str,
		bus: Optional[SdBus] = None,
	) -> None:
		"""
		:param bus: You probably want to set default bus to system bus \
			or pass system bus directly.
		"""
		super().__init__(MODEM_MANAGER_SERVICE_NAME, object_path, bus)


class MMModemMessaging(MMModemMessagingInterface):

	def __init__(self, object_path: str, bus: Optional[SdBus] = None) -> None:
		super().__init__(MODEM_MANAGER_SERVICE_NAME, object_path, bus)

	def create_sms(self, number: str, text: str = None, data: bytes = None) -> MMSms:
		"""Creates a new message object."""
		args = {"number": ("s", number)}
		if text:
			args["text"] = ("s", text)
		elif data:
			args["data"] = ("ay", data)

		return MMSms(self.create(properties=args))

	def delete_sms(self, sms: MMSms) -> None:
		"""Delete an SMS message."""
		self.delete(sms._dbus.object_path)


class MMModemSignal(MMModemSignalInterface):

	def __init__(self, object_path: str, bus: Optional[SdBus] = None) -> None:
		"""
		:param bus: You probably want to set default bus to system bus \
			or pass system bus directly.
		"""
		super().__init__(MODEM_MANAGER_SERVICE_NAME, object_path, bus)


class MMModemSimple(MMModemSimpleInterface):

	def __init__(self, object_path: str, bus: Optional[SdBus] = None) -> None:
		super().__init__(MODEM_MANAGER_SERVICE_NAME, object_path, bus)


class MMModemVoice(MMModemVoiceInterface):

	def __init__(self, object_path: str, bus: Optional[SdBus] = None) -> None:
		super().__init__(MODEM_MANAGER_SERVICE_NAME, object_path, bus)

	def get_calls(self):
		return [MMCall(path) for path in self.call_object_paths]


class MMModem(MMModemInterface):

	def __init__(
		self,
		object_path: str,
		bus: Optional[SdBus] = None,
	) -> None:
		"""
		:param bus: You probably want to set default bus to system bus \
			or pass system bus directly.
		"""
		super().__init__(MODEM_MANAGER_SERVICE_NAME, object_path, bus)
		self.messaging = MMModemMessaging(object_path=object_path, bus=bus)
		self.location = MMModemLocation(object_path=object_path, bus=bus)
		self.simple = MMModemSimple(object_path=object_path, bus=bus)
		self.signal = MMModemSignal(object_path=object_path, bus=bus)
		self.voice = MMModemVoice(object_path=object_path, bus=bus)
		self.modem3gpp = MMModem3gpp(object_path=object_path, bus=bus)
		self.time = MMModemTime(object_path=object_path, bus=bus)
		self.sim: Optional[MMSim] = None
		self.bearers: List[MMBearer] = []

	def set_sim(self, object_path: str):
		self.sim = MMSim(object_path=object_path)

	def set_bearers(self, object_paths: List[str]):
		for p in object_paths:
			b = MMBearer(p)
			self.bearers.append(b)


class MMModems(MMModemsInterface):
	modems: List[MMModem] = []

	def __init__(self, bus: Optional[SdBus] = None) -> None:
		super().__init__(service_name=MODEM_MANAGER_SERVICE_NAME, object_path='/org/freedesktop/ModemManager1', bus=bus)

	def get_modems(self) -> List[MMModem]:
		self.modems = []
		for k, v in self.get_managed_objects().items():
			m: MMModem = MMModem(object_path=k)
			self.modems.append(m)
		return self.modems

	def get_first(self) -> Optional[MMModem]:
		if len(self.modems) <= 0:
			self.get_modems()
		return self.modems[0] if len(self.modems) >= 1 else None


class MMSim(MMSimInterface):

	def __init__(
		self,
		object_path: str,
		bus: Optional[SdBus] = None,
	) -> None:
		"""
		:param bus: You probably want to set default bus to system bus \
			or pass system bus directly.
		"""
		super().__init__(MODEM_MANAGER_SERVICE_NAME, object_path, bus)


class MMBearer(MMBearerInterface):

	def __init__(
		self,
		object_path: str,
		bus: Optional[SdBus] = None,
	) -> None:
		"""
		:param bus: You probably want to set default bus to system bus \
			or pass system bus directly.
		"""
		super().__init__(MODEM_MANAGER_SERVICE_NAME, object_path, bus)


class MMCall(MMCallInterface):

	def __init__(
		self,
		object_path: str,
		bus: Optional[SdBus] = None,
	) -> None:
		"""
		:param bus: You probably want to set default bus to system bus \
			or pass system bus directly.
		"""
		super().__init__(MODEM_MANAGER_SERVICE_NAME, object_path, bus)

	@property
	def state_text(self) -> str:
		"""A MMCallState name, describing the state of the call."""
		return MMCallState(self.state).name

	@property
	def state_reason_text(self) -> str:
		"""A MMCallStateReason name, describing why the state is changed."""
		return MMCallStateReason(self.state_reason).name

	@property
	def direction_text(self) -> str:
		"""A MMCallDirection name, describing the direction of the call."""
		return MMCallDirection(self.direction).name


class MMModem3gpp(MMModem3gppInterface):

	def __init__(self, object_path: str, bus: Optional[SdBus] = None) -> None:
		super().__init__(MODEM_MANAGER_SERVICE_NAME, object_path, bus)


class MMModemTime(MMModemTimeInterface):

	def __init__(self, object_path: str, bus: Optional[SdBus] = None) -> None:
		super().__init__(MODEM_MANAGER_SERVICE_NAME, object_path, bus)


class MMModemLocation(MMModemLocationInterface):

	def __init__(self, object_path: str, bus: Optional[SdBus] = None) -> None:
		super().__init__(MODEM_MANAGER_SERVICE_NAME, object_path, bus)

	def configure(self, sources_to_enable: list[MMModemLocationSource], enable_signaling: bool = False):
		bitmask = 0
		for src in sources_to_enable:
			bitmask |= src
		super().setup(bitmask, enable_signaling)

	@property
	def enabled_list(self) -> List[MMModemLocationSource]:
		bitmask = super().enabled
		return [src for src in MMModemLocationSource if src & bitmask]

	@property
	def capabilities_list(self) -> List[MMModemLocationSource]:
		bitmask = super().capabilities
		return [src for src in MMModemLocationSource if src & bitmask]

	@property
	def source_map(self) -> dict[MMModemLocationSource, Any]:
		"""
        Returns dictionary of parsed get_location call, where keys are MMModemLocationSource
        """

		def build_dict(raw_dict):
			new_dict: dict[str, Any] = {}
			for k, v in raw_dict.items():
				val = v
				if isinstance(v, tuple):
					val = v[1]
				new_dict[k] = build_dict(val) if isinstance(val, dict) else val
			return new_dict

		src_map: dict[MMModemLocationSource, Any] = {}
		for k, v in super().get_location().items():
			# get the enum corresponding to bit k
			key = MMModemLocationSource(k)
			value = v
			if isinstance(v, tuple):
				value = v[1]
			src_map[key] = build_dict(value) if isinstance(value, dict) else value

		return src_map
