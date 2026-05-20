from sdbus_async import modemmanager as async_modemmanager
from sdbus_block import modemmanager as block_modemmanager


def test_async_public_imports():
	assert async_modemmanager.MM is not None
	assert async_modemmanager.MMModems is not None
	assert async_modemmanager.MMBearer is not None
	assert 'MM' in async_modemmanager.__all__
	assert 'MMModems' in async_modemmanager.__all__
	assert 'MMBearer' in async_modemmanager.__all__


def test_blocking_public_imports():
	assert block_modemmanager.MM is not None
	assert block_modemmanager.MMModems is not None
	assert block_modemmanager.MMBearer is not None
	assert 'MM' in block_modemmanager.__all__
	assert 'MMModems' in block_modemmanager.__all__
	assert 'MMBearer' in block_modemmanager.__all__
