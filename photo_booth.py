# import the necessary packages
from __future__ import print_function
from pyui import PhotoBoothApp
from imutils.video import VideoStream
import argparse
import time


# initialize the video stream and allow the camera sensor to warmup
print("[INFO] warming up camera...")
vs = VideoStream(0).start()
time.sleep(2.0)
outputPath = ".\\photos"
# start the app
pba = PhotoBoothApp(vs,outputPath)

pba.root.mainloop()



