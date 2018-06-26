#!/bin/bash
set e

choices="
1.) kivycatalog  
3.) multistroke 
4.) pictures
5.) shadereditor
2.) showcase
6.) touchtracer
7.) camera puzzle
"
PS3="Please choose your option "
select option in kivycatalog showcase multistroke pictures shadereditor touchtracer camerapuzzle 3Drendering RST_Editor compass takepicture audio camera container designwithkv quickstart includes keyboard settings svg tutorial_notes  sequenced_images pong_tutorial pong_tutorial_step1 pong_tutorial_step2 pong_tutorial_step3 pong_tutorial_step4 pong_tutorial_step5 quit

do
	case $option in
		1|kivycatalog )
			exec python3 /usr/share/kivy-examples/demo/kivycatalog/./main.py&
			;;
		2|showcase )
			exec python3 /usr/share/kivy-examples/demo/showcase/./main.py&
			;;
		3|multistroke )
			exec python3 /usr/share/kivy-examples/demo/multistroke/./main.py& 
			;;
		4|pictures )
			exec python3 /usr/share/kivy-examples/demo/pictures/./main.py&
			;;
		5|shadereditor )
			exec python3 /usr/share/kivy-examples/demo/shadereditor/./main.py&
			;;
		6|touchtracer )
			exec python3 /usr/share/kivy-examples/demo/touchtracer/./main.py&
			;;
		7|camerapuzzle )
			exec python3 /usr/share/kivy-examples/demo/ ./camera_puzzle.py&
			;;
		8|3Drendering)
			exec python3 /usr/share/kivy-examples/3Drendering/main.py&
			;;
		9|RST_Editor)
			exec python3 /usr/share/kivy-examples/RST_Editor/main.py&
			;;
		10|compass)
			exec python3 /usr/share/kivy-examples/android/compass/main.py&
			;;
		11|takepicture)
			exec python3 /usr/share/kivy-examples/android/takepicture/main.py&
			;;
		12|audio)
			exec python3 /usr/share/kivy-examples/audio/main.py&
			;;
		13|camera)
			exec python3 /usr/share/kivy-examples/camera/main.py&
			;;
		14|container)
			exec python3 /usr/share/kivy-examples/container/main.py&
			;;
		15|designwithkv)
			exec python3 /usr/share/kivy-examples/guide/designwithkv/main.py&
			;;
		16|quickstart)
			exec python3 /usr/share/kivy-examples/guide/quickstart/main.py&
			;;
		17|includes)
			exec python3 /usr/share/kivy-examples/includes/main.py&
			;;
		18|keyboard)
			exec python3 /usr/share/kivy-examples/keyboard/main.py&
			;;
		19|settings)
			exec python3 /usr/share/kivy-examples/settings/main.py&
			;;
		20|svg)
			exec python3 /usr/share/kivy-examples/svg/main.py&
			;;
		21|tutorial_notes)
			exec python3 /usr/share/kivy-examples/tutorials/notes/final/main.py&
			;;
		22|sequenced_images)
			exec python3 /usr/share/kivy-examples/widgets/sequenced_images/main.py&
			;;
		23|pong_tutorial)
			exec python3 /usr/share/kivy-examples/tutorials/pong/main.py&
			;;
		24|pong_tutorial_step1)
			exec python3 /usr/share/kivy-examples/tutorials/pong/steps/step1/main.py&
			;;
		25|pong_tutorial_step2)
			exec python3 /usr/share/kivy-examples/tutorials/pong/steps/step2/main.py&
			;;
		26|pong_tutorial_step3)
			exec python3 /usr/share/kivy-examples/tutorials/pong/steps/step3/main.py&
			;;
		27|pong_tutorial_step4)
			exec python3 /usr/share/kivy-examples/tutorials/pong/steps/step4/main.py&
			;;
		28|pong_tutorial_step5)
			exec python3 /usr/share/kivy-examples/tutorials/pong/steps/step5/main.py&
			;;
		29| quit )
			break
			;;
		* )
			echo "Remember what you learned here today."
			exit 1
	esac
done	

# Install on Ubuntu bionic 18.04

# pip3 install --user Cython==0.26.1

# kivy for each user of the system (doing otherwise breaks pip under various Ubuntu, certainly bionic 18.04)
#pip3 install --user kivy pygame

# for compass (don't install until kivy is install/built since the cython require exceeds kivy's build compatibility, and you may require java components as wellcp)
#pip3 install --user jnius

#sudo apt-get install python3-kivy python-kivy-examples


#pong_tutorial pong_tutorial_step1 pong_tutorial_step2 pong_tutorial_step3 pong_tutorial_step4 pong_tutorial_step5
#exec python3 /usr/share/kivy-examples/demo/kivycatalog/main.py&
#exec python3 /usr/share/kivy-examples/demo/multistroke/main.py&
#exec python3 /usr/share/kivy-examples/demo/pictures/main.py&
#exec python3 /usr/share/kivy-examples/demo/shadereditor/main.py&
#exec python3 /usr/share/kivy-examples/demo/showcase/main.py&
#exec python3 /usr/share/kivy-examples/demo/touchtracer/main.py&

#exec python3 /usr/share/kivy-examples/3Drendering/main.py&
#exec python3 /usr/share/kivy-examples/RST_Editor/main.py&
#exec python3 /usr/share/kivy-examples/android/compass/main.py&
#exec python3 /usr/share/kivy-examples/android/takepicture/main.py&
#exec python3 /usr/share/kivy-examples/audio/main.py&
#exec python3 /usr/share/kivy-examples/camera/main.py&
#exec python3 /usr/share/kivy-examples/container/main.py&

#exec python3 /usr/share/kivy-examples/guide/designwithkv/main.py&
#exec python3 /usr/share/kivy-examples/guide/quickstart/main.py&

#exec python3 /usr/share/kivy-examples/includes/main.py&
#exec python3 /usr/share/kivy-examples/keyboard/main.py&
#exec python3 /usr/share/kivy-examples/settings/main.py&
#exec python3 /usr/share/kivy-examples/svg/main.py&
#exec python3 /usr/share/kivy-examples/tutorials/notes/final/main.py&
#exec python3 /usr/share/kivy-examples/widgets/sequenced_images/main.py&

#exec python3 /usr/share/kivy-examples/tutorials/pong/main.py&
#exec python3 /usr/share/kivy-examples/tutorials/pong/steps/step1/main.py&
#exec python3 /usr/share/kivy-examples/tutorials/pong/steps/step2/main.py&
#exec python3 /usr/share/kivy-examples/tutorials/pong/steps/step3/main.py&
#exec python3 /usr/share/kivy-examples/tutorials/pong/steps/step4/main.py&
#exec python3 /usr/share/kivy-examples/tutorials/pong/steps/step5/main.py&

