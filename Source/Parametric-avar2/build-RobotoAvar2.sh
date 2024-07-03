
source tools/robotoflexA2-env/bin/activate

## MAKE VF

## full glyphset
#fontmake -m source/Parametric-avar2/RobotoAvar2-avar1.designspace -o variable --output-path fonts/LGCAlpha/RobotoA2-avar1-VF.ttf --no-production-names
fontmake -m source/Parametric-avar2/RobotoAvar2-avar2.designspace -o variable --output-path fonts/LGCAlpha/RobotoA2-avar2-VF.ttf --no-production-names
fontmake -m source/Parametric-avar2/RobotoAvar2-avar2-no-fences.designspace -o variable --output-path fonts/LGCAlpha/RobotoA2-avar2-no-fences-VF.ttf --no-production-names

## SUBSET ascii
#python tools/subset.py


## MAKE INSTANCES
#fontmake -m source/Parametric-avar2/RobotoAvar2-avar2.designspace -i -o ufo --output-dir source/Parametric-avar2/instances/


## instancer
#fonttools varLib.instancer fonts/LGCAlpha/RobotoA2-avar2-VF.ttf XTRA=850

#Partial VFs
#fonttools varLib.instancer fonts/LGCAlpha/RobotoA2-avar2-VF.ttf opsz=144 wdth=25:151 wght=1:1000

deactivate