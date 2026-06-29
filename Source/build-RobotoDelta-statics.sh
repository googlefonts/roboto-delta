#!/bin/bash
python3 -m venv tools/RobotoflexA2-env
source tools/RobotoflexA2-env/bin/activate

pip install fonttools

# Check if VIRTUAL_ENV is set
if [ -z "$VIRTUAL_ENV" ]; then
    echo "❌ Error: No active Python virtual environment detected!"
    echo "Please activate your venv before running this script."
    exit 1
fi

echo "✅ Using virtual environment: $VIRTUAL_ENV"

declare -a weights=('1' '100' '200' '300' '400' '500' '600' '700' '800' '900' '1000')
declare -a widths=('25' '50' '75' '100' '125' '151')
declare -a opticalsize=('8' '14' '36' '72' '144')
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
						"$VIRTUAL_ENV/bin/python" tools/updateNameIDs-avar1-datestamp.py -f "Roboto Delta Roman" -s $LOCATION_WP -i $FULL_PATH/$FILENAME.ttf -o $FULL_PATH/$FILENAME.ttf -d False
						
						echo 'Location / Stylename' + $LOCATION_WP
					else
						fonttools varLib.instancer fonts/LGCAlpha/RobotoDelta-Italic-VF.ttf opsz=$fontOpticalSize wght=$fontWeight wdth=$fontWidth -o $FULL_PATH/$FILENAME.ttf --static
						
						# # Update nameIDs
						"$VIRTUAL_ENV/bin/python" tools/updateNameIDs-avar1-datestamp.py -f "Roboto Delta Italic" -s $LOCATION_WP -i $FULL_PATH/$FILENAME.ttf -o $FULL_PATH/$FILENAME.ttf -d False
						
					fi
					
				done
			
			done
		done
	done
done

deactivate
