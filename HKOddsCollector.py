# -*- coding: utf-8 -*-

import datetime
from optparse import OptionParser, OptionGroup
import re
import urllib
import urllib2
import cookielib
import time
from decimal import *

from database import Database

# It's for get out exceptions in unicode.
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class HKOddsCollector(object):
	# Initialization.
	def __init__(self):
		self.URL = u''
		self.req_data = None
		self.race_date = None
		self.race_course_code = u''
		self.race_number = 0
		self.is_reserve = False
		self.is_scratched = False
		self.bReady = True
		self.db = Database()
		self.db.connection()
		if not self.db.isReady():
			self.bReady = False

	# Set URL.
	def setURL(self, URL = None):
		if not URL:
			print u'Error. URL is empty.'
			return
		self.URL = URL

	# Set race date.
	def setRaceDate(self, race_date = None):
		if not race_date:
			print u'Warning. Race date is empty.'
			return
		try:
			race_date = race_date.split(u'-')
			self.race_date = datetime.date(int(race_date[2]), int(race_date[1]), int(race_date[0]))
		except:
			print u'Warning. Race date format error.'

	# Set race course code.
	def setRaceCourseCode(self, race_course_code = None):
		if not race_course_code or race_course_code != u'HV' and race_course_code != u'ST':
			print u'Warning. Race course code is empty.'
			return
		self.race_course_code = race_course_code

	# Set race number.
	def setRaceNumber(self, race_number = 0):
		if not race_number:
			print u'Warning. Race number is 0.'
			self.race_number = 0
			return
		try:
			self.race_number = int(race_number)
		except:
			print u'Warning. Race number is 0.'
			self.race_number = 0

	# Set if reserve.
	def setIsReserve(self, is_reserve = False):
		if is_reserve == None or is_reserve != False and is_reserve != True:
			print u'Warning. Reserve flag wrong.'
			return
		self.is_reserve = is_reserve

	# Set if scratched.
	def setIsScratched(self, is_scratched = False):
		if is_scratched == None or is_scratched != False and is_scratched != True:
			print u'Warning. Scratched flag wrong.'
			return
		self.is_scratched = is_scratched

	# Get data from URL.
	def getPageData(self):
		if not self.URL:
			return None
		tryes = 0
		while tryes < 3:
			try:
				headers = {u'content-type': u'text/xml', u'charset': u'utf-8'}
				request = urllib2.Request(self.URL, self.req_data, headers)
				response = urllib2.urlopen(request, None, 30000)
				data = response.read()
				response.close()
				self.updatedatetime = datetime.datetime.now()
				return data
			except Exception, e:
				print  u'Error.  %s.' % (e)
				time.sleep(5)
				tryes +=1
		if tryes > 3:
			print u'Can\'t get data form URL: %s.' % (URL)
		return None


	# Processing.
	def processing(self):
		if not self.URL:
			print u'Error. URL is empty. Exit.'
			return False
		if not self.race_date:
			race_date = re.search(u'date=(\d+-\d+-\d+)', self.URL)
			if not race_date:
				print u'Error. Race date unknown.'
				return False
			self.setRaceDate(race_date.group(1))
			if not self.race_date:
				print u'Error. Race date unknown.'
				return False
		if not self.race_course_code:
			race_course_code = re.search(u'venue=(.+)', self.URL)
			if not race_course_code:
				print u'Error. Race course code unknown.'
				return False
			self.setRaceCourseCode(race_course_code.group(1))
			if not self.race_course_code:
				print u'Error. Race course code unknown.'
				return False
		if not self.is_reserve or not self.is_scratched:
			reserve_data = re.search(u'type=(.+)', self.URL)
			if not reserve_data:
				print u'Error. It seems URL is worng. No type value.'
				return
			reserve_data = reserve_data.group(1).split(u'&')[0].split(u'_')
			reserve_data = reserve_data[-1]
			if not self.is_reserve and reserve_data == u'reserve':
				self.is_reserve = True
			if not self.is_scratched and reserve_data == u'scratched':
				self.is_scratched = True
		data = self.getPageData()
		if not data:
			return False
		data = re.search(u'<OUT>(.*)<\/OUT>', data)
		if not data:
			print u'Error. Wrong response from server.'
			return False
		data = data.group(1).split(u'@@@')
		try:
			self.pool = int(data[0])
		except Exception, e:
			print u'Error. It seems data is wrong. Can\'t get pool number.'
			return False
		data = data[1:]
		self.race_number = 0
		for item in data:
			if not item:
				continue
			item = item.split(u'#PLA')
			item[0] = item[0][3:]
			if len(item[0]) > 0:
				item[0] = item[0][1:]
			else:
				continue
			win = item[0].split(u';')
			if len(win) > 0:
				self.race_number += 1
			pla = item[1].split(u';')
			win_dict = {}
			for i in win:
				i = i.split(u'=')
				if len(i) > 0:
					win_dict[i[0]] = [i[1], i[2]]
			pla_dict = {}
			for i in pla:
				i = i.split(u'=')
				if len(i) > 1:
					pla_dict[i[0]] = [i[1], i[2]]
			if not self.bReady:
				return False
			for i in win_dict.keys():
				if win_dict[i][0] == u'SCR':
					win_dict[i][0] = -1
				if i not in pla_dict.keys() or pla_dict[i][0] == u'SCR':
					pla_dict[i][0] = -1
					pla_dict[i][1] = -1
				self.db.addRowToTableHKOdds(self.race_date, self.race_course_code, self.race_number, i, self.updatedatetime, win_dict[i][0], win_dict[i][1], pla_dict[i][0], pla_dict[i][1], self.pool, self.is_reserve, self.is_scratched)
			for i in pla_dict.keys():
				if i not in win_dict.keys():
					win_dict[i][0] = -1
					win_dict[i][1] = -1
					if pla_dict[i][0] == u'SCR':
						pla_dict[i][0] = -1
					self.db.addRowToTableHKOdds(self.race_date, self.race_course_code, self.race_number, i, self.updatedatetime, win_dict[i][0], win_dict[i][1], pla_dict[i][0], pla_dic[i][1], self.pool, self.is_reserve, self.is_scratched)
		return True

