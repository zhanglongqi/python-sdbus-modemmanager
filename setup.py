from setuptools import setup

setup(
	name='sdbus-modemmanager',
	description=('ModemManager binds for sdbus.'),
	long_description=open('README.md').read(),
	long_description_content_type='text/markdown',
	version='1.0.1',
	url='https://github.com/zhanglongqi/python-sdbus-modemmanager',
	project_urls={
		'Source': 'https://github.com/zhanglongqi/python-sdbus-modemmanager/',
		'Tracker': 'https://github.com/zhanglongqi/python-sdbus-modemmanager/issues/',
	},
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		('License :: OSI Approved :: '
			'GNU Lesser General Public License v2 or later (LGPLv2+)'),
		'Operating System :: POSIX :: Linux',
		'Programming Language :: Python :: 3 :: Only',
		'Topic :: Software Development :: Libraries :: Python Modules',
	],
	license='LGPL-2.1-or-later',
	packages=['sdbus_async.modemmanager', 'sdbus_block.modemmanager'],
	package_data={
		'sdbus_async.modemmanager': [
			'py.typed'
		],
		'sdbus_block.modemmanager': [
			'py.typed'
		],
	},
	python_requires='>=3.7',
	install_requires=[
		'sdbus>=0.8rc2',
	],
)
