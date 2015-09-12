#!/bin/bash
#11-03-2015
# INPUT_FILE="futuremeetings.csv"

# A pretend Python dictionary with bash 3 

NOW=$(date +"%d%m%Y")

# echo $nowu
#2 days 
nowplus2=$(date -v +2d +%d%m%Y)

# unix_now=$(date -d "${NOW}" +"%s")

ARRAY=( "11032015:HV"
		"15032015:ST"
        "18032015:HV"
        "21032015:ST"
        "25032015:ST"
        "29032015:ST"
        "01042015:HV"
        "07042015:ST"
        "12042015:ST"
        "15042015:HV"
        "19042015:ST"
        "22042015:HV"
        "26042015:ST"
        "29042015:HV"
        "03052015:ST"
        "06050215:HV"
        "09052915:ST"
        "13052015:HV"
        "16052015:ST"
        "20052015:HV"
        "24052015:ST"
        "27052015:ST"
        "31052015:ST"
        "03062015:HV"
        "07062015:ST"
        "10062015:HV"
        "14062015:ST"
        "17062015:HV"
        "21062015:ST"
        "24062015:HV"
        "27062015:ST"
        "01072015:ST"
        "05072015:ST"
        "08072015:HV"
        "12072015:ST"
         )
ARRAY1516=(  
        "06092015:ST"
        "09092015:HV"
        "13092015:ST"
        "16092015:HV"
        "19092015:ST"
        "23092015:HV"
        "28092015:ST"
        "01102015:ST"
        "04102015:ST"
        "07102015:HV"
        "14102015:HV"
        "18102015:ST"
        "22102015:HV"
        "25102015:ST"
        "01112015:HV"
        "08112015:ST"
        "01112015:HV"
        "14112015:ST"
        "18112015:ST"
        "21112015:ST"
        "25112015:HV"
        "29112015:ST"
        "02122015:HV"
        "06122015:HV"
        "09122015:HV"
        "13122015:HV"
        "16122015:HV"
        "19122015:HV"
        "23122015:HV"
        "27122015:HV"
        "01012016:ST"
        "06012016:HV"
        "09012016:HV"
        "13012016:HV"
        "17012016:ST"
        "20012016:HV"
        "24012016:ST"
        "31012016:ST"
        "03022016:HV"
        "06022016:ST"
        "10022016:ST"
        "14022016:ST"
        "17022016:HV"
        "21022016:ST"
        "24022016:HV"
        "28022016:ST"
        "02032016:HV"
        "06032016:HV"
        "09032016:HV"
        "13032016:ST"
        "16032016:HV"
        "20032016:ST"
        "28032016:ST"
        "31032016:HV"
        "03042016:ST"
        "06042016:ST"
        "10042016:ST"
        "13042016:HV"
        "16042016:ST"
         )


SORTED=($(printf '%s\n' "${ARRAY1516[@]}"|sort))
#get todays meet code
for m in "${SORTED[@]}" ; do
	THEDATE=${m%%:*}
	# THEDIFF= "${NOW}"-"${THEDATE}"
	# echo $THEDATE
	# unix_todate=$(date -d "${THEDATE}" +"%s")
	if [ "${THEDATE}" -ge "${NOW}" ]; then
		if [ "${THEDATE}" -le "${nowplus2}" ]; then 
    		echo $THEDATE

    		# THEDATE=$(date -d "${THEDATE}" +"%d-%m-%Y")
    		# NEWDATE=$(date -d $THEDATE +"%d-%m-%Y")
    		CODE=${m#*:}
    		 cd "/Users/vmac/Documents/PROGRAMMING/PY/scrapy/NEWHKODDS/v3/HKOdds" && python ./HKOddsCollector.py -U "http://bet.hkjc.com/racing/getXML.aspx?type=jcbwracing_winplaodds&date=${THEDATE:0:2}-${THEDATE:2:2}-${THEDATE:4:4}&venue=$CODE" > 5.log
    	fi
    fi
 
    # printf "%s likes to %s.\n" "$DATE" "$CODE"
done


# while read rdate code
# do
# # csv_array[$col2]=$col1
# aa[$rdate]=$code

# done < $INPUT_FILE

# echo "${!aa[*]}" 

# m[0]='test' || (echo 'Failure: arrays not supported in this version of bash.' && exit 2)

# m=(
# 	'15-03-2015 ST'
# 	'18-03-2015 HV'
#    )
# count=0
# while [ "x${m[count]}" != "x" ]
# do
#    count=$(( $count + 1 ))
# done

# today=$(date +"%d-%m-%Y")    	# The week of the year (0..53).
# today=${today#0}       	# Remove possible leading zero.
                                                                                
# let "index = $today"   # week modulo count = the lucky person

# email=${m[index]}     # Get the lucky person's e-mail address.
                                                                                
# echo $email     	# Output the person's e-mail address.



# homedir[ormaaj]=/home/ormaaj # Ordinary assignment adds another single element

# for user in "${!homedir[@]}"; do   # Enumerate all indices (user names)
#     printf 'Home directory of user %s is: %s\n' "$user" "${homedir[$user]}"
# done


# csv=( $(cat "$infile"))
# declare -A m
# m=( ["15-03-2015"]="ST" ["18-03-2015"]="HV")
# NOW=$(date +"%d-%m-%Y")

# echo "Current user is: $USER.  Full name: ${m[$USER]}."

# echo "${m["$NOW"]}"
# m=( $(cat "$infile"))
# l=("0")
# for element in $(seq $l $((  ${#m[@]} - 1)) )
# do
# 	echo "${m[$element]}"
# done
# $l = $l+1
# while IFS=, read -ra arr; do
#     ## Do something with $a, $b and $c
#     echo "${arr[0]:0}" #dates
# done < $infile

# OLDIFS="$IFS"

# # Create the CSV Array Hash keyed by Col #2
# while IFS="," read -r col1 col2
# do
#     csv_array[$col2]=$col1
# done <<EOD
# $csv
# EOD

# #For each key in Data Hash, print out corresponding keyed value in CSV Hash
# for key in "${!csv_array[@]}"
# do
#     echo "$key ${csv_array[$key]}"
# done
# IFS="$OLDIFS"
# eCollection=( $(cut -d ',' -f2 futuremeetings.csv ) )
# printf '%s\t%s' "${eCollection[0]}, ${eCollection[1]}"

# printf "http://bet.hkjc.com/racing/getXML.aspx?type=jcbwracing_winplaodds&date="+ ${eCollection[0]}+ "&venue=" + ${eCollection[1]} 

# VENUE = $("HV")
# cd "/Users/vmac/Documents/PROGRAMMING/PY/scrapy/NEWHKODDS/v3/HKOdds" && python ./HKOddsCollector.py -U "http://bet.hkjc.com/racing/getXML.aspx?type=jcbwracing_winplaodds&date=$NOW&venue=HV" > 2.log
# python ./HKOddsCollector.py -U "http://bet.hkjc.com/racing/getXML.aspx?type=jcbwracing_winplaodds&date=08-03-2015&venue=ST" > live.log
# python /Users/vmac/Documents/PROGRAMMING/PY/scrapy/NEWHKODDS/v3/HKOdds/HKOddsCollector.py -U "http://bet.hkjc.com/racing/getXML.aspx?type=jcbwracing_winplaodds&date=08-03-2015&venue=ST" > live.log
# python ./HKOddsCollector.py -U "http://bet.hkjc.com/racing/getXML.aspx?type=jcbwracing_winplaodds&date=04-03-2015&venue=HV" > 1.log
