"""
File: watcher.py
Author: Remi <Scyn> Chaintron
"""



class Watcher(object):
	""" Abstract class watcher-type classes inherit from.  """

	identifier = "UndefinedWatcher"
	_event_handler = None

	def __init__(self, event_handler):
		""" Constructor """
		self._event_handler = event_handler
		pass


	def register(self, event_handler):
		""" Register to an event handler in order to be triggered when
		events regarding the watched elements are detected.

		"""
		pass


	def unregister(self):
		""" Unsubscribe from subscribed event handler. """
		pass


	def notify(self, event):
		""" The function called whenever an event regarding watched
		elements is detected.
		"""
		pass
