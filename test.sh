#!/bin/sh
cd "/Users/vmac/Documents/PROGRAMMING/PY/scrapy/NEWHKODDS/v3/HKOdds" && python ./HKOddsCollector.py -U "http://bet.hkjc.com/racing/getXML.aspx?type=jcbwracing_winplaodds&date=11-03-2015&venue=HV" > 2.log
# python ./HKOddsCollector.py -U "http://bet.hkjc.com/racing/getXML.aspx?type=jcbwracing_winplaodds&date=08-03-2015&venue=ST" > live.log
# python /Users/vmac/Documents/PROGRAMMING/PY/scrapy/NEWHKODDS/v3/HKOdds/HKOddsCollector.py -U "http://bet.hkjc.com/racing/getXML.aspx?type=jcbwracing_winplaodds&date=08-03-2015&venue=ST" > live.log
#python ./HKOddsCollector.py -U "http://bet.hkjc.com/racing/getXML.aspx?type=jcbwracing_winplaodds&date=04-03-2015&venue=HV" > 1.log
