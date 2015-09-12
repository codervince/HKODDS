# -*- coding: utf-8 -*-

from sqlalchemy.types import Float, Unicode, BigInteger, Integer, Boolean, Date, DateTime, Unicode, DECIMAL, String
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import *
from models.meta import *

# It's for get out exceptions in unicode.
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


#HK odds model implementation.
class HKOddsModel(Base):
	__tablename__ = "hk_odds"
	id = Column(BigInteger, primary_key = True, autoincrement = True, nullable = False) # Unique ID
	race_date = Column("racedate", Date, nullable = False) # Race date.
	race_course_code = Column("racecoursecode", Unicode(2)) # Race course code.
	race_number = Column("racenumber", Integer) # Race number.
	horse_number = Column("horsenumber", Integer, nullable = False) # Horse number.
	update_date_time = Column("updatedate", DateTime, nullable = False) # Date and time of last update.
	win_odds = Column("winodds", DECIMAL(10,2)) # Odds of win. It's not float! Float for money is not acceptable!
	is_win_fav = Column("isWinFav", Integer) # Some times this parameter can takes value 2 and more.
	place_odds = Column("placeodds", DECIMAL(10,2)) # The same as Win odds.
	is_place_fav = Column("isPlaceFav", Integer) # The same as is_win_fav.
	pool = Column("pool", BigInteger) # Pool number.
	is_reserve = Column("isReserve", Boolean) # Reserve data.
	is_scratched = Column("isScratched", Boolean) # Scratched data.

# class HKOddsStats(Base):
# 	__tablename__ = "hk_oddsstats"
# 	id = Column(BigInteger, primary_key = True, autoincrement = True, nullable = False) # Unique identificator.
# 	race_date = Column("racedate", Date, nullable = False) # Race date.
# 	race_number = Column("racenumber", Integer, nullable=False) # Race number
# 	horse_number = Column("horsenumber", Integer, nullable = False) # Horse number.
# 	update_date_time = Column("updatedate", DateTime, nullable = False) # Date and time of last update.
# 	OP_win = Column("opwin", DECIMAL(10,2)) 
# 	pc_win_now_op = Column("pcnowwinop", Float)
# 	win_now = Column("winnow", DECIMAL(10,2))
# 	winoddsrank_now = Column("winoddsrank_now", Integer)
# 	bettingline_now = Column("bettingline", Integer)
# 	bettingline_op = Column("bettinglineop", Integer)
# 	bettinglinedist_now = Column("bettinglinedistnow", String)
# 	bettinglinedist_op = Column("bettinglinedistop", String)   
# 	pc_win_now_L1 = Column("pcwinnowl1", Float) #last change
# 	win_L1 = Column("winl1", DECIMAL(10,2)) 
# 	op_win_racemax = Column("winopracemax", DECIMAL(10,2))
# 	op_win_racemin = Column("winopracemin", DECIMAL(10,2))
# 	now_win_racemax = Column("nowwinracemax", DECIMAL(10,2))
# 	now_win_racemin = Column("nowwinracemin", DECIMAL(10,2))
# 	now_avgwinodds = Column("nowavgwinodds", DECIMAL(10,2))
# 	op_avgwinodds = Column("opavgwinodds", DECIMAL(10,2))

	# Create record.
	def __init__(self, race_date, race_course_code, race_number, horse_number, update_date_time, win_odds, is_win_fav, place_odds, is_place_fav, pool, is_reserve = False, is_scratched = False):
		self.race_date = race_date
		self.race_course_code = race_course_code
		self.race_number = race_number
		self.horse_number = horse_number
		self.update_date_time = update_date_time
		self.win_odds = win_odds
		self.is_win_fav = is_win_fav
		self.place_odds = place_odds
		self.is_place_fav = is_place_fav
		self.pool = pool
		self.is_reserve = is_reserve
		self.is_scratched = is_scratched
