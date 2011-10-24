#!/usr/bin/python2
"""
File: replicat.py
Author: Remi <Scyn> Chaintron
"""

import sys
import logging
import optparse

def main():
	""" Main function """
	pass


if __name__ == '__main__':
	"""
	Program's entry point.
	Set up option parsing and logging
	"""
	# create parser
	parser = optparse.OptionParser()
	parser.add_option('-v', '--verbose', dest='verbose', action='count', 
			help='Increase verbosity (specify multiple times for more)')
	# parse command line
	opts, args = parser.parse_args()
	
	# set up logger
	log_format = '%(levelname)s : %(message)s'
	log_level = logging.WARNING
	if opts.verbose == 1:
		log_level = logging.INFO
	if opts.verbose >= 2:
		log_level = logging.DEBUG
	logging.basicConfig(level=log_level, format=log_format)
	# main function
	main()
