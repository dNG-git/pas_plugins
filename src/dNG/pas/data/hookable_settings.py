# -*- coding: utf-8 -*-
##j## BOF

"""
direct PAS
Python Application Services
----------------------------------------------------------------------------
(C) direct Netware Group - All rights reserved
http://www.direct-netware.de/redirect.py?pas;plugins

This Source Code Form is subject to the terms of the Mozilla Public License,
v. 2.0. If a copy of the MPL was not distributed with this file, You can
obtain one at http://mozilla.org/MPL/2.0/.
----------------------------------------------------------------------------
http://www.direct-netware.de/redirect.py?licenses;mpl2
----------------------------------------------------------------------------
#echo(pasPluginsVersion)#
#echo(__FILEPATH__)#
"""

from dNG.pas.plugins.hook import Hook
from .settings import Settings

class HookableSettings(object):
#
	"""
"HookableSettings" provide a hook based solution to set custom values for
requested settings in a given context and fall back to the default value
otherwise. Please note that NULL is not supported as a valid setting value.

:author:     direct Netware Group
:copyright:  direct Netware Group - All rights reserved
:package:    pas
:subpackage: plugins
:since:      v0.1.00
:license:    http://www.direct-netware.de/redirect.py?licenses;mpl2
             Mozilla Public License, v. 2.0
	"""

	def __init__(self, hook, **kwargs):
	#
		"""
Constructor __init__(HookableSettings)

:since: v0.1.00
		"""

		self.hook = hook
		"""
Hook called to get custom values
		"""
		self.params = kwargs
		"""
Hook parameters used to provide context relevant information
		"""
		self.settings = Settings.get_dict()
		"""
Settings instance
		"""
	#

	def is_defined(self, key):
	#
		"""
Checks if a given key is a defined setting.

:param key: Settings key

:return: (bool) True if defined
:since:  v0.1.00
		"""

		_return = True
		if (Hook.call(self.hook, **self.params) == None): _return = (key in self.settings)

		return _return
	#

	def get(self, key = None, default = None):
	#
		"""
Returns the value with the specified key.

:param key: Settings key
:param default: Default value if not set

:return: (mixed) Value
:since:  v0.1.00
		"""

		_return = Hook.call(self.hook, **self.params)
		if (_return == None): _return = self.settings.get(key)
		if (_return == None and default != None): _return = default

		return _return
	#
#

##j## EOF