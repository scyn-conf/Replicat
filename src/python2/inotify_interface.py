"""
File: inotify_interface.py
Author: Remi <Scyn> Chaintron
"""

import ctypes

class InotifyInterface(object):
	"""
	Provide interface with Linux kernel's inotify subsystem. Inotify acts to
	extend filesystems to notice changes to the filesystem and report those
	changes.
	"""

	def __init__(self):
		""" Constructor """
		# retrieve libc using ctypes
		try:
			libname = ctypes.util.find_library('c')
		except (OSError, IOError):
			pass
		self._libc = ctypes.CDLL(libname)
		# abort if libc does not contain required functions
		if self._libc is None or not hasattr(self._libc, 'inotify_init')
				or not hasattr(self._libc, 'inotify_add_watch')
				or not hasattr(self._libc, 'inotify_rm_watch')):
			return None
		# else store inotify's file descriptor
		self.fd = self._libc.inotify_init()


	def add_watch(self, pathname, events):
		"""
		Start watching an inode for events
		@param pathname: inode's pathname
		@param events: events to notify
		@return: a watch descriptor, unique to the inode pointed to by
		the pathname
		@rtype: integer
		"""
		return self._libc.inotify_add_watch(self.fd, pathname, events)

	def rm_watch(self, wd):
		"""
		Stop watching an inode for events
		@param wd: watch descriptor to cancel the watch on
		"""
		return self._libc.inotify_rm_watch(self.fd, wd)

