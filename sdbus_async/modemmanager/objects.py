from typing import Dict, List, Optional

from sdbus.sd_bus_internals import SdBus

from .enums import MMCallDirection, MMCallState, MMCallStateReason
from .interfaces_bearer import MMBearerInterfaceAsync
from .interfaces_call import MMCallInterfaceAsync
from .interfaces_modem import MMModemInterfaceAsync, MMModemMessagingInterfaceAsync, MMModemSimpleInterfaceAsync, MMModemSignalInterfaceAsync, MMModemsInterfaceAsync, MMModemVoiceInterfaceAsync
from .interfaces_root import MMInterfaceAsync
from .interfaces_sim import MMSimInterfaceAsync
from .interfaces_sms import MMSmsInterfaceAsync

MODEM_MANAGER_SERVICE_NAME = 'org.freedesktop.ModemManager1'


class MM(MMInterfaceAsync):
	"""Modem Manger main object

	Implements :py:class:`ModemManagerInterfaceAsync`

	Service name ``'org.freedesktop.ModemManager1'``
	and object path ``/org/freedesktop/ModemManager1`` is predetermined.
	"""

	def __init__(self, bus: Optional[SdBus] = None) -> None:
		"""
		:param bus: You probably want to set default bus to system bus \
			or pass system bus directly.
		"""
		super().__init__()
		self._connect(MODEM_MANAGER_SERVICE_NAME, '/org/freedesktop/ModemManager1', bus)


class MMSms(MMSmsInterfaceAsync):

	def __init__(
		self,
		object_path: str,
		bus: Optional[SdBus] = None,
	) -> None:
		"""
		:param bus: You probably want to set default bus to system bus \
			or pass system bus directly.
		"""
		super().__init__()
		self._connect(MODEM_MANAGER_SERVICE_NAME, object_path, bus)


class MMModemMessaging(MMModemMessagingInterfaceAsync):

	def __init__(self, object_path: str, bus: Optional[SdBus] = None) -> None:
		super().__init__()
		self._connect(MODEM_MANAGER_SERVICE_NAME, object_path, bus)

	async def create_sms(self, number: str, text: str = None, data: bytes = None) -> MMSms:
		"""Creates a new message object."""
		args = {"number": ("s", number)}
		if text:
			args["text"] = ("s", text)
		elif data:
			args["data"] = ("ay", data)

		return MMSms(self.create(properties=args))

	async def delete_sms(self, sms: MMSms) -> None:
		"""Delete an SMS message."""
		self.delete(sms._dbus.object_path)


class MMModemSignal(MMModemSignalInterfaceAsync):

	def __init__(self, object_path: str, bus: Optional[SdBus] = None) -> None:
		"""
		:param bus: You probably want to set default bus to system bus \
			or pass system bus directly.
		"""
		super().__init__()
		self._connect(MODEM_MANAGER_SERVICE_NAME, object_path, bus)


class MMModemSimple(MMModemSimpleInterfaceAsync):

	def __init__(self, object_path: str, bus: Optional[SdBus] = None) -> None:
		super().__init__()
		self._connect(MODEM_MANAGER_SERVICE_NAME, object_path, bus)


class MMModemVoice(MMModemVoiceInterfaceAsync):

	def __init__(self, object_path: str, bus: Optional[SdBus] = None) -> None:
		super().__init__()
		self._connect(MODEM_MANAGER_SERVICE_NAME, object_path, bus)

	async def get_calls(self):
		return [MMCall(path) for path in self.call_object_paths]


class MMModem(MMModemInterfaceAsync):

	def __init__(
		self,
		object_path: str,
		bus: Optional[SdBus] = None,
	) -> None:
		"""
		:param bus: You probably want to set default bus to system bus \
			or pass system bus directly.
		"""
		super().__init__()
		self._connect(MODEM_MANAGER_SERVICE_NAME, object_path, bus)
		self.messaging = MMModemMessaging(object_path=object_path, bus=bus)
		self.simple = MMModemSimple(object_path=object_path, bus=bus)
		self.signal = MMModemSignal(object_path=object_path, bus=bus)
		self.voice = MMModemVoice(object_path=object_path, bus=bus)
		self.sim: Optional[MMSim] = None
		self.bearers: List[MMBearer] = []

	async def set_sim(self, object_path: str):
		self.sim = MMSim(object_path=object_path)

	async def set_bearers(self, object_paths: List[str]):
		for p in object_paths:
			b = MMBearer(p)
			self.bearers.append(b)


class MMModems(MMModemsInterfaceAsync):
	modems: List[MMModem] = []

	def __init__(self, bus: Optional[SdBus] = None) -> None:
		super().__init__()
		self._connect(service_name=MODEM_MANAGER_SERVICE_NAME, object_path='/org/freedesktop/ModemManager1', bus=bus)

	async def get_modems(self) -> List[MMModem]:
		objects = await self.get_managed_objects()
		for k, v in objects.items():
			m: MMModem = MMModem(object_path=k)
			self.modems.append(m)
		return self.modems

	async def get_first(self) -> Optional[MMModem]:
		if len(self.modems) <= 0:
			await self.get_modems()
		return self.modems[0] if len(self.modems) >= 1 else None


class MMSim(MMSimInterfaceAsync):

	def __init__(
		self,
		object_path: str,
		bus: Optional[SdBus] = None,
	) -> None:
		"""
		:param bus: You probably want to set default bus to system bus \
			or pass system bus directly.
		"""
		super().__init__()
		self._connect(MODEM_MANAGER_SERVICE_NAME, object_path, bus)


class MMBearer(MMBearerInterfaceAsync):

	def __init__(
		self,
		object_path: str,
		bus: Optional[SdBus] = None,
	) -> None:
		"""
		:param bus: You probably want to set default bus to system bus \
			or pass system bus directly.
		"""
		super().__init__()
		self._connect(MODEM_MANAGER_SERVICE_NAME, object_path, bus)


class MMCall(MMCallInterfaceAsync):

	def __init__(
		self,
		object_path: str,
		bus: Optional[SdBus] = None,
	) -> None:
		"""
		:param bus: You probably want to set default bus to system bus \
			or pass system bus directly.
		"""
		super().__init__()
		self._connect(MODEM_MANAGER_SERVICE_NAME, object_path, bus)

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
