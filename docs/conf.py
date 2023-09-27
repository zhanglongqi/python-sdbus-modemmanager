# SPDX-License-Identifier: LGPL-2.1-or-later
from os.path import abspath
from sys import path

project = 'python-sdbus-modemmanager'
author = 'zhanglongqi'
source_suffix = '.rst'
extensions = ['sdbus.autodoc']

autoclass_content = 'both'
autodoc_typehints = 'description'
autodoc_member_order = 'bysource'

path.insert(0, abspath('..'))
