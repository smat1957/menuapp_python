# menuapp_python
menu for selecting a video data to play  

This application was developped on the raspberry pi 4.  

WORK_DIR : /home/pi/Videos is assumed as WORKING_DIRECTORY  
all of the following files should be putted on the WORKING_DITECTORY  
excep for MENU which is the short cut(link) icon to be on the Desktop  

1. MENU : This is putted on the Desktop as an icon.  
          short cut(link) to the WORK_DIR/menu.sh  
2. menu.sh : this executes the menu0.py with python3  
3. menu0.py : source program of main procedure written by the python   
          (1) read menu items from menu.csv  
          (2) display the menu items on a monitor (pygame)   
          (3) get a key board event (pygame.locals)  
          (4) according to the key event,  
             set the file name of video to fname and   
             run a subprocess of the shell show.sh with fname as its argument   
4. menu.csv : contains menu items to display on the monitor and its video file name   
          [message to display line, name of the corresponding video file]  
          the extension part of the video file name have to be omitted.   
5. show.sh : execute the application vlc with full screen option.  
          the 1st argument of this shell is the name of the specific video   
6. show_all : same as above show.sh  
          10 video files' names have to be specified with fname  

video data files are putted on the "gg" directory , WORK_DIR/gg/xxxxxx.mp4
