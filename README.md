# menuapp_python
To select a video data from menu  

This application was developped on the raspberry pi 4.  

WORK_DIR : /home/pi/Videos is assumed as WORKING_DIRECTORY  
all of the following files should be putted on the WORKING_DITECTORY  
excep for MENU which is the short cut(link) icon to be on the Desktop  

1. MENU : This is putted on the Desktop as an icon.  
          short cut(link) to the WORK_DIR/menu.sh  
2. menu.sh : this shell executes the menu.py  
3. menu.py : main procedure written in python   
          menu0.py(pygame), menu1.py(thinter)  
          (1) read menu items from menu.csv  
          (2) display the menu items on a monitor (pygame, tkinter)   
          (3) get a key board event  
          (4) according to the key event,  
             set the file name of video to fname and   
             run a subprocess of the shell show.sh with fname as its argument   
4. menu.csv : contains menu items to display on the monitor and its video file name   
          [message to display line, name of the corresponding video file]  
          the extension part of the video file name have to be omitted.   
5. show.sh : execute the application vlc with full screen option.  
          the 1st argument of this shell is the name of the specific video   
6. show_all.sh : same as the above shell show.sh  
          10 video files' names have to be specified with fname  

video data files are putted on the "gg" directory , WORK_DIR/gg/xxxxxx.mp4

=======================================  

additional functions as follows  

1. when the machine power is on, this application wakes up automatically  
    $ &nbsp; mkdir &nbsp; -p &nbsp; ~/.config/lxsession/LXDE-pi  
    $ &nbsp; cp &nbsp; /etc/xdg/lxsession/LXDE-pi/autostart &nbsp; ~/.config/lxsession/LXDE-pi/    
    $ &nbsp; echo &nbsp; '/home/pi/Videos/menu.sh' &nbsp; >> &nbsp; ~/.config/lxsession/LXDE-pi/autostart  

2. after this application wakes up, 9 hours(=540 minites) later,  
   nothing to do with human dealings, the normal shutdown will be occurred  

     at the first step of the program 'menu.py',  
             .....  
         os.system("sudo shutdown -h " + "+540")  
             .....  

3. video data watching log will be stored for each selection  
