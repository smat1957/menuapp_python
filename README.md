# menuapp_python
menu for selecting a video data to play
</br>
This application was developped on the raspberry pi 4.
</br>

WORK_DIR : /home/pi/Videos is assumed as WORKING_DIRECTORY</br>
all of the following files should be putted on the WORKING_DITECTORY</br>
excep for MENU which is the short cut(link) icon to be on the Desktop</br>
</br>
(1)MENU : This is putted on the Desktop as an icon.</br>
          short cut(link) to the WORK_DIR/menu.sh</br>
(2)menu.sh : this executes the menu0.py with python3</br>
(3)menu0.py : source program of main procedure written by the python</br> 
          1. read menu items from menu.csv</br> 
          2. display the menu items on a monitor (pygame)</br> 
          3. get a key board event (pygame.locals)</br> 
          4. according to the key event, </br> 
             set the file name of video to fname and</br> 
             run a subprocess of the shell show.sh with fname as its argument</br> 
(4)menu.csv : contains menu items to display on the monitor and its video file name</br> 
          [message to display line, name of the corresponding video file]</br> 
          the extension part of the video file name have to be omitted.</br> 
(5)show.sh : execute the application vlc with full screen option.</br> 
          the 1st argument of this shell is the name of the specific video</br> 
(6)show_all : same as above show.sh</br>
          10 video files' names have to be specified with fname</br>
</br>
video data files are putted on the "gg" directory , WORK_DIR/gg/xxxxxx.mp4
