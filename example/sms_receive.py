import asyncio
import sdbus
from sdbus_async.modemmanager import MMModems, MMSms

async def main():
	sdbus.set_default_bus(sdbus.sd_bus_open_system())
	modem = await MMModems().get_first()
	if modem:
		async for path, received in modem.messaging.added:
			if received:
				sms = MMSms(path)
				print(f'From {await sms.number}: {await sms.text}')
	else:
		print('no modem found')

asyncio.run(main())
