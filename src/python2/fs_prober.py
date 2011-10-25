"""
File: fs_prober.py
Author: Remi <Scyn> Chaintron
"""

import os

STATE_PROBED	= 1
STATE_NEW	= 0
STATE_UNPROBED	= -1


class FsProber(object):
	"""
	While inotify provides informations about the changes occurring in the
	inodes it watches, it does not about its subdirectories. FsProber
	provides a way to probe inodes and their subdirectories and obtain
	informations about the 'state' of the filesystem from an inode's point
	of view.

	"""

	def __init__(self, root):
		""" Constructor.
		@param root: the root inode of the filesystem which state to represent
		
		"""
		self.root = root
		# add final / if it is not present
		if len(root) > 0 and root[-1] != '/':
			self.root += '/'
		self._state = {}


	def probe(self):
		""" Probe the filesystem for changes and update the recorded
		state, while returning the changes (deletions and creations).
		@return: a tuple containing the pathnames of the deleted and new directories
		@rtype: tuple of lists

		"""
		# we mark all entries as unprobed and we probe the root
		for key in self._state.keys():
			self._state[key] = STATE_UNPROBED
		self._probe(self.root)
		# get new and deleted dirs
		deleted_dirs = []
		new_dirs = []
		# for each inode in the state
		for inode, status in self._state.items():
			# if it is unprobed, delete it from the state
			if status == STATE_UNPROBED:
				deleted_dirs.append(inode)
				del self._state[inode]
			if status == STATE_NEW:
				new_dirs.append(inode)
		# return the changes
		return (deleted_dirs, new_dirs)


	def _probe(self, directory):
		""" Probe a directory and propagate on its subdirectories.
		@param directory: the directory to probe

		"""
		# if directory was already recorded in state, mark is at probed
		if self._state.has_key(directory):
			self._state[directory] = STATE_PROBED
		else: # mark is as new
			self._state[directory] = STATE_NEW
		# for each node in the directory
		for dir_entry in os.listdir(directory):
			# if it is a directory, add it to the filesystem state and probe it
			if os.path.isdir(directory + dir_entry):
				self._probe(directory + dir_entry + '/')

