
#introduction to computer vision with python

This intro is going to stick to cv2 and python 2, even though there are many other computer vision tools out there.

## Before you get there

If you have trouble with this, we will do troubleshooting during the last third of the tutorial.  However, if you want to follow along during the middle third, get the packages in place.

Numpy and opencv are compiled packages, so either you will need to install binaries, or have a compiler ready to go. Mostly this will be difficult for the windows folks.

### Linux

Instal with your favorite package manager

* apt-get install python
* apt-get install python-numpy
* apt-get install python-opencv


### OSX

* brew install python
* pip install numpy
* brew tap homebrew/science
* brew install opencv (will require compilation!)

check [here](https://jjyap.wordpress.com/2014/05/24/installing-opencv-2-4-9-on-mac-osx-with-python-support/) for more details

### Windows

If you have a compiler
* install python
  * https://www.python.org/downloads/
* pip install numpy
* openCV
  * is opencv pip installable?


If you don't have a compiler
* install python
    * https://www.python.org/downloads/
* install prereqs
 * numpy: http://sourceforge.net/projects/numpy/files/NumPy/1.9.2/
 * note: the link on scipy.org leads to an old version of numpy
* install openCV
  * http://opencv.org/
* install cv2 bindings for python
  * copy cv2.pyd to site-packages
  * [more here](http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html)

## What's next

* see if opencv is working by running hello.py
* see if your webcam works
  * sanity check in another app if needed
  * run livecam.py
* next steps
  * read a video?
  * some detection stuff
  * frame rate
