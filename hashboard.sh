#!/usr/bin/env bash

param=$(echo $1 $2)
rainbowpath=$(echo "$3rainbow.table")
realcounter=$(echo "$4")
loopcounter=0
file=$(echo "$6")
success=0
Sec2Test=$(echo "$7")
check=0


echo "============================================="
echo "Tweet Nbr : $4 / $5"
echo "Trying to find Md5 in $6 :"
echo "Seconds to test : $Sec2Test "
echo "Any luck ? $success"

HalfSec2Test=$(($Sec2Test/2))
paramfinal2=$(echo $(date -d "$param $HalfSec2Test seconds ago" "+%Y-%m-%d %H:%M:%S"))


function show_time () {
    num=$1
    min=0
    hour=0
    day=0
    if((num>59));then
        ((sec=num%60))
        ((num=num/60))
        if((num>59));then
            ((min=num%60))
            ((num=num/60))
            if((num>23));then
                ((hour=num%24))
                ((day=num/24))
            else
                ((hour=num))
            fi
        else
            ((min=num))
        fi
    else
        ((sec=num))
    fi
    echo "$day"d "$hour"h "$min"m "$sec"s
}



((HalfSec2Test++))
paramfinal=$(echo $(date -d "$param $HalfSec2Test seconds ago" "+%Y-%m-%d %H:%M:%S"))
#paramfinal=$(echo $(date -d "$param $Sec2Test seconds ago" "+%Y-%m-%d %H:%M:%S"))

for i in `seq 1 $Sec2Test`
do
		((loopcounter++))
		DATE=$(echo $(date -d "$paramfinal $i seconds" "+%Y-%m-%d;%H:%M:%S"))
		let "counter = 0"
		realtwt=$(($5-$4+1))
		SECONDS=0
                TimeLeft="Calculating.."
                FinalTimeLeft="Calculating.."


		while read line
		do


        	     SAMPLE=$(echo $line)
        	     MD5=$(echo $DATE $SAMPLE \
        	        | md5sum \
			| awk '{ print $1 }')


		     if [ $counter -eq 100 ]
		     then
				if [ $check -eq 0 ]
				then
					
		                	Laps=$SECONDS
                                	math=$(($Laps*310*$realtwt*$Sec2Test))
					math1lap=$(($Laps*310))
					Finalmath=$math
					
				else
					Finalmath=$(($Finalmath-$math1lap))
					
				fi

                                TimeLeft=$(show_time "$Finalmath")
				FinalTimeLeft="$TimeLeft ......"
				check=1

		     fi 

		if [ $counter -lt 100 ]
		then
			echo -ne "Time Left : $TimeLeft\\r"
		else
			echo -ne "Time Left : $FinalTimeLeft\\r"
		fi	     


		md5="$MD5"
		pos=6
		startpos=0
		size=${#md5}
		size2=$(($size-6))

		while [ $startpos -le $size ]
		do

		        sample=${md5:$startpos:$pos}

		        cat "$file" | grep -q "$sample"

		        if [ $? -eq 0 ] 
		        then

				((success++))

                                echo "=============================================">>$rainbowpath
				echo "Success : $success"
		                echo "Fucking Found $sample in $file !"
				echo "Fucking Found $sample in $file !">>$rainbowpath
				echo "Date = $DATE Tweet Nbr : $4 Current Second : $loopcounter"
		                echo "Date = $DATE Tweet Nbr : $4 Current Second : $loopcounter">>$rainbowpath
				echo "Text = $SAMPLE"
        		        echo "Text = $SAMPLE">>$rainbowpath
				echo "Md5sum = $MD5"
                		echo "Md5sum = $MD5">>$rainbowpath
                		echo "=============================================">>$rainbowpath

				sizeleft=$(($size-$startpos))

				if [ $pos -le $sizeleft ]
				then
					let pos=pos+1
				else
					break
				fi
				sleep 10
				
		         else
				
#		             	echo "$counter / 31102 "
				pos=6
				if [ $startpos -le $size2 ]
				then
					let startpos=startpos+1
				else
					break
				fi

		        fi

		done

	     	((counter++))
	done < bible.txt

done

echo
echo
echo "Found $success md5 hash in $file wich are exactly the same as in $rainbowpath"

if [ $success -eq 0 ]
then
	echo;echo;echo;
	echo "fuck my life"
fi

echo 
