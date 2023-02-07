from re import M
from typing import List, Optional, Dict
from sdbus.sd_bus_internals import SdBus
from interfaces_root import MMInterface
from interfaces_modem import MMModemInterface, MMModemSimpleInterface, MMModemsInterface, MMModemSingalInterface
from interfaces_sim import MMSimInterface
from sdbus_block.modemmanager.interfaces_bearer import MMBearerInterface

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


class MMModemSignal(MMModemSingalInterface):

	def __init__(self, object_path: str, bus: Optional[SdBus] = None) -> None:
		"""
        :param bus: You probably want to set default bus to system bus \
            or pass system bus directly.
        """
		super().__init__(MODEM_MANAGER_SERVICE_NAME, object_path, bus)


class MMModemSimple(MMModemSimpleInterface):

	def __init__(self, object_path: str, bus: Optional[SdBus] = None) -> None:
		super().__init__(MODEM_MANAGER_SERVICE_NAME, object_path, bus)


class MMModem(MMModemInterface):

	def __init__(self,
					object_path: str,
					bus: Optional[SdBus] = None,
					simple_object_path: str = 'org.freedesktop.ModemManager1.Modem.Simple',
					signal_object_path: str = 'org.freedesktop.ModemManager1.Modem.Signal') -> None:
		"""
        :param bus: You probably want to set default bus to system bus \
            or pass system bus directly.
        """
		super().__init__(MODEM_MANAGER_SERVICE_NAME, object_path, bus)
		self.simple = MMModemSimple(object_path=simple_object_path)
		self.signal = MMModemSignal(object_path=signal_object_path)
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


if __name__ == "__main__":
	import sdbus

	sdbus.set_default_bus(sdbus.sd_bus_open_system())
	mm = MM()
	print(f'{mm.version=}')

	mms = MMModems()
	modem = mms.get_first()
	if modem:
		print(f'{modem.state_text=}, {modem.imei=}, {modem.manufacturer=}, {modem.model=}, {modem.hardware_revision=}, '
				f'{modem.own_numbers=}, {modem.power_state_text=}, {modem.signal_quality=}')

		if modem.sim_object_path is not None:
			modem.set_sim(modem.sim_object_path)
			if modem.sim:
				print(f'{modem.sim.imsi=}, {modem.sim.sim_identifier=}, {modem.sim.operator_name=}, '
						f'{modem.sim.operator_identifier=}')
			else:
				print(f'failed to get sim object {modem.sim_object_path=}')
		else:
			print('no sim card found')
		if len(modem.bearer_object_paths) > 0:
			modem.set_bearers(modem.bearer_object_paths)
			for b in modem.bearers:
				print(f'{b.connected=}')
		else:
			print('no bearer found')
	else:
		print('no modem found')