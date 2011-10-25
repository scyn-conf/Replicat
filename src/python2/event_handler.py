"""
File: event_handler.py
Author: Remi <Scyn> Chaintron
"""


class EventCodes(object):
	""" Define event code and allow to retrieve event code names from value """

	COLLECTION = {
		'OPCODES' : {
		'ACCESS'        : 0x00000001, 
		'MODIFY'        : 0x00000002,
		'ATTRIB'        : 0x00000004,
		'CLOSE_WRITE'   : 0x00000008, 
		'CLOSE_NOWRITE' : 0x00000010,
		'OPEN'          : 0x00000020, 
		'MOVED_FROM'    : 0x00000040,
		'MOVED_TO'      : 0x00000080,
		'CREATE'        : 0x00000100,
		'DELETE'        : 0x00000200,
		'DELETE_SELF'   : 0x00000400,
		'MOVE_SELF'     : 0x00000800
		},

		'EVENTCODES' : {
		'UNMOUNT'       : 0x00002000,
		'Q_OVERFLOW'    : 0x00004000,
		'IGNORED'       : 0x00008000,
		},

		'SPECIALCODES' : {
		'ONLYDIR'       : 0x01000000,
		'DONT_FOLLOW'   : 0x02000001,
		'MASK_ADD'      : 0x20000000,
		'ISDIR'         : 0x40000000,
		'ONESHOT'       : 0x80000000,
		}
	}

	def itoa(value):
		""" Retrieve code name from its value.
		@param maskvalue: the code value 
		@return: the name of the code
		@rtype: string
		
		"""
		mask = value
		if mask & EventCodes.ISDIR:
			mask = value - EventCode.ISDIR
			return '%s | ISDIR' % EventCodes.VALUES[mask]
		return "%s" % EventCodes.VALUES[mask]
	itoa = staticmethod(itoa)

# make the collection's members directly accessible through the class
# dictionnary and build collection of values containing corresponding flags in
# order for EventCodes.itoa to be able to fetch names strings.
EventCodes.VALUES = {}
for label, codes in EventCodes.COLLECTION.items():
	for code, value in codes.items():
		EventCodes.VALUES[value] = code
		setattr(EventCodes, code, value)