if __name__ == '__main__':
	usage = u'Use %prog -h for get more information.'
	parser = OptionParser(usage = usage)
	# Script parameter description.
	parser.add_option(u'-U', u'--URL', dest = u'URL', type = 'string', default = None, help = u'URL.')
	parser.add_option(u'-d', u'--race_date', dest = u'race_date', type = 'string', default = None, help = u'Race date in format DD-MM-YYYY. Optional parameter.')
	parser.add_option(u'-c', u'--race_course_code', dest = u'race_course_code', type = 'string', default = None, help = u'Race course code. Optional parameter.')
	parser.add_option(u'-n', u'--race_number', dest = u'race_number', type = 'string', default = None, help = u'Race number')
	parser.add_option(u'-r', u'--reserve', dest = u'is_reserve', action = 'store_true', default = False, help = u'Set reserve.')
	parser.add_option(u'-s', u'--scratched', dest = u'is_scratched', action = 'store_true', default = False, help = u'Set scratched')
	(options, args) = parser.parse_args()
	collector = HKOddsCollector()
	if options.URL:
		collector.setURL(options.URL)
	if options.race_date:
		collector.setRaceDate(options.race_date)
	if options.race_course_code:
		collector.setRaceCourseCode(options.race_course_code)
	if options.race_number:
		collector.setRaceNumber(options.race_number)
	if options.is_reserve:
		collector.setIsReserve(options.is_reserve)
	if options.is_scratched:
		collector.setIsScratched(options.is_scratched)
	if collector.processing():
		print u'HK odds collected succesfully.'
