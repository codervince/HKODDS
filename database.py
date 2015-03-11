# -*- coding: utf-8 -*-

from config import Config, CONFIG_FILE
import models
from models.meta import Session, Base
from models.HKOddsModel import HKOddsModel
import sqlalchemy as sa
from optparse import OptionParser, OptionGroup
from decimal import *

# It's for get out exceptions in unicode.
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Implementation class for working with database.
class Database(object):
	# Initialization.
	def __init__(self):
		self.bReady = True
		config = Config()
		if not config.isReady():
			self.bReady = False
		self.config = config.getDBSettings()
		try:
			self.engine = sa.engine_from_config(self.config[0], self.config[1])
			models.init_model(self.engine)
		except Exception, e:
			print u'Database exception: %s' % (e)
			self.bReady = False

	# Connect to database server.
	def connection(self):
		try:
			self.connection = self.engine.connect()
		except Exception, e:
			print u'Database exception: %s' % (e)
			self.bReady = False

	# Create session.
	def createSession(self):
		try:
			self.session = Session()
		except Exception, e:
			print u'Database exception: %s' % (e)
			self.bReady = False

	# Creating tables in database (need use one time only).
	def createTablesByModels(self):
		try:
			Base.metadata.create_all(bind = self.engine)
		except Exception, e:
			print u'Database exception: %s' % (e)
			self.bReady = False

	# Add row in HK_odds table.
	def addRowToTableHKOdds(self, race_date, race_course_code, race_number, horse_number, update_datetime, win_odds, is_win_fav, place_odds, is_place_fav, pool, is_reserve = False, is_scratched = False):
		if not race_date or not race_course_code or not race_number or horse_number == None or not update_datetime or win_odds == None or is_win_fav == None or place_odds == None or is_place_fav == None or not pool:
			return
		self.createSession()
		try:
			self.session.begin()
			win_odds = Decimal(win_odds)
			place_odds = Decimal(place_odds)
			hk_odds_model = HKOddsModel(race_date, race_course_code, race_number, horse_number, update_datetime, win_odds, is_win_fav, place_odds, is_place_fav, pool, is_reserve, is_scratched)
			self.session.add(hk_odds_model)
			self.session.commit()
		except Exception, e:
			print u'Database exception: %s' % (e)
			self.bReady = False

	# Check if database is not available.
	def isReady(self):
		return self.bReady

if __name__ == '__main__':
	usage = u'Use %prog -h for get more information.'
	parser = OptionParser(usage = usage)
	# Script parameters description.
	parser.add_option(u'--cdb', dest = 'cdb', action = 'store_true', default = None, help = u'Create database tables.')
	(options, args) = parser.parse_args()
	if options.cdb:
		db = Database()
		if not db.isReady():
			print u'Error database usage. Please, check if database is available, config file exists, file with security key exists.'
		else:
			db.createTablesByModels()
