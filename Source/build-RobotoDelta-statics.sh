
source tools/RobotoflexA2-env/bin/activate

declare -a weights=('100' '400' '1000')
declare -a widths=('25' '100' '151')
declare -a opticalsize=('8' '14' '144')
declare -a grade=('0')
declare -a posture=('Roman' 'Italic')

declare STATICS_DIR='fonts/LGCAlpha/statics/'

if [ -d $STATICS_DIR ]; then
	rm -r $STATICS_DIR
fi

mkdir $STATICS_DIR

for fontGrade in ${grade[@]}
do
	for fontPosture in ${posture[@]}
	do
		for fontOpticalSize in ${opticalsize[@]}
		do
			for fontWidth in ${widths[@]}
				do
				
				declare DIR_NAME='fonts/LGCAlpha/statics/'$fontPosture'-GRAD'$fontGrade'-opsz'$fontOpticalSize'-wdth'$fontWidth
				
				if [ -d $DIR_NAME ]; then
					rm -r $DIR_NAME
				fi
				
				mkdir $DIR_NAME
				
				for fontWeight in ${weights[@]}
				do
					PATH_INSTANCES='fonts/LGCAlpha/statics'
					PATH_GRADE=$fontPosture'-GRAD'$fontGrade'-opsz'$fontOpticalSize'-wdth'$fontWidth
					FILENAME=RobotoDelta-$fontPosture'-GRAD'$fontGrade-opsz$fontOpticalSize-wdth$fontWidth-wght$fontWeight
					FULL_PATH=$PATH_INSTANCES/$PATH_GRADE
					LOCATION=$fontPosture'-GRAD'$fontGrade'-opsz'$fontOpticalSize'-wdth'$fontWidth'-wght'$fontWeight
					LOCATION_WP='GRAD'$fontGrade'-opsz'$fontOpticalSize'-wdth'$fontWidth'-wght'$fontWeight
					
					if [ $fontPosture == 'Roman' ]; then
						fonttools varLib.instancer fonts/LGCAlpha/RobotoDelta-Roman-VF.ttf opsz=$fontOpticalSize wght=$fontWeight wdth=$fontWidth -o $FULL_PATH/$FILENAME.ttf --static
						
						# # Update nameIDs
						python3 tools/updateNameIDs-avar1-datestamp.py -f "Roboto Delta Roman" -s $LOCATION_WP -i $FULL_PATH/$FILENAME.ttf -o $FULL_PATH/$FILENAME.ttf -d False
						
						echo 'Location / Stylename' + $LOCATION_WP
					else
						fonttools varLib.instancer fonts/LGCAlpha/RobotoDelta-Italic-VF.ttf opsz=$fontOpticalSize wght=$fontWeight wdth=$fontWidth -o $FULL_PATH/$FILENAME.ttf --static
						
						# # Update nameIDs
						python3 tools/updateNameIDs-avar1-datestamp.py -f "Roboto Delta Italic" -s $LOCATION_WP -i $FULL_PATH/$FILENAME.ttf -o $FULL_PATH/$FILENAME.ttf -d False
						
					fi
					
				done
			
			done
		done
	done
done

deactivate
