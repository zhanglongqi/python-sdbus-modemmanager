from typing import Dict, List, Optional

from sdbus.sd_bus_internals import SdBus

from .enums import MMCallDirection, MMCallState, MMCallStateReason
from .interfaces_bearer import MMBearerInterface
from .interfaces_call import MMCallInterface
from .interfaces_modem import MMModemInterface, MMModemMessagingInterface, MMModemSimpleInterface, MMModemSignalInterface, MMModemsInterface, MMModemVoiceInterface
from .interfaces_root import MMInterface
from .interfaces_sim import MMSimInterface
from .interfaces_sms import MMSmsInterface

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
		self.delete(sms._remote_object_path)


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
		self.simple = MMModemSimple(object_path=object_path, bus=bus)
		self.signal = MMModemSignal(object_path=object_path, bus=bus)
		self.voice = MMModemVoice(object_path=object_path, bus=bus)
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
