# -*- coding: utf-8 -*-

import ConfigParser

# Config file name.
CONFIG_FILE = u'HKOdds.conf'

# It's for get out exceptions in unicode.
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Read config class.
class Config(object):
	# Initialization.
	def __init__(self):
		self.bReady = True
		try:
			self.config = ConfigParser.ConfigParser()
			self.config.read(CONFIG_FILE)
		except:
			self.bReady = False

	# Check if config file can't be read.
	def isReady(self):
		return self.bReady

	# Get database settings.
	def getDBSettings(self):
		return (dict(self.config.items("database")), "sqlalchemy.")

if __name__ == '__main__':
	pass
